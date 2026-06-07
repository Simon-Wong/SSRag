import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from SrcLoader import ParameterSrcHTML,SrcLoaderHTML,BaseResultSrc,ResultSrc

def Test1_SrcLoaderHTML():
    sl=SrcLoaderHTML()

    src_param=ParameterSrcHTML(pathfile="test/data/html_1/blabla.html",parse_only="cnblogs_post_body")
    
    res = sl.load(src_param)
    
    if isinstance(res, ResultSrc):
        res:ResultSrc
        print(res.src_type)
        print(res.src_data)

def Test2_SrcLoaderHTML_to_documents():
    sl = SrcLoaderHTML()

    src_param = ParameterSrcHTML(  pathfile="test/data/html_2/blabla.html",
                                   parse_only="cnblogs_post_body")
    
    res = sl.load(src_param)

    res2 = ResultSrc(res.to_documents())
    print(res2.src_type)
    print(res2.src_data)

def Test3_SrcLoaderHTML():
    sl = SrcLoaderHTML()

    src_param = ParameterSrcHTML(  pathfile="test/data/html_1/blabla.html")
    
    res = sl.load(src_param)
    
    if isinstance(res, ResultSrc):
        res:ResultSrc
        print(res.src_type)
        print(res.src_data)

if __name__ =='__main__':
    Test1_SrcLoaderHTML()    
    Test2_SrcLoaderHTML_to_documents() 
    Test3_SrcLoaderHTML()
