import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from Loader import ParameterLoaderImageJpgPng,LoaderImageJpgPng,ResultLoder

def Test1_LoaderImageJpgPng():
    sl=LoaderImageJpgPng()

    src_param=ParameterLoaderImageJpgPng(pathfile="test/data/blabla.PNG")
    
    res = sl.load(src_param)
    
    if isinstance(res, ResultLoder):
        res:ResultLoder
        print(res.src_type) 
        print(res.src_data)

def Test2_LoaderImageJpgPng_to_documents():
    sl=LoaderImageJpgPng()

    src_param=ParameterLoaderImageJpgPng(pathfile="test/data/blabla.JPG")  
    
    res = sl.load(src_param)

    res2=ResultLoder(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':   
    Test1_LoaderImageJpgPng()
    #Test2_LoaderImageJpgPng_to_documents() 
