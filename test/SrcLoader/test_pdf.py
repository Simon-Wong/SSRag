import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from SrcLoader import ParameterSrcLoderPDF,SrcLoaderPDF,BaseResultSrcLoder,ResultSrcLoder

def Test1_SrcLoaderPDF():
    sl=SrcLoaderPDF()

    src_param=ParameterSrcLoderPDF( pathfile="test/data/blabla.pdf")
    
    res = sl.load(src_param)
    
    # if isinstance(res, ResultSrcLoder):
    #     res:ResultSrcLoder
    #     print(res.src_type)
    #     print(res.src_data)

    if isinstance(res, ResultSrcLoder):
        res:ResultSrcLoder
        alldata=""
        for item in res.src_data:
            if item.page_content:
                alldata+=item.page_content

        print(alldata)


def Test2_SrcLoaderPDF_to_documents():
    sl=SrcLoaderPDF()

    src_param=ParameterSrcLoderPDF( pathfile="test/data/blabla2.pdf")
    
    res = sl.load(src_param)

    res2=ResultSrcLoder(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':
    Test1_SrcLoaderPDF()       
    Test2_SrcLoaderPDF_to_documents() 

