import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from Loader import ParameterLoaderDocDocx,LoaderDocDocx,ResultLoader

def Test1_LoaderDocDocx():
    sl=LoaderDocDocx()

    param=ParameterLoaderDocDocx(pathfile="test/data/blabla.doc")
    
    res = sl.load(param)

    if isinstance(res, ResultLoader):
        res:ResultLoader
        print(res.src_type)
        print(res.src_data)

def Test2_LoaderDocDocx_to_documents():
    sl=LoaderDocDocx()

    param=ParameterLoaderDocDocx(pathfile="test/data/blabla.docx")
    
    res = sl.load(param)
    
    res2=ResultLoader(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':
    Test1_LoaderDocDocx()
    Test2_LoaderDocDocx_to_documents() 
