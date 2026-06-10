import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from Loader import ParameterLoaderXlsXlsx,LoaderXlsXlsx,ResultLoder

def Test1_LoaderXlsXlsx():
    sl=LoaderXlsXlsx()

    param=ParameterLoaderXlsXlsx(pathfile="test/data/blabla.xlsx")
    
    res = sl.load(param)
    
    if isinstance(res, ResultLoder):
        res:ResultLoder
        print(res.src_type)
        print(res.src_data)

def Test2_Loader_to_documents():
    sl=LoaderXlsXlsx()

    param=ParameterLoaderXlsXlsx(pathfile="test/data/blabla.xls")
    
    res = sl.load(param)

    res2=ResultLoder(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':
    Test1_LoaderXlsXlsx()
    Test2_Loader_to_documents() 
