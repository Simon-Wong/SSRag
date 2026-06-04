from abc import ABC, abstractmethod
from pathlib import Path
from langchain_core.documents import Document

class BaseParameterSrc:
    '''一个资源参数基类'''
    pathfile: str|Path # 资源文件路径

    def __init__(self, pathfile: str|Path):
        self.pathfile = pathfile

class BaseSrcLoader(ABC):
    '''一个资源加载器基类'''
    src_param: BaseParameterSrc = None # 资源参数
    def __init__(self):
        pass

    @abstractmethod
    def load(self,src_param: BaseParameterSrc, **kwarg)->list[Document]:
        pass
