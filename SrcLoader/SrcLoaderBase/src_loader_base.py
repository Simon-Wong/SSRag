from abc import ABC, abstractmethod

class BaseSrcLoader(ABC):
    '''一个资源加载器基类'''
    def __init__(self):
        pass

    @abstractmethod
    def load(self, **kwarg):
        pass
