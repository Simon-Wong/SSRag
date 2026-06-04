import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from SrcLoader import ParameterSrcTxt,SrcLoaderTxt

def Test1():
    sl=SrcLoaderTxt()

    src_param=ParameterSrcTxt(pathfile="test/data/blabla.txt")
    
    docs = sl.load(src_param)
    print(docs)

if __name__ =='__main__':
    Test1()
