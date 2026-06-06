import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from SrcLoader import ParameterSrcImageJpgPng,SrcLoaderImageJpgPng,BaseResultSrc,ResultSrc

def Test1_SrcLoaderImageJpgPng():
    sl=SrcLoaderImageJpgPng()

    src_param=ParameterSrcImageJpgPng(pathfile="test/data/blabla.PNG")
    
    res = sl.load(src_param)
    
    if isinstance(res, ResultSrc):
        res:ResultSrc=res
        print(res.src_type) 
        print(res.src_data)

def Test2_SrcLoaderImageJpgPng_to_documents():
    sl=SrcLoaderImageJpgPng()

    src_param=ParameterSrcImageJpgPng(pathfile="test/data/blabla.JPG")  
    
    res = sl.load(src_param)

    res2=ResultSrc(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':   
    Test1_SrcLoaderImageJpgPng()
    #Test2_SrcLoaderImageJpgPng_to_documents() 
