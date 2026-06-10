from ..SrcLoaderBase import BaseParameterSrcLoder, BaseSrcLoader, BaseResultSrcLoder,ResultSrcLoder

from pathlib import Path
from typing import Dict,Any

from langchain_community.document_loaders import MHTMLLoader
import bs4


class ParameterSrcLoderMHTML(BaseParameterSrcLoder):
    '''
    一个mhtml加载器参数
    封装了一些用的到的参数，用于加载mhtml文件
    #公共参数
    pathfile，mhtml文件路径
    open_encoding，文件编码，默认None
    parse_only，指定解析的元素,默认None  
    bs_kwargs，MHTMLLoader的参数，默认None
    get_text_separator，获取文本时的分隔符，默认空字符串
    '''

    open_encoding: str|None = None,
    parse_only:str|None=None
    bs_kwargs: Dict[str, Any]|None =None
    get_text_separator: str = ""

    def __init__(   self, 
                    pathfile: str|Path,
                    open_encoding: str|None = None,
                    parse_only:str|None=None,
                    bs_kwargs: Dict[str, Any]|None =None,
                    get_text_separator: str = "",
                    ):
        super().__init__(pathfile=pathfile)

        self.open_encoding=open_encoding
        self.parse_only=parse_only
        self.bs_kwargs=bs_kwargs
        self.get_text_separator=get_text_separator

        if parse_only is not None:
            if bs_kwargs is None:
                self.bs_kwargs={"parse_only": bs4.SoupStrainer(id=parse_only)}
    
class SrcLoaderMHTML(BaseSrcLoader):
    def __init__(self):
        super().__init__()

    def load(self,src_param: BaseParameterSrcLoder, **kwarg)->BaseResultSrcLoder:
        if isinstance(src_param, ParameterSrcLoderMHTML):
            src_param:ParameterSrcLoderMHTML


            loader = MHTMLLoader(file_path=src_param.pathfile,
                                open_encoding=src_param.open_encoding,
                                bs_kwargs=src_param.bs_kwargs,
                                get_text_separator=src_param.get_text_separator)

            return ResultSrcLoder(loader.load())
            
        else:
            raise ValueError("src_param must be a ParameterSrcLoderMHTML")
