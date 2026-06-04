from ..SrcLoaderBase import BaseParameterSrc, BaseSrcLoader
from pathlib import Path
from langchain_core.documents import Document

import os
from langchain_community.document_loaders import TextLoader

class ParameterSrcTxt(BaseParameterSrc):
    '''一个文本加载器参数'''
    encoding: str|None = None
    autodetect_encoding: bool = False

    def __init__(self, pathfile: str|Path, encoding: str|None = None, autodetect_encoding: bool = False):
        super().__init__(pathfile)

        self.encoding = encoding
        self.autodetect_encoding = autodetect_encoding

class SrcLoaderTxt(BaseSrcLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,src_param: BaseParameterSrc, **kwarg)->list[Document]:
        if isinstance(src_param, ParameterSrcTxt):
            tl = TextLoader(src_param.pathfile, 
                                encoding=src_param.encoding, 
                                autodetect_encoding=src_param.autodetect_encoding)
            return tl.load()
        else:
            raise ValueError("src_param must be a ParameterSrcTxt")
