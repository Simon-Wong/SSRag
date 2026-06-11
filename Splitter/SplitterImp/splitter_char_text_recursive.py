from ..SplitterBase import BaseSplitter, BaseResultSplitter, ResultSplitter, BaseParameterSplitter
from Loader import BaseResultLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from typing import Literal

class ParameterSplitterCharTextRecursive(BaseParameterSplitter):
    '''一个字符文本分割器参数基类'''
    separators: list[str] | None = None #["\n\n", ".", "，", " "]
    keep_separator: bool | Literal['start', 'end'] = True
    is_separator_regex: bool = False
    chunk_size: int = 1000
    chunk_overlap: int = 100
    kwargs: dict = {}

    def __init__(self,separators: list[str] | None = None,
                    keep_separator: bool | Literal['start', 'end'] = True,
                    is_separator_regex: bool = False,
                    chunk_size: int = 1000,
                    chunk_overlap: int = 100,
                    **kwargs):
        self.separators = separators
        self.keep_separator = keep_separator
        self.is_separator_regex = is_separator_regex
        self.chunk_overlap = chunk_overlap
        self.chunk_size = chunk_size
        self.kwargs = kwargs

class SplitterCharTextRecursive(BaseSplitter):
    '''一个字符文本分割器'''
    param: ParameterSplitterCharTextRecursive = None
    splitter: RecursiveCharacterTextSplitter = None

    def __init__(self, param: BaseParameterSplitter):
        if not isinstance(param, ParameterSplitterCharTextRecursive):
            raise ValueError("param must be a ParameterSplitterCharTextRecursive")
        self.param = param
        if param.kwargs.get('language') is not None:
             raise ValueError("parameter language is not supported")

        self.splitter = RecursiveCharacterTextSplitter(
                separators=self.param.separators,
                keep_separator=self.param.keep_separator,
                is_separator_regex=self.param.is_separator_regex,
                chunk_overlap=self.param.chunk_overlap,
                chunk_size=self.param.chunk_size,
                **self.param.kwargs)

    def load(self,param: BaseResultLoader|str, **kwarg)->BaseResultSplitter:
        '''加载数据并返回结果器'''
        
        docs=self.splitter.split_documents(param.to_documents())

        return ResultSplitter(docs)
