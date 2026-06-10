from Loader import ParameterLoaderTxt,LoaderTxt

if __name__ =='__main__':
    param=ParameterLoaderTxt(pathfile="test/data/blabla.txt")
    sl=LoaderTxt()
    sl.load(param)
