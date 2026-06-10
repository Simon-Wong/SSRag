from ..LoaderBase import BaseParameterLoader, BaseLoader, BaseResultLoder,ResultLoder

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
    
    def load(self,src_param: BaseParameterLoader, **kwarg)->BaseResultLoder:
        if isinstance(src_param, ParameterLoaderImageJpgPng):
            src_param:ParameterLoaderImageJpgPng
            
            loader = UnstructuredImageLoader(src_param.pathfile,
                                                mode=src_param.mode, 
                                                languages=src_param.languages,
                                                **src_param.unstructured_kwargs)    
            return ResultLoder(loader.load())
            
        else:
            raise ValueError("src_param must be a ParameterLoaderImageJpgPng")
