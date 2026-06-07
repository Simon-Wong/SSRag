import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from SrcLoader import ParameterSrcMHTML,SrcLoaderMHTML,BaseResultSrc,ResultSrc

def Test1_SrcLoaderMHTML():
    sl=SrcLoaderMHTML()

    src_param=ParameterSrcMHTML(pathfile="test/data/blabla.mhtml",parse_only="cnblogs_post_body")
    
    res = sl.load(src_param)
    
    if isinstance(res, ResultSrc):
        res:ResultSrc
        print(res.src_type)
        print(res.src_data)

def Test2_SrcLoaderMHTML_to_documents():
    sl = SrcLoaderMHTML()

    src_param = ParameterSrcMHTML(  pathfile="test/data/blabla.mhtml",
                                parse_only="cnblogs_post_body")
    
    res = sl.load(src_param)

    res2 = ResultSrc(res.to_documents())
    print(res2.src_type)
    print(res2.src_data)


if __name__ =='__main__':
    Test1_SrcLoaderMHTML()    
    Test2_SrcLoaderMHTML_to_documents() 
