from ..LoaderBase import BaseParameterLoader, BaseLoader, BaseResultLoader,ResultLoader

from pathlib import Path
from typing import Dict,Sequence

import csv
from langchain_community.document_loaders import CSVLoader
from langchain_core.documents import Document

from typing import Iterator
from io import TextIOWrapper
import datetime
import random

import os
import pandas as pd


def split_excel_to_csvs(excel_path: str|Path, encoding: str, output_dir: str|None=None)->tuple[list[str],list[str]]:
    """
    将Excel文件的每个sheet保存为独立的CSV文件
    命名规则: {excel文件名(不含扩展名)}-{sheet名}.csv
    返回生成的CSV文件路径列表
    """
    if output_dir is None:
        output_dir = os.path.dirname(excel_path) or '.'
    os.makedirs(output_dir, exist_ok=True)

    # 获取Excel基础名称（不含扩展名）
    base_name = os.path.splitext(os.path.basename(excel_path))[0]

    # 读取所有sheet，sheet_name=None返回字典 {sheet_name: DataFrame}
    all_sheets = pd.read_excel(excel_path, sheet_name=None)

    csv_files = []
    sheet_names = []
    for sheet_name, df in all_sheets.items():
        # 清理sheet名称中的非法文件名字符（如 / \ : * ? " < > |）
        safe_sheet_name = "".join(c for c in sheet_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
        # 如果清理后为空，使用随机名称
        if not safe_sheet_name:
            safe_sheet_name = "sheet" +"_"+str(datetime.datetime.now())+"_"+ str(random.randint(0, 1000000))

        csv_filename = f"{base_name}-{safe_sheet_name}.csv"
        csv_pathfile = os.path.join(output_dir, csv_filename)

        # 保存为CSV（不包含索引）
        df.to_csv(csv_pathfile, index=False, encoding=encoding)
        csv_files.append(csv_pathfile)
        #print(f"已生成: {csv_pathfile} (共 {len(df)} 行)")
        sheet_names.append(safe_sheet_name)

    return csv_files,sheet_names


class CSVLoader_XlsXlsx(CSVLoader):
    '''
    修改了CSVLoader，增加了source_custom参数、sheet_name参数
    __read_file方法中使用了self.source_column、self.sheet_name
    由于__read_file是私有方法，所以不能直接调用，只能通过lazy_load方法调用
    '''
    source_custom: str|None=None

    def __init__(self, file_path: str|Path, **kwarg):
        self.source_custom=kwarg.pop("source_custom",None)
        self.sheet_name=kwarg.pop("sheet_name",None)
        #print(f"self.source_custom:{self.source_custom}")

        super().__init__(file_path, **kwarg)

    def lazy_load(self) -> Iterator[Document]:
        try:
            with open(self.file_path, newline="", encoding=self.encoding) as csvfile:
                yield from self.__read_file(csvfile)
        except UnicodeDecodeError as e:
            if self.autodetect_encoding:
                detected_encodings = detect_file_encodings(self.file_path)
                for encoding in detected_encodings:
                    try:
                        with open(
                            self.file_path, newline="", encoding=encoding.encoding
                        ) as csvfile:
                            yield from self.__read_file(csvfile)
                            break
                    except UnicodeDecodeError:
                        continue
            else:
                raise RuntimeError(f"Error loading {self.file_path}") from e
        except Exception as e:
            raise RuntimeError(f"Error loading {self.file_path}") from e

    def __read_file(self, csvfile: TextIOWrapper) -> Iterator[Document]:
        csv_reader = csv.DictReader(csvfile, **self.csv_args)
        for i, row in enumerate(csv_reader):

            #修改了source的处理逻辑
            try:
                if self.source_custom is not None:
                    source=self.source_custom
                else:
                    source = (
                        row[self.source_column]
                        if self.source_column is not None
                        else str(self.file_path)
                    )
            except KeyError:
                raise ValueError(
                    f"Source column '{self.source_column}' not found in CSV file."
                )
            content = "\n".join(
                f"""{k.strip() if k is not None else k}: {
                    v.strip()
                    if isinstance(v, str)
                    else ",".join(map(str.strip, v))
                    if isinstance(v, list)
                    else v
                }"""
                for k, v in row.items()
                if (
                    k in self.content_columns
                    if self.content_columns
                    else k not in self.metadata_columns
                )
            )
            if self.sheet_name is not None:
                 metadata = {"source": source, "row": i, "sheet_name": self.sheet_name}
            else:
                metadata = {"source": source, "row": i}

            for col in self.metadata_columns:
                try:
                    metadata[col] = row[col]
                except KeyError:
                    raise ValueError(f"Metadata column '{col}' not found in CSV file.")
            yield Document(page_content=content, metadata=metadata)


class ParameterLoaderXlsXlsx(BaseParameterLoader):
    '''
    一个Excel加载器参数
    封装了CSVLoader的参数，用于加载Excel文件
    '''
    source_column: str|None=None
    metadata_columns: Sequence[str]=()
    csv_args: Dict|None=None
    encoding: str|None=None
    autodetect_encoding: bool=False
    content_columns: Sequence[str]=()
    sheet_name: str|None=None
    temp_dir: str|None=None

    def __init__(self, 
                    pathfile: str|Path,
                    sheet_name: str|None=None,
                    temp_dir: str|None=None,
                    encoding: str|None=None, 
                    source_column: str|None=None, 
                    metadata_columns: Sequence[str]=(), 
                    csv_args: Dict|None=None, 
                    autodetect_encoding: bool=False, 
                    content_columns: Sequence[str]=(),
                    **kwarg):
        super().__init__(pathfile)
        
        self.sheet_name=sheet_name
        self.temp_dir=temp_dir
        self.encoding=encoding
        self.source_column=source_column
        self.metadata_columns=metadata_columns
        self.csv_args=csv_args
        self.autodetect_encoding=autodetect_encoding
        self.content_columns=content_columns


class LoaderXlsXlsx(BaseLoader):
    def __init__(self):
        super().__init__()

    def load(self,param: BaseParameterLoader, **kwarg)->BaseResultLoader:
        if isinstance(param, ParameterLoaderXlsXlsx):
            param:ParameterLoaderXlsXlsx
            all_documents=[]

            # 不同的子类这里使用不同的方式加载资源数据
            try:
                csv_files,sheet_names = split_excel_to_csvs(param.pathfile, param.encoding, param.temp_dir)

                for csv_pathfile,sheet_name in zip(csv_files,sheet_names):
                    loader = CSVLoader_XlsXlsx(csv_pathfile, 
                                source_custom=f"{param.pathfile.as_posix()}",
                                sheet_name=sheet_name,
                                metadata_columns=param.metadata_columns,
                                csv_args=param.csv_args,
                                encoding=param.encoding,
                                autodetect_encoding=param.autodetect_encoding, 
                                content_columns=param.content_columns)
                    documents = loader.load()
                    all_documents.extend(documents)
            
            except Exception as e:
                raise ValueError(f"Error loading Excel file: {e}")

            finally:
                # 确保删除临时的CSV文件
                for csv_path in csv_files:
                    os.remove(csv_path)
            
            return ResultLoader(all_documents)

        else:
            raise ValueError("param must be a ParameterLoaderXlsXlsx")
