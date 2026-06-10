import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from Loader import ParameterLoaderHTML,LoaderHTML,ResultLoader

def Test1_LoaderHTML():
    sl=LoaderHTML()

    param=ParameterLoaderHTML(pathfile="test/data/html_1/blabla.html",parse_only="cnblogs_post_body")
    
    res = sl.load(param)
    
    if isinstance(res, ResultLoader):
        res:ResultLoader
        print(res.src_type)
        print(res.src_data)

def Test2_LoaderHTML_to_documents():
    sl = LoaderHTML()

    param = ParameterLoaderHTML(  pathfile="test/data/html_2/blabla.html",
                                   parse_only="cnblogs_post_body")
    
    res = sl.load(param)

    res2 = ResultLoader(res.to_documents())
    print(res2.src_type)
    print(res2.src_data)

def Test3_LoaderHTML():
    sl = LoaderHTML()

    param = ParameterLoaderHTML(  pathfile="test/data/html_1/blabla.html")
    
    res = sl.load(param)
    
    if isinstance(res, ResultLoader):
        res:ResultLoader
        print(res.src_type)
        print(res.src_data)

if __name__ =='__main__':
    Test1_LoaderHTML()    
    Test2_LoaderHTML_to_documents() 
    Test3_LoaderHTML()
