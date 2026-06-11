from ..SplitterBase import BaseSplitter, BaseResultSplitter, ResultSplitter, BaseParameterSplitter
from Loader import BaseResultLoader,ResultLoader
from utility import doc_langchain_to_llamaindex_batch,LlamaIndexDocument

from llama_index.core.node_parser import SemanticSplitterNodeParser

from llama_index.core.callbacks.base import CallbackManager
from llama_index.core import Settings
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama


from typing import Any, List, Optional, Union, Callable

class ParameterSplitterSemantic(BaseParameterSplitter):
    '''
    一个语义分割器参数基类
        buffer_size (int): number of sentences to group together when evaluating semantic similarity
        embed_model: (BaseEmbedding): embedding model to use
        sentence_splitter (Optional[Callable]): splits text into sentences
        breakpoint_percentile_threshold (int): dissimilarity threshold for creating semantic breakpoints, lower value will generate more nodes
        include_metadata (bool): whether to include metadata in nodes
        include_prev_next_rel (bool): whether to include prev/next relationships
    '''
    buffer_size:int=1
    embed_model: str = None
    sentence_splitter: Optional[Callable] = None
    breakpoint_percentile_threshold: int = 90
    include_metadata:bool=True  
    include_prev_next_rel:bool =True
    kwargs: dict = {}

    def __init__(self,
                 buffer_size:int=1,
                 embed_model: str = None,
                 sentence_splitter: Optional[Callable] = None,
                 breakpoint_percentile_threshold: int = 90,
                 include_metadata:bool=True,
                 include_prev_next_rel:bool=True,
                **kwargs):
        self.kwargs = kwargs
        self.buffer_size=buffer_size
        self.embed_model=embed_model
        self.sentence_splitter=sentence_splitter
        self.breakpoint_percentile_threshold=breakpoint_percentile_threshold
        self.include_metadata=include_metadata
        self.include_prev_next_rel=include_prev_next_rel

class SplitterSemantic(BaseSplitter):
    '''一个语义分割器'''
    param: ParameterSplitterSemantic = None
    splitter: SemanticSplitterNodeParser = None

    def __init__(self, param: BaseParameterSplitter):
        if not isinstance(param, ParameterSplitterSemantic):
            raise ValueError("param must be a ParameterSplitterSemantic")
        param:ParameterSplitterSemantic=param
        embed_model=None
        if param.embed_model is None:
            embed_model = OllamaEmbedding(model_name="nomic-embed-text",   # 确保与 Ollama 下载的模型名完全一致
                                        base_url="http://192.168.0.107:11434",  # Ollama 服务地址
                                        )
        else:
            embed_model = OllamaEmbedding(model_name=param.embed_model,   # 确保与 Ollama 下载的模型名完全一致
                                        base_url="http://192.168.0.107:11434",  # Ollama 服务地址
                                        )


        # Build splitter kwargs, conditionally adding sentence_splitter if provided
        splitter_kwargs = {
            "buffer_size": param.buffer_size,
            "embed_model": embed_model,
            "breakpoint_percentile_threshold": param.breakpoint_percentile_threshold,
            "include_metadata": param.include_metadata,
            "include_prev_next_rel": param.include_prev_next_rel,
        }
        if param.sentence_splitter is not None:
            splitter_kwargs["sentence_splitter"] = param.sentence_splitter
        splitter_kwargs.update(param.kwargs)
        
        self.splitter = SemanticSplitterNodeParser(**splitter_kwargs)

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
        