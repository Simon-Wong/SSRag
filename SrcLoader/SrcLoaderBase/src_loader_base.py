from abc import ABC, abstractmethod

class BaseParameterSrc:
    '''一个资源参数基类'''
    def __init__(self):
        pass

class BaseSrcLoader(ABC):
    '''一个资源加载器基类'''
    src_param: BaseParameterSrc = None # 资源参数
    def __init__(self):
        pass

    @abstractmethod
    def load(self,src_param: BaseParameterSrc, **kwarg):
        pass
