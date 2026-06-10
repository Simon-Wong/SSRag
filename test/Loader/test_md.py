import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from Loader import ParameterLoaderMD,LoaderMD,ResultLoder

def Test1_LoaderMD():
    sl=LoaderMD()

    param=ParameterLoaderMD(pathfile="test/data/blabla.md",mode="single")
    
    res = sl.load(param)
    
    if isinstance(res, ResultLoder):
        res:ResultLoder
        print(res.src_type)
        print(res.src_data)

def Test2_LoaderMD_to_documents():
    sl=LoaderMD()

    param=ParameterLoaderMD(pathfile="test/data/blabla.md",parse_pic=True)
    
    res = sl.load(param)

    res2=ResultLoder(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':
    Test1_LoaderMD()
    Test2_LoaderMD_to_documents() 
