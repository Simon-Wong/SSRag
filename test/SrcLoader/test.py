import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from SrcLoader import SrcLoaderTxt

if __name__ =='__main__':
    sl=SrcLoaderTxt()
    sl.load(aaa='blabla')