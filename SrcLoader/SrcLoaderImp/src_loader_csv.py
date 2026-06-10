from ..SrcLoaderBase import BaseParameterSrcLoder, BaseSrcLoader, BaseResultSrcLoder,ResultSrcLoder

from pathlib import Path
from typing import Dict,Sequence

from langchain_community.document_loaders import CSVLoader

class ParameterSrcLoderCSV(BaseParameterSrcLoder):
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

class SrcLoaderCSV(BaseSrcLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,src_param: BaseParameterSrcLoder, **kwarg)->BaseResultSrcLoder:
        if isinstance(src_param, ParameterSrcLoderCSV):
            src_param:ParameterSrcLoderCSV
            
            loader = CSVLoader(src_param.pathfile, 
                                source_column=src_param.source_column,
                                metadata_columns=src_param.metadata_columns,
                                csv_args=src_param.csv_args,
                                encoding=src_param.encoding,
                                autodetect_encoding=src_param.autodetect_encoding, 
                                content_columns=src_param.content_columns)
    
            return ResultSrcLoder(loader.load())
        else:
            raise ValueError("src_param must be a ParameterSrcLoderCSV")
