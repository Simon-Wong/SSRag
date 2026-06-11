from langchain_core.documents import Document as LangChainDocument
from llama_index.core.schema import Document as LlamaIndexDocument

def doc_langchain_to_llamaindex(langchain_doc: LangChainDocument,idx:int|str='1') -> LlamaIndexDocument:
    """
    将单个 LangChain Document 转换为 LlamaIndex Document
    
    Args:
        langchain_doc: LangChain 的 Document 对象
        
    Returns:
        LlamaIndex 的 Document 对象
    """
    doc_id=''
    if hasattr(langchain_doc, 'id'):
        if langchain_doc.id:
            doc_id = str(langchain_doc.id)
        else:
            doc_id = str(idx)
    else:
        doc_id = str(idx)
    
    #doc_id = langchain_doc.id if hasattr(langchain_doc, 'id') and langchain_doc.id else idx
    
    return LlamaIndexDocument(text=langchain_doc.page_content,
                                metadata=langchain_doc.metadata,
                                doc_id=doc_id)

from typing import List

def doc_langchain_to_llamaindex_batch(langchain_docs: List[LangChainDocument],format_style:str='',diff_i:int=0) -> List[LlamaIndexDocument]:
    """
    批量将 LangChain Document 列表转换为 LlamaIndex Document 列表
    
    Args:
        langchain_docs: LangChain Document 对象列表
        format_style: 包含"{i}"的格式字符串，默认用于生成doc_id
    Returns:
        LlamaIndex Document 对象列表
    """
    if format_style == '':
        return [doc_langchain_to_llamaindex(doc,i) for i,doc in enumerate(langchain_docs)]

    return [doc_langchain_to_llamaindex(doc,format_style.format(i=i+diff_i)) for i,doc in enumerate(langchain_docs)]


def doc_llamaindex_to_langchain(llamaindex_doc: LlamaIndexDocument) -> LangChainDocument:
    """
    将单个 LlamaIndex Document 转换为 LangChain Document
    
    Args:
        llamaindex_doc: LlamaIndex 的 Document 对象
        
    Returns:
        LangChain 的 Document 对象
    """
    return LangChainDocument(
        page_content=llamaindex_doc.text,
        metadata=llamaindex_doc.metadata,
        id=llamaindex_doc.doc_id
    )

def doc_llamaindex_to_langchain_batch(llamaindex_docs: List[LlamaIndexDocument]) -> List[LangChainDocument]:
    """
    批量将 LlamaIndex Document 列表转换为 LangChain Document 列表
    """
    return [doc_llamaindex_to_langchain(doc) for doc in llamaindex_docs]

