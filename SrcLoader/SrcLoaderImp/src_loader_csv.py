from ..SrcLoaderBase import BaseParameterSrc, BaseSrcLoader, BaseResultSrc


class ParameterSrcCSV(BaseParameterSrc):
    '''一个CSV加载器参数'''
    def __init__(self):
        pass

class SrcLoaderCSV(BaseSrcLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,src_param: BaseParameterSrc, **kwarg)->BaseResultSrc:
        return BaseResultSrc([])
