import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from Loader import ParameterLoaderTxt,LoaderTxt,ResultLoader

def Test1_LoaderTxt():
    sl=LoaderTxt()

    param=ParameterLoaderTxt(pathfile="test/data/blabla.txt")
    
    res = sl.load(param)

    if isinstance(res, ResultLoader):
        res:ResultLoader
        print(res.src_type)
        print(res.src_data)

def Test2_LoaderTxt_to_documents():
    sl=LoaderTxt()

    param=ParameterLoaderTxt(pathfile="test/data/blabla.txt")
    
    res = sl.load(param)
    
    res2=ResultLoader(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':
    Test1_LoaderTxt()
    Test2_LoaderTxt_to_documents() 
