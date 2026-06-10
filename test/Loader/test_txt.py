import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from Loader import ParameterLoaderTxt,LoaderTxt,ResultLoder

def Test1_LoaderTxt():
    sl=LoaderTxt()

    src_param=ParameterLoaderTxt(pathfile="test/data/blabla.txt")
    
    res = sl.load(src_param)

    if isinstance(res, ResultLoder):
        res:ResultLoder
        print(res.src_type)
        print(res.src_data)

def Test2_LoaderTxt_to_documents():
    sl=LoaderTxt()

    src_param=ParameterLoaderTxt(pathfile="test/data/blabla.txt")
    
    res = sl.load(src_param)
    
    res2=ResultLoder(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':
    Test1_LoaderTxt()
    Test2_LoaderTxt_to_documents() 
