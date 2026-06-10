import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from Loader import ParameterLoaderImageOCR,LoaderImageOCR,ResultLoader

def Test1_LoaderImageOCR():
    sl=LoaderImageOCR()

    param=ParameterLoaderImageOCR(pathfile="test/data/blabla.PNG")
    
    res = sl.load(param)
    
    if isinstance(res, ResultLoader):
        res:ResultLoader
        print(res.src_type) 
        print(res.src_data)

    param=ParameterLoaderImageOCR(pathfile="test/data/blabla.PNG")
    res = sl.load(param)
    
    if isinstance(res, ResultLoader):
        res:ResultLoader
        print(res.src_type) 
        print(res.src_data)
    

def Test2_LoaderImageOCR_to_documents():
    sl=LoaderImageOCR()

    param=ParameterLoaderImageOCR(pathfile="test/data/blabla.JPG",reocr=True)  
    
    res = sl.load(param)

    res2=ResultLoader(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':   
    Test1_LoaderImageOCR()
    Test2_LoaderImageOCR_to_documents() 
