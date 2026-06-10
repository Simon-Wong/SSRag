import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from Loader import ParameterLoaderImageContent,LoaderImageContent,ResultLoader

def Test1_LoaderImageContent():
    sl=LoaderImageContent()

    param=ParameterLoaderImageContent(pathfile="test/data/blabla.PNG")
    
    res = sl.load(param)
    
    if isinstance(res, ResultLoader):
        res:ResultLoader
        print(res.src_type) 
        print(res.src_data)

    param=ParameterLoaderImageContent(pathfile="test/data/blabla.PNG",max_tokens=500)
    res = sl.load(param)
    
    if isinstance(res, ResultLoader):
        res:ResultLoader
        print(res.src_type) 
        print(res.src_data)
    

def Test2_LoaderImageContent_to_documents():
    sl=LoaderImageContent()

    param=ParameterLoaderImageContent(pathfile="test/data/blabla.JPG")  
    
    res = sl.load(param)

    res2=ResultLoader(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':   
    Test1_LoaderImageContent()
    Test2_LoaderImageContent_to_documents() 
