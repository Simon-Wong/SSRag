import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from SrcLoader import ParameterSrcPDFModel,SrcLoaderPDFModel,BaseResultSrc,ResultSrc

def Test1_SrcLoaderPDFModel():
    sl=SrcLoaderPDFModel()

    src_param=ParameterSrcPDFModel(pathfile="test/data/blabla2.pdf")
    
    res = sl.load(src_param)
    
    if isinstance(res, ResultSrc):
        res:ResultSrc
        print(res.src_type) 
        print(res.src_data)

    src_param=ParameterSrcPDFModel(pathfile="test/data/blabla2.pdf",max_tokens=500)
    res = sl.load(src_param)
    
    if isinstance(res, ResultSrc):
        res:ResultSrc
        print(res.src_type) 
        print(res.src_data)
    

def Test2_SrcLoaderPDFModel_to_documents():
    sl=SrcLoaderPDFModel()

    src_param=ParameterSrcPDFModel(pathfile="test/data/blabla2.pdf")  
    
    res = sl.load(src_param)

    res2=ResultSrc(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':   
    # Test1_SrcLoaderPDFModel()
    Test2_SrcLoaderPDFModel_to_documents() 
