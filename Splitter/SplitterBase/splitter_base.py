from SrcLoader import BaseSrcLoader

from abc import ABC,abstractmethod

'''

src----->BaseParameterLoader
            |
            V
            BaseLoader----->BaseResultLoder
                                     |
                                     V
                                     BaseSplitter----->BaseResultSplitter

'''
class BaseResultSplitter(ABC):
    def __init__(self):
        pass

class BaseSplitter(ABC):
    def __init__(self):
        pass    
