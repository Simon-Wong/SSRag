from ..SplitterBase import BaseSplitter, BaseResultSplitter, ResultSplitter, BaseParameterSplitter
from Loader import BaseResultLoader

from langchain_text_splitters import CharacterTextSplitter


class ParameterSplitterCharText(BaseParameterSplitter):
    '''一个字符文本分割器参数基类'''
    separator: str = "\n\n"
    is_separator_regex: bool = False
    chunk_size: int = 1000
    chunk_overlap: int = 100
    kwargs: dict = {}

    def __init__(self,separator: str = "\n\n",
                    is_separator_regex: bool = False,
                    chunk_size: int = 1000,
                    chunk_overlap: int = 100,
                    **kwargs):
        self.separator = separator
        self.is_separator_regex = is_separator_regex
        self.chunk_overlap = chunk_overlap
        self.chunk_size = chunk_size
        self.kwargs = kwargs

class SplitterCharText(BaseSplitter):
    '''一个字符文本分割器'''
    param: ParameterSplitterCharText = None
    splitter: CharacterTextSplitter = None

    def __init__(self, param: BaseParameterSplitter):
        if not isinstance(param, ParameterSplitterCharText):
            raise ValueError("param must be a ParameterSplitterCharText")
        self.param = param
        self.splitter = CharacterTextSplitter(
                    separator=self.param.separator,
                    is_separator_regex=self.param.is_separator_regex,
                    chunk_overlap=self.param.chunk_overlap,
                    chunk_size=self.param.chunk_size,
                    **self.param.kwargs)

    def load(self,param: BaseResultLoader, **kwarg)->BaseResultSplitter:
        '''加载数据并返回结果器'''
        
        docs=self.splitter.split_documents(param.to_documents())

        return ResultSplitter(docs)
