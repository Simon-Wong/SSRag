import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from SrcLoader import ParameterSrcLoderPPT,SrcLoaderPPT,BaseResultSrcLoder,ResultSrcLoder

def Test1_SrcLoaderPPT():
    sl=SrcLoaderPPT()

    src_param=ParameterSrcLoderPPT(pathfile="test/data/blabla.pptx")
    
    res = sl.load(src_param)
    
    if isinstance(res, ResultSrcLoder):
        res:ResultSrcLoder
        print(res.src_type)
        print(res.src_data)

def Test2_SrcLoaderPPT_to_documents():
    sl=SrcLoaderPPT()

    src_param=ParameterSrcLoderPPT(pathfile="test/data/blabla2.ppt")
    
    res = sl.load(src_param)

    res2=ResultSrcLoder(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

def Test3_SrcLoaderPPT():
    sl=SrcLoaderPPT()

    src_param=ParameterSrcLoderPPT(pathfile="test/data/blabla3.pptx")
    
    res = sl.load(src_param)
    
    if isinstance(res, ResultSrcLoder):
        res:ResultSrcLoder
        print(res.src_type)
        print(res.src_data)
if __name__ =='__main__':
    Test1_SrcLoaderPPT()
    Test2_SrcLoaderPPT_to_documents() 
    Test3_SrcLoaderPPT()
