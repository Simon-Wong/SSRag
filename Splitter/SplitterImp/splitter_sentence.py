from ..SplitterBase import BaseSplitter, BaseResultSplitter, ResultSplitter, BaseParameterSplitter
from Loader import BaseResultLoader,ResultLoader
from utility import doc_langchain_to_llamaindex_batch,LlamaIndexDocument

from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.callbacks.base import CallbackManager
from llama_index.core import Settings
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama


from typing import Any, List, Optional, Union, Callable

class ParameterSplitterSentence(BaseParameterSplitter):
    '''一个句子分割器参数基类'''
    separator: str=" "
    chunk_size: int=1024
    chunk_overlap: int=20
    tokenizer: Optional[Callable]=None
    paragraph_separator: str="\n\n\n"
    chunking_tokenizer_fn: Optional[Callable[[str], List[str]]]=None
    secondary_chunking_regex: Optional[str]="[^,.;。？！]+[,.;。？！]?|[,.;。？！]"
    callback_manager: Optional[CallbackManager]=None
    include_metadata: bool=True
    include_prev_next_rel: bool=True
    id_func: Optional[Callable]=None
    kwargs: dict = {}

    def __init__(self,
                separator: str=" ",
                chunk_size: int=1024,
                chunk_overlap: int=20,
                tokenizer: Optional[Callable]=None,
                paragraph_separator: str="\n\n\n",
                chunking_tokenizer_fn: Optional[Callable[[str], List[str]]]=None,
                secondary_chunking_regex: Optional[str]="[^,.;。？！]+[,.;。？！]?|[,.;。？！]",
                callback_manager: Optional[CallbackManager]=None,
                include_metadata: bool=True,
                include_prev_next_rel: bool=True,
                id_func: Optional[Callable]=None,
                **kwargs):

        self.kwargs = kwargs

class SplitterSentence(BaseSplitter):
    '''一个字符文本分割器'''
    param: ParameterSplitterSentence = None
    splitter: SentenceSplitter = None

    def __init__(self, param: BaseParameterSplitter):
        if not isinstance(param, ParameterSplitterSentence):
            raise ValueError("param must be a ParameterSplitterSentence")
        param:ParameterSplitterSentence
        self.splitter = SentenceSplitter(param.separator,
                                            param.chunk_size,
                                            param.chunk_overlap,
                                            param.tokenizer,
                                            param.paragraph_separator,
                                            param.chunking_tokenizer_fn,
                                            param.secondary_chunking_regex,
                                            param.callback_manager,
                                            param.include_metadata,
                                            param.include_prev_next_rel,
                                            param.id_func)

    def load(self,param: BaseResultLoader, **kwarg)->BaseResultSplitter:
        '''加载数据并返回结果器'''

        docs=doc_langchain_to_llamaindex_batch(param.to_documents())
        nodes=self.splitter.get_nodes_from_documents(docs)
        # for i,node in enumerate(nodes):
        #     print(f"\n--- 第 {i} 个句子块 ---")
        #     print(f"内容:\n{node.text}")
        #     print(f"metadata: {node.metadata}")
        #     print(f"ref_doc_id: {node.ref_doc_id}")
        #     print(f"id: {node.id_}")
        #     print("-" * 50)

        return ResultSplitter(nodes)

        #这里需要把BaseNode转成langchain的Document
        # all_doc=[]
        # for i,node in enumerate(nodes):
        #     all_doc.append( Document(page_content=node.text,
        #                             metadata=node.metadata,
        #                             id=i,
        #                             id_=node.id_))
        