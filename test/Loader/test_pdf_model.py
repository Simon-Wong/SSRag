import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from Loader import ParameterLoaderPDFModel,LoaderPDFModel,ResultLoder

def Test1_LoaderPDFModel():
    sl=LoaderPDFModel()

    param=ParameterLoaderPDFModel(pathfile="test/data/blabla2.pdf")
    
    res = sl.load(param)
    
    if isinstance(res, ResultLoder):
        res:ResultLoder
        print(res.src_type) 
        print(res.src_data)

    param=ParameterLoaderPDFModel(pathfile="test/data/blabla2.pdf",max_tokens=500)
    res = sl.load(param)
    
    if isinstance(res, ResultLoder):
        res:ResultLoder
        print(res.src_type) 
        print(res.src_data)
    

def Test2_LoaderPDFModel_to_documents():
    sl=LoaderPDFModel()

    param=ParameterLoaderPDFModel(pathfile="test/data/blabla2.pdf")  
    
    res = sl.load(param)

    res2=ResultLoder(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':   
    # Test1_LoaderPDFModel()
    Test2_LoaderPDFModel_to_documents() 
