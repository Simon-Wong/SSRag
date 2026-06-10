from ..LoaderBase import BaseParameterLoader, BaseLoader, BaseResultLoder,ResultLoder

from pathlib import Path

from langchain_core.documents import Document
from langchain_unstructured import UnstructuredLoader


class ParameterLoaderDocDocx(BaseParameterLoader):
    '''
    一个docx加载器参数
    封装了UnstructuredLoader的参数，用于加载docx文件
    partition_via_api: 是否使用API模式加载，默认False
    ''' 
    partition_via_api=False

    def __init__(   self, 
                    pathfile: str|Path, 
                    partition_via_api=False,
                    **kwarg):
        super().__init__(pathfile)
        
        self.partition_via_api=partition_via_api
        self.kwarg = kwarg

class LoaderDocDocx(BaseLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,param: BaseParameterLoader, **kwarg)->BaseResultLoder:
        if isinstance(param, ParameterLoaderDocDocx):
            param:ParameterLoaderDocDocx
            
            tl = UnstructuredLoader(param.pathfile,
                                    partition_via_api=param.partition_via_api,
                                    **param.kwarg)

            return ResultLoder(tl.load())
        else:
            raise ValueError("param must be a ParameterLoaderDocDocx")
