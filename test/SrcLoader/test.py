import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from SrcLoader import ParameterSrcTxt,SrcLoaderTxt,BaseResultSrc,ResultSrc

def Test1_SrcLoaderTxt():
    sl=SrcLoaderTxt()

    src_param=ParameterSrcTxt(pathfile="test/data/blabla.txt")
    
    res = sl.load(src_param)
    if isinstance(res, ResultSrc):
        print(res.src_type)
        print(res.src_data)

def Test2_ParameterSrcTxt_to_documents():
    sl=SrcLoaderTxt()

    src_param=ParameterSrcTxt(pathfile="test/data/blabla.txt")
    
    res = sl.load(src_param)
    res2=ResultSrc(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':
    Test1_SrcLoaderTxt()
    Test2_ParameterSrcTxt_to_documents() 
