from abc import ABC, abstractmethod
from pathlib import Path
from langchain_core.documents import Document
from unstructured.documents.elements import Element 


class BaseParameterLoader:
    '''
    一个资源参数基类
    参数都是一次性的，在一个load函数里使用过了，就不要再传给其他函数使用。
    '''
    pathfile: str|Path # 资源文件路径

    def __init__(self, pathfile: str|Path):
        self.pathfile = Path(pathfile).resolve()
        

class BaseResultLoader(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def to_documents(self,filter:callable=None)->list[Document]:
        '''
        将资源数据转换为文档列表，根据filter函数过滤元素，默认返回所有元素
        filter函数的参数为src_data中的元素，返回值为bool，True表示保留该元素，False表示过滤该元素
        '''    
        pass

class ResultLoader(BaseResultLoader):
    '''一个资源结果基类'''
    src_data: list[Document]|list[Element] = None # 资源文档列表
    src_type: str = None # 资源类型
    def __init__(self, data: list[Document]|list[Element]):
        assert isinstance(data, list), "data must be a list"
        self.src_data = data
        self.src_type = next(elem.__class__.__name__ for elem in data if elem is not None) or 'Unknown'
        #print(self.src_type)

    def to_documents(self,filter:callable=None)->list[Document]:
        '''
        将资源数据转换为文档列表，根据filter函数过滤元素，默认返回所有元素
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
            
            docs = [Document(page_content=elem.text, metadata=elem.metadata.to_dict()) for elem in valid_elements]
            return docs


class BaseLoader(ABC):
    '''一个加载器基类'''
    param: BaseParameterLoader = None # 资源参数
    def __init__(self):
        pass

    @abstractmethod
    def load(self,param: BaseParameterLoader, **kwarg)->BaseResultLoader:
        pass
