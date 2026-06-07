import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from SrcLoader import ParameterSrcMD,SrcLoaderMD,BaseResultSrc,ResultSrc

def Test1_SrcLoaderMD():
    sl=SrcLoaderMD()

    src_param=ParameterSrcMD(pathfile="test/data/blabla.md",mode="single")
    
    res = sl.load(src_param)
    
    if isinstance(res, ResultSrc):
        res:ResultSrc
        print(res.src_type)
        print(res.src_data)

def Test2_SrcLoaderMD_to_documents():
    sl=SrcLoaderMD()

    src_param=ParameterSrcMD(pathfile="test/data/blabla.md")
    
    res = sl.load(src_param)

    res2=ResultSrc(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':
    Test1_SrcLoaderMD()
    Test2_SrcLoaderMD_to_documents() 
