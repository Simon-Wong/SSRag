import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from Loader import ParameterLoaderPPT,LoaderPPT,ResultLoader

def Test1_LoaderPPT():
    sl=LoaderPPT()

    param=ParameterLoaderPPT(pathfile="test/data/blabla.pptx")
    
    res = sl.load(param)
    
    if isinstance(res, ResultLoader):
        res:ResultLoader
        print(res.src_type)
        print(res.src_data)

def Test2_LoaderPPT_to_documents():
    sl=LoaderPPT()

    param=ParameterLoaderPPT(pathfile="test/data/blabla2.ppt")
    
    res = sl.load(param)

    res2=ResultLoader(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

def Test3_LoaderPPT():
    sl=LoaderPPT()

    param=ParameterLoaderPPT(pathfile="test/data/blabla3.pptx")
    
    res = sl.load(param)
    
    if isinstance(res, ResultLoader):
        res:ResultLoader
        print(res.src_type)
        print(res.src_data)
if __name__ =='__main__':
    Test1_LoaderPPT()
    Test2_LoaderPPT_to_documents() 
    Test3_LoaderPPT()
