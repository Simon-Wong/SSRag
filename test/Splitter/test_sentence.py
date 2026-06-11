import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from Loader import ParameterLoaderTxt,LoaderTxt,ResultLoader
from Splitter import SplitterSentence,ParameterSplitterSentence,ResultSplitter

def Test1_SplitterSentence():
    sl=LoaderTxt()

    src_param=ParameterLoaderTxt(pathfile="test/data/xiyouji-01.txt")
    
    res_loader = sl.load(src_param)
    # res:ResultLoader
    # print(res.src_data)
    # print('-'*20)

    spliter_param=ParameterSplitterSentence()
    splitter=SplitterSentence(spliter_param)
    res_spliter=splitter.load(res_loader)

    print(res_spliter.src_type) 
    print('-'*20)
    print(res_spliter.src_data)
    print('-'*20)
    print(res_spliter.to_documents())

if __name__ =='__main__':
    Test1_SplitterSentence()
