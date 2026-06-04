from ..SrcLoaderBase import BaseParameterSrc, BaseSrcLoader, BaseResultSrc,ResultSrc

from pathlib import Path
from typing import Any


from langchain_community.document_loaders import UnstructuredMarkdownLoader


class ParameterSrcMD(BaseParameterSrc):
    '''
    一个MD加载器参数
    封装了UnstructuredMarkdownLoader的参数，用于加载MD文件
    '''
    mode: str = "elements"
    unstructured_kwargs: Any = None

    def __init__(self, pathfile: str|Path, mode: str = "elements", **kwarg):
        super().__init__(pathfile)
        self.mode=mode
        self.unstructured_kwargs=kwarg

class SrcLoaderMD(BaseSrcLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,src_param: BaseParameterSrc, **kwarg)->BaseResultSrc:
        if isinstance(src_param, ParameterSrcMD):

            loader = UnstructuredMarkdownLoader(src_param.pathfile,
                                                mode=src_param.mode, 
                                                **src_param.unstructured_kwargs)
            return ResultSrc(loader.load())
            
        else:
            raise ValueError("src_param must be a ParameterSrcMD")
