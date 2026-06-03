from ..SrcLoaderBase import BaseSrcLoader

class SrcLoaderTxt(BaseSrcLoader):
    def __init__(self):
        super().__init__()
    
    def load(self, **kwarg):
        print("SrcLoaderTxt load")