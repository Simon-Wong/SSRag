from ..SrcLoaderBase import BaseParameterSrcLoder, BaseSrcLoader, BaseResultSrcLoder,ResultSrcLoder

from pathlib import Path
from typing import Callable, Dict,Literal,Any


class ParameterSrcLoderJSON(BaseParameterSrcLoder):
    '''
    一个JSON加载器参数
    封装了JSONLoader的参数，用于加载JSON文件
    '''

    #公共参数
    #using_loader，指定使用的加载器，默认JSONLoader
    #kwargs，其他参数，用于传递给加载器的构造函数
    using_loader:Literal["JSONLoader","fake_no_impl"]="JSONLoader"
    kwargs: Any = None

    #JSONLoader的专属参数
    # jq_schema: str='tostring'
    # content_key: str|None = None
    # is_content_key_jq_parsable: bool|None = False
    # metadata_func: Callable[[Dict, Dict], Dict]|None = None
    # text_content: bool = True
    # json_lines: bool = False
    
    #JSONLoader参数
    #... 

    # 其他参数
    #.......

    def __init__(   self, 
                    pathfile: str|Path,
                    using_loader:Literal["JSONLoader","fake"]="JSONLoader",
                    **kwargs):
        super().__init__(pathfile)
        self.using_loader=using_loader
        self.kwargs=kwargs

class SrcLoaderJSON(BaseSrcLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,src_param: BaseParameterSrcLoder, **kwarg)->BaseResultSrcLoder:
        if isinstance(src_param, ParameterSrcLoderJSON):
            src_param:ParameterSrcLoderJSON
            
            if src_param.using_loader=="JSONLoader":

                from langchain_community.document_loaders import JSONLoader
                argdict=src_param.kwargs
                loader = JSONLoader(src_param.pathfile,
                                jq_schema=argdict.get("jq_schema","tostring"),
                                content_key=argdict.get("content_key"), 
                                is_content_key_jq_parsable=argdict.get("is_content_key_jq_parsable",False),
                                metadata_func=argdict.get("metadata_func"),
                                text_content=argdict.get("text_content",True),
                                json_lines=argdict.get("json_lines",False))

            elif src_param.using_loader=="fake_no_impl":
                raise ValueError(f"the value of using_loader {src_param.using_loader}  is not implemented")

            return ResultSrcLoder(loader.load())
            
        else:
            raise ValueError("src_param must be a ParameterSrcLoderJSON")
