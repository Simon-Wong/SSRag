from ..LoaderBase import BaseParameterLoader, BaseLoader, BaseResultLoder,ResultLoder

from pathlib import Path
from typing import Callable, Dict,Literal,Any


class ParameterLoaderPDF(BaseParameterLoader):
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

class LoaderPDF(BaseLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,param: BaseParameterLoader, **kwarg)->BaseResultLoder:
        if isinstance(param, ParameterLoaderPDF):
            param:ParameterLoaderPDF
            
            if param.using_loader=="UnstructuredLoader":

                from langchain_unstructured import UnstructuredLoader
                argdict=param.kwargs
                loader = UnstructuredLoader(param.pathfile,
                                            strategy=param.strategy)

            elif param.using_loader=="fake_no_impl":
                raise ValueError(f"the value of using_loader {param.using_loader}  is not implemented")

            return ResultLoder(loader.load())
            
        else:
            raise ValueError("param must be a ParameterLoaderPDF")
