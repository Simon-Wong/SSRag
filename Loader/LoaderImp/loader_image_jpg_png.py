from ..LoaderBase import BaseParameterLoader, BaseLoader, BaseResultLoader,ResultLoader

from pathlib import Path
from typing import Any


from langchain_community.document_loaders import UnstructuredImageLoader


class ParameterLoaderImageJpgPng(BaseParameterLoader):
    '''
    一个JPG和PNG文件加载器参数
    封装了UnstructuredImageLoader的参数，用于加载JPG和PNG文件
    '''
    mode: str = "single"
    languages: list[str] = []
    unstructured_kwargs: Any = None

    def __init__(self, pathfile: str|Path, mode: str = "single", languages: list[str] = ['chi_sim','eng'],  **kwarg):
        super().__init__(pathfile)
        self.mode=mode
        self.languages=languages
        self.unstructured_kwargs=kwarg

class LoaderImageJpgPng(BaseLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,param: BaseParameterLoader, **kwarg)->BaseResultLoader:
        if isinstance(param, ParameterLoaderImageJpgPng):
            param:ParameterLoaderImageJpgPng
            
            loader = UnstructuredImageLoader(param.pathfile,
                                                mode=param.mode, 
                                                languages=param.languages,
                                                **param.unstructured_kwargs)    
            return ResultLoader(loader.load())
            
        else:
            raise ValueError("param must be a ParameterLoaderImageJpgPng")
