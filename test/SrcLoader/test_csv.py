import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from SrcLoader import ParameterSrcCSV,SrcLoaderCSV,BaseResultSrc,ResultSrc

def Test1_SrcLoaderCSV():
    sl=SrcLoaderCSV()

    src_param=ParameterSrcCSV(pathfile="test/data/blabla.csv")
    
    res = sl.load(src_param)
    
    if isinstance(res, ResultSrc):
        res:ResultSrc=res
        print(res.src_type)
        print(res.src_data)

def Test2_SrcLoaderCSV_to_documents():
    sl=SrcLoaderCSV()

    src_param=ParameterSrcCSV(pathfile="test/data/blabla.csv")
    
    res = sl.load(src_param)

    res2=ResultSrc(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':
    Test1_SrcLoaderCSV()
    Test2_SrcLoaderCSV_to_documents() 
