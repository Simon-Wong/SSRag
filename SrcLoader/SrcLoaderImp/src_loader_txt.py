from ..SrcLoaderBase import BaseParameterSrcLoder, BaseSrcLoader, BaseResultSrcLoder,ResultSrcLoder

from pathlib import Path

from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader

class ParameterSrcLoderTxt(BaseParameterSrcLoder):
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

class SrcLoaderTxt(BaseSrcLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,src_param: BaseParameterSrcLoder, **kwarg)->BaseResultSrcLoder:
        if isinstance(src_param, ParameterSrcLoderTxt):
            src_param:ParameterSrcLoderTxt
            
            # 不同的子类这里使用不同的方式加载资源数据
            tl = TextLoader(src_param.pathfile, 
                            encoding=src_param.encoding, 
                            autodetect_encoding=src_param.autodetect_encoding)

            return ResultSrcLoder(tl.load())
        else:
            raise ValueError("src_param must be a ParameterSrcLoderTxt")
