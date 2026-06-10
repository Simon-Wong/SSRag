from ..SrcLoaderBase import BaseParameterSrcLoder, BaseSrcLoader, BaseResultSrcLoder,ResultSrcLoder

from pathlib import Path
from typing import Dict,Any
from typing import Literal

from bs4 import BeautifulSoup
from langchain_core.documents import Document


class ParameterSrcLoderHTML(BaseParameterSrcLoder):
    '''
    一个html加载器参数
    封装了一些用的到的参数，用于加载html文件
    #公共参数
    pathfile，html文件路径
    open_encoding，文件编码，默认utf-8
    parse_only，指定解析的元素，默认None
    parse_type，指定解析元素的类型，可选值为 id 或 class，默认 id。仅在parse_only不为None时生效
    '''

    open_encoding: str|None = "utf-8",
    parse_only:str|None=None
    parse_type:Literal["id","class"]="id",

    def __init__(   self, 
                    pathfile: str|Path,
                    open_encoding: str|None = "utf-8",
                    parse_only:str|None=None,
                    parse_type:Literal["id","class"]="id"
                    ):
        super().__init__(pathfile=pathfile)

        self.open_encoding=open_encoding
        self.parse_only=parse_only
        self.parse_type=parse_type

class SrcLoaderHTML(BaseSrcLoader):    
    def __init__(self):
        super().__init__()

    def load(self,src_param: BaseParameterSrcLoder, **kwarg)->BaseResultSrcLoder:
        if isinstance(src_param, ParameterSrcLoderHTML):
            src_param:ParameterSrcLoderHTML

            with open(src_param.pathfile.as_posix(), "r", encoding=src_param.open_encoding) as file:
                soup = BeautifulSoup(file, "html.parser")

            if src_param.parse_only is not None:
                if src_param.parse_type=="id":
                    content_div=soup.find("div",id=src_param.parse_only)
                elif src_param.parse_type=="class":
                    content_div=soup.find("div",class_=src_param.parse_only)

                if content_div:
                    content=content_div.get_text()
                else:
                    content="未找到目标内容"
                    print(f"请注意检查HTML中{src_param.parse_type}名称{src_param.parse_only}是否正确")

            else:
                content=soup.get_text()


            metadata = {"source": src_param.pathfile.as_posix(),"type":"html"}
            return ResultSrcLoder([Document(page_content=content, metadata=metadata)])   

        else:
            raise ValueError("src_param must be a ParameterSrcLoderHTML")
