from ..SrcLoaderBase import BaseParameterSrc, BaseSrcLoader, BaseResultSrc,ResultSrc

from pathlib import Path

from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader

class ParameterSrcTxt(BaseParameterSrc):
    '''
    一个txt加载器参数
    封装了TextLoader的参数，用于加载txt文件
    '''
    encoding: str|None = None
    autodetect_encoding: bool = False

    def __init__(self, pathfile: str|Path, encoding: str|None = None, autodetect_encoding: bool = False):
        super().__init__(pathfile)

        self.encoding = encoding
        self.autodetect_encoding = autodetect_encoding

class SrcLoaderTxt(BaseSrcLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,src_param: BaseParameterSrc, **kwarg)->BaseResultSrc:
        if isinstance(src_param, ParameterSrcTxt):

            # 不同的子类这里使用不同的方式加载资源数据
            tl = TextLoader(src_param.pathfile, 
                                encoding=src_param.encoding, 
                                autodetect_encoding=src_param.autodetect_encoding)

            return ResultSrc(tl.load())
        else:
            raise ValueError("src_param must be a ParameterSrcTxt")
