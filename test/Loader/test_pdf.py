import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from Loader import ParameterLoaderPDF,LoaderPDF,ResultLoder

def Test1_LoaderPDF():
    sl=LoaderPDF()

    param=ParameterLoaderPDF( pathfile="test/data/blabla.pdf")
    
    res = sl.load(param)
    
    # if isinstance(res, ResultLoder):
    #     res:ResultLoder
    #     print(res.src_type)
    #     print(res.src_data)

    if isinstance(res, ResultLoder):
        res:ResultLoder
        alldata=""
        for item in res.src_data:
            if item.page_content:
                alldata+=item.page_content

        print(alldata)


def Test2_LoaderPDF_to_documents():
    sl=LoaderPDF()

    param=ParameterLoaderPDF( pathfile="test/data/blabla2.pdf")
    
    res = sl.load(param)

    res2=ResultLoder(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':
    Test1_LoaderPDF()       
    Test2_LoaderPDF_to_documents() 

