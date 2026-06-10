import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from SrcLoader import ParameterSrcLoderImageOCRModel,SrcLoaderImageOCRModel,BaseResultSrcLoder,ResultSrcLoder

def Test1_SrcLoaderImageOCRModel():
    sl=SrcLoaderImageOCRModel()

    src_param=ParameterSrcLoderImageOCRModel(pathfile="test/data/blabla.PNG")
    
    res = sl.load(src_param)
    
    if isinstance(res, ResultSrcLoder):
        res:ResultSrcLoder
        print(res.src_type) 
        print(res.src_data)

    src_param=ParameterSrcLoderImageOCRModel(pathfile="test/data/blabla.PNG",max_tokens=300)
    res = sl.load(src_param)
    
    if isinstance(res, ResultSrcLoder):
        res:ResultSrcLoder
        print(res.src_type) 
        print(res.src_data)
    

def Test2_SrcLoaderImageOCRModel_to_documents():
    sl=SrcLoaderImageOCRModel()

    src_param=ParameterSrcLoderImageOCRModel(pathfile="test/data/blabla.JPG")  
    
    res = sl.load(src_param)

    res2=ResultSrcLoder(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':   
    Test1_SrcLoaderImageOCRModel()
    Test2_SrcLoaderImageOCRModel_to_documents() 
