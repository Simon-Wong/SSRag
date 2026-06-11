from Loader import BaseResultLoader

from abc import ABC,abstractmethod

from langchain_core.documents import Document
from unstructured.documents.elements import Element 
from llama_index.core.schema import BaseNode

'''

src----->BaseParameterLoader
            |
            V
            BaseLoader----->BaseResultLoader + BaseParameterSplitter
                                     |
                                     V
                                     BaseSplitter----->BaseResultSplitter

'''

class BaseParameterSplitter(ABC):
    '''一个分割器参数基类'''
    def __init__(self):
        pass


class BaseResultSplitter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def to_documents(self,filter:callable=None)->list[Document]:
        '''
        转换为文档列表，根据filter函数过滤元素，默认返回所有元素
        filter函数的参数为src_data中的元素，返回值为bool，True表示保留该元素，False表示过滤该元素
        '''    
        pass

class ResultSplitter(BaseResultSplitter):
    '''一个分割器结果基类'''
    src_data: list[Document]|list[BaseNode] = None # 资源文档列表
    src_type: str = None # 资源类型
    def __init__(self, data: list[Document]|list[BaseNode]):
        assert isinstance(data, list), "data must be a list"
        self.src_data = data
        self.src_type = next(elem.__class__.__name__ for elem in data if elem is not None) or 'Unknown'
        #print(self.src_type)

    def to_documents(self,filter:callable=None)->list[Document]:
        '''
        转换为文档列表，根据filter函数过滤元素，默认返回所有元素
        filter函数的参数为src_data中的元素，返回值为bool，True表示保留该元素，False表示过滤该元素
        '''        
        if self.src_type == 'Document':
            return self.src_data
        else:
            if filter is None:
                filter = lambda x: True
                
            valid_elements = [elem for elem in self.src_data if filter(elem)]
            if len(valid_elements) == 0:
                return []
            
            docs = [Document(page_content=elem.text, metadata=elem.metadata,id=i,id_=elem.id_) for i,elem in enumerate(valid_elements)]
            return docs


class BaseSplitter(ABC):
    '''一个分割器基类'''
    param: BaseParameterSplitter = None
    
    def __init__(self, param: BaseParameterSplitter):
        self.param = param

    @abstractmethod
    def load(self,param: BaseResultLoader, **kwarg)->BaseResultSplitter:
        pass
