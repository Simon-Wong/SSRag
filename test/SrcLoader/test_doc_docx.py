import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from SrcLoader import ParameterSrcDocDocx,SrcLoaderDocDocx,BaseResultSrc,ResultSrc

def Test1_SrcLoaderDocDocx():
    sl=SrcLoaderDocDocx()

    src_param=ParameterSrcDocDocx(pathfile="test/data/blabla.doc")
    
    res = sl.load(src_param)

    if isinstance(res, ResultSrc):
        res:ResultSrc
        print(res.src_type)
        print(res.src_data)

def Test2_SrcLoaderDocDocx_to_documents():
    sl=SrcLoaderDocDocx()

    src_param=ParameterSrcDocDocx(pathfile="test/data/blabla.docx")
    
    res = sl.load(src_param)
    
    res2=ResultSrc(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':
    Test1_SrcLoaderDocDocx()
    Test2_SrcLoaderDocDocx_to_documents() 
