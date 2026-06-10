import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from Loader import ParameterLoaderImageOCRModel,LoaderImageOCRModel,ResultLoader

def Test1_LoaderImageOCRModel():
    sl=LoaderImageOCRModel()

    param=ParameterLoaderImageOCRModel(pathfile="test/data/blabla.PNG")
    
    res = sl.load(param)
    
    if isinstance(res, ResultLoader):
        res:ResultLoader
        print(res.src_type) 
        print(res.src_data)

    param=ParameterLoaderImageOCRModel(pathfile="test/data/blabla.PNG",max_tokens=300)
    res = sl.load(param)
    
    if isinstance(res, ResultLoader):
        res:ResultLoader
        print(res.src_type) 
        print(res.src_data)
    

def Test2_LoaderImageOCRModel_to_documents():
    sl=LoaderImageOCRModel()

    param=ParameterLoaderImageOCRModel(pathfile="test/data/blabla.JPG")  
    
    res = sl.load(param)

    res2=ResultLoader(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':   
    Test1_LoaderImageOCRModel()
    Test2_LoaderImageOCRModel_to_documents() 
