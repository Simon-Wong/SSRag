from ..LoaderBase import BaseParameterLoader, BaseLoader, BaseResultLoder,ResultLoder

from pathlib import Path
from typing import Callable, Dict,Literal,Any
import bs4

class ParameterLoaderURL(BaseParameterLoader):
    '''
    一个网页加载器参数
    封装了一些用的到的参数，用于加载网页文件
    #公共参数
    web_urls，网页URL列表
    using_loader，指定使用的加载器，默认UnstructuredURLLoader
    kwargs，其他参数，用于传递给加载器的构造函数

    #UnstructuredURLLoader的专用参数,延迟到load方法中处理
    continue_on_failure，是否继续加载失败的URL，默认True
    mode，加载模式，默认single
    show_progress，是否显示进度条，默认True

    #WebBaseLoader的专用参数，延迟到load方法中处理
    parse_only，指定解析的元素,默认None  
    bs_kwargs，WebBaseLoader的参数，默认None
    requests_kwargs，WebBaseLoader的参数，默认None
    '''

    web_urls: list[str]|str=None
    using_loader:Literal["UnstructuredURLLoader","WebBaseLoader"]="UnstructuredURLLoader"
    kwargs: Any = None

    parse_only:str|None=None
    bs_kwargs: Dict[str, Any]|None =None
    requests_kwargs: Dict[str, Any]|None=None

    def __init__(   self, 
                    web_urls: list[str]|str,
                    using_loader:Literal["UnstructuredURLLoader","WebBaseLoader"]="UnstructuredURLLoader", 
                    **kwargs):
        self.pathfile=None
        self.web_urls=web_urls
        self.using_loader=using_loader

        self.kwargs=kwargs

class LoaderURL(BaseLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,param: BaseParameterLoader, **kwarg)->BaseResultLoder:
        if isinstance(param, ParameterLoaderURL):
            param:ParameterLoaderURL
            if param.using_loader=="UnstructuredURLLoader":

                from langchain_community.document_loaders import UnstructuredURLLoader

                argdict=param.kwargs
                loader = UnstructuredURLLoader(urls=param.web_urls,
                                continue_on_failure=argdict.pop("continue_on_failure",True),
                                mode=argdict.pop("mode","single"),
                                show_progress_bar=argdict.pop("show_progress_bar",False),
                                **argdict)

            elif param.using_loader=="WebBaseLoader":
                param:ParameterLoaderURL

                from langchain_community.document_loaders import WebBaseLoader

                argdict=param.kwargs
                parse_only=argdict.pop("parse_only",None)
                bs_kwargs=argdict.pop("bs_kwargs",None)   

                if parse_only is not None:
                    if bs_kwargs is None:
                        bs_kwargs={"parse_only": bs4.SoupStrainer(id=parse_only)}

                requests_kwargs=argdict.pop("requests_kwargs",{"headers": {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}})
                
                loader = WebBaseLoader( web_paths=param.web_urls,
                                        bs_kwargs=bs_kwargs,
                                        requests_kwargs=requests_kwargs,
                                        **argdict)
            
            return ResultLoder(loader.load())
            
        else:
            raise ValueError("param must be a ParameterLoaderURL")
