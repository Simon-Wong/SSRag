import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from SrcLoader import ParameterSrcLoderImageJpgPng,SrcLoaderImageJpgPng,BaseResultSrcLoder,ResultSrcLoder

def Test1_SrcLoaderImageJpgPng():
    sl=SrcLoaderImageJpgPng()

    src_param=ParameterSrcLoderImageJpgPng(pathfile="test/data/blabla.PNG")
    
    res = sl.load(src_param)
    
    if isinstance(res, ResultSrcLoder):
        res:ResultSrcLoder
        print(res.src_type) 
        print(res.src_data)

def Test2_SrcLoaderImageJpgPng_to_documents():
    sl=SrcLoaderImageJpgPng()

    src_param=ParameterSrcLoderImageJpgPng(pathfile="test/data/blabla.JPG")  
    
    res = sl.load(src_param)

    res2=ResultSrcLoder(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':   
    Test1_SrcLoaderImageJpgPng()
    #Test2_SrcLoaderImageJpgPng_to_documents() 
