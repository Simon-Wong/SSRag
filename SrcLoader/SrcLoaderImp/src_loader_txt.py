from ..SrcLoaderBase import BaseParameterSrc, BaseSrcLoader

import os
from langchain_community.document_loaders import TextLoader

class ParameterSrcTxt(BaseParameterSrc):
    '''一个文本加载器参数'''
    def __init__(self):
        pass

class SrcLoaderTxt(BaseSrcLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,src_param: BaseParameterSrc, **kwarg):
        print("SrcLoaderTxt load")