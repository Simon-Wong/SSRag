from ..SrcLoaderBase import BaseParameterSrc, BaseSrcLoader, BaseResultSrc,ResultSrc

from pathlib import Path
from typing import Callable, Dict,Literal,Any


class ParameterSrcPDF(BaseParameterSrc):
    '''
    一个PDF加载器参数
    封装了UnstructuredLoader的参数，用于加载PDF文件
    '''

    #公共参数
    #using_loader，指定使用的加载器，默认UnstructuredLoader
    #kwargs，其他参数，用于传递给加载器的构造函数
    using_loader:Literal["UnstructuredLoader","fake_no_impl"]="UnstructuredLoader"
    kwargs: Any = None

    #UnstructuredLoader的专属参数
    strategy:str="hi_res"

    # 其他参数
    #.......

    def __init__(   self, 
                    pathfile: str|Path,
                    using_loader:Literal["UnstructuredLoader","fake_no_impl"]="UnstructuredLoader",
                    **kwargs):
        super().__init__(pathfile)
        self.using_loader=using_loader
        self.kwargs=kwargs

class SrcLoaderPDF(BaseSrcLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,src_param: BaseParameterSrc, **kwarg)->BaseResultSrc:
        if isinstance(src_param, ParameterSrcPDF):
            src_param:ParameterSrcPDF
            
            if src_param.using_loader=="UnstructuredLoader":

                from langchain_unstructured import UnstructuredLoader
                argdict=src_param.kwargs
                loader = UnstructuredLoader(src_param.pathfile,
                                            strategy=src_param.strategy)

            elif src_param.using_loader=="fake_no_impl":
                raise ValueError(f"the value of using_loader {src_param.using_loader}  is not implemented")

            return ResultSrc(loader.load())
            
        else:
            raise ValueError("src_param must be a ParameterSrcPDF")
