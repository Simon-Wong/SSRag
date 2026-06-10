from ..LoaderBase import BaseParameterLoader, BaseLoader, BaseResultLoader,ResultLoader

from pathlib import Path

from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader

class ParameterLoaderTxt(BaseParameterLoader):
    '''
    一个txt加载器参数
    封装了TextLoader的参数，用于加载txt文件
    '''
    encoding: str|None = None
    autodetect_encoding: bool = False

    def __init__(   self, 
                    pathfile: str|Path, 
                    encoding: str|None = None, 
                    autodetect_encoding: bool = False,
                    **kwarg):
        super().__init__(pathfile)

        self.encoding = encoding
        self.autodetect_encoding = autodetect_encoding

class LoaderTxt(BaseLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,param: BaseParameterLoader, **kwarg)->BaseResultLoader:
        if isinstance(param, ParameterLoaderTxt):
            param:ParameterLoaderTxt
            
            # 不同的子类这里使用不同的方式加载资源数据
            tl = TextLoader(param.pathfile, 
                            encoding=param.encoding, 
                            autodetect_encoding=param.autodetect_encoding)

            return ResultLoader(tl.load())
        else:
            raise ValueError("param must be a ParameterLoaderTxt")
