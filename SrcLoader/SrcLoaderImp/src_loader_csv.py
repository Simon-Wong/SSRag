from ..SrcLoaderBase import BaseSrcLoader

class SrcLoaderCSV(BaseSrcLoader):
    def __init__(self):
        super().__init__()
    
    def load(self, **kwarg):
        print("SrcLoaderCSV load")