import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from Loader import ParameterLoaderMHTML,LoaderMHTML,ResultLoader

def Test1_LoaderMHTML():
    sl=LoaderMHTML()

    param=ParameterLoaderMHTML(pathfile="test/data/blabla.mhtml",parse_only="cnblogs_post_body")
    
    res = sl.load(param)
    
    if isinstance(res, ResultLoader):
        res:ResultLoader
        print(res.src_type)
        print(res.src_data)

def Test2_LoaderMHTML_to_documents():
    sl = LoaderMHTML()

    param = ParameterLoaderMHTML(  pathfile="test/data/blabla.mhtml",
                                parse_only="cnblogs_post_body")
    
    res = sl.load(param)

    res2 = ResultLoader(res.to_documents())
    print(res2.src_type)
    print(res2.src_data)


if __name__ =='__main__':
    Test1_LoaderMHTML()    
    Test2_LoaderMHTML_to_documents() 
