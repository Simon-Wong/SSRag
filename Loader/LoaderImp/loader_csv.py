from ..LoaderBase import BaseParameterLoader, BaseLoader, BaseResultLoader,ResultLoader

from pathlib import Path
from typing import Dict,Sequence

from langchain_community.document_loaders import CSVLoader

class ParameterLoaderCSV(BaseParameterLoader):
    '''
    一个CSV加载器参数
    封装了CSVLoader的参数，用于加载CSV文件
    '''
    source_column: str|None=None
    metadata_columns: Sequence[str]=()
    csv_args: Dict|None=None
    encoding: str|None=None
    autodetect_encoding: bool=False
    content_columns: Sequence[str]=()

    def __init__(self, 
                    pathfile: str|Path,
                    source_column: str|None=None, 
                    metadata_columns: Sequence[str]=(), 
                    csv_args: Dict|None=None, 
                    encoding: str|None=None, 
                    autodetect_encoding: bool=False, 
                    content_columns: Sequence[str]=(),
                    **kwarg):
        super().__init__(pathfile)

        self.source_column=source_column
        self.metadata_columns=metadata_columns
        self.csv_args=csv_args
        self.encoding=encoding
        self.autodetect_encoding=autodetect_encoding
        self.content_columns=content_columns

class LoaderCSV(BaseLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,param: BaseParameterLoader, **kwarg)->BaseResultLoader:
        if isinstance(param, ParameterLoaderCSV):
            param:ParameterLoaderCSV
            
            loader = CSVLoader(param.pathfile, 
                                source_column=param.source_column,
                                metadata_columns=param.metadata_columns,
                                csv_args=param.csv_args,
                                encoding=param.encoding,
                                autodetect_encoding=param.autodetect_encoding, 
                                content_columns=param.content_columns)
    
            return ResultLoader(loader.load())
        else:
            raise ValueError("param must be a ParameterLoaderCSV")
