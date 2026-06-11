import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from Loader import ParameterLoaderTxt,LoaderTxt,ResultLoader
from Splitter import SplitterCharTextRecursive,ParameterSplitterCharTextRecursive,ResultSplitter

def Test1_SplitterCharTextRecursive():
    sl=LoaderTxt()

    src_param=ParameterLoaderTxt(pathfile="test/data/blabla.txt")
    
    res = sl.load(src_param)
    
    spliter_param=ParameterSplitterCharTextRecursive(separators=["\n\n", ".", "，", " "],
                                            is_separator_regex=False,
                                            chunk_overlap=100,
                                            chunk_size=1000)
    splitter=SplitterCharTextRecursive(spliter_param)
    res_spliter=splitter.load(res)
    
    print(res_spliter.src_type) 
    print(res_spliter.src_data)

if __name__ =='__main__':
    Test1_SplitterCharTextRecursive()
