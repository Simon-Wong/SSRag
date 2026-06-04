from ..SrcLoaderBase import BaseParameterSrc, BaseSrcLoader, BaseResultSrc,ResultSrc

from pathlib import Path
from typing import Callable, Dict


from langchain_community.document_loaders import JSONLoader


class ParameterSrcJSON(BaseParameterSrc):
    '''
    一个JSON加载器参数
    封装了JSONLoader的参数，用于加载JSON文件
    '''
    jq_schema: str
    content_key: str|None = None
    is_content_key_jq_parsable: bool|None = False
    metadata_func: Callable[[Dict, Dict], Dict]|None = None
    text_content: bool = True
    json_lines: bool = False

    def __init__(   self, 
                    pathfile: str|Path,
                    jq_schema: str,
                    content_key: str|None = None,
                    is_content_key_jq_parsable: bool|None = False,
                    metadata_func: Callable[[Dict, Dict], Dict]|None = None,
                    text_content: bool= True,
                    json_lines: bool= False,
                    **kwarg):
        super().__init__(pathfile)

        self.jq_schema=jq_schema
        self.content_key=content_key
        self.is_content_key_jq_parsable=is_content_key_jq_parsable
        self.metadata_func=metadata_func
        self.text_content=text_content
        self.json_lines=json_lines


class SrcLoaderJSON(BaseSrcLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,src_param: BaseParameterSrc, **kwarg)->BaseResultSrc:
        if isinstance(src_param, ParameterSrcJSON):

            loader = JSONLoader(src_param.pathfile,
                                jq_schema=src_param.jq_schema,
                                content_key=src_param.content_key,
                                is_content_key_jq_parsable=src_param.is_content_key_jq_parsable,
                                metadata_func=src_param.metadata_func,
                                text_content=src_param.text_content,
                                json_lines=src_param.json_lines)

            return ResultSrc(loader.load())
            
        else:
            raise ValueError("src_param must be a ParameterSrcJSON")
