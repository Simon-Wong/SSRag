from ..SrcLoaderBase import BaseParameterSrc, BaseSrcLoader, BaseResultSrc,ResultSrc

import base64
import os
from openai import OpenAI

from langdetect import detect, LangDetectException
from langchain_core.documents import Document


class ParameterSrcImageContent(BaseParameterSrc):
    """
    图片文字识别工具的参数
    """
    def __init__(self, pathfile: str,
                 max_retry: int = 3,
                 use_max_tokens: bool = True,
                 max_tokens: int = 1024,
                 **kwargs):
        super().__init__(pathfile)
        self.max_retry=max_retry
        self.use_max_tokens=use_max_tokens
        self.max_tokens=max_tokens
        self.kwargs=kwargs

class SrcLoaderImageContent(BaseSrcLoader):
    """
    基于大模型的图片内容提取工具
    自动识别语言，最终返回LangChain Document格式
    """

    def __init__(self):
        self.model:OpenAI = OpenAI(base_url="http://192.168.0.107:11434/v1",api_key="fake_key")

    def load(self,src_param: BaseParameterSrc, **kwarg)->BaseResultSrc:
        """本地多模态大模型提取图片内容"""

        if not isinstance(src_param, ParameterSrcImageContent):
            raise ValueError("src_param must be a ParameterSrcImageContent")

        src_param:ParameterSrcImageContent

        # 读取图片转base64
        with open(src_param.pathfile.as_posix(), "rb") as f:
            base64_image = base64.b64encode(f.read()).decode("utf-8")

        suffix = src_param.pathfile.suffix.lower().strip('.')
        if suffix == 'jpg':
            mime_type = f"image/jpeg"
        else:
            mime_type = f"image/{suffix}"

        # 调用本地大模型
        i=0
        token_len=src_param.max_tokens 
        while i<src_param.max_retry:
            if src_param.use_max_tokens is True:
                response = self.model.chat.completions.create(model="qwen3.5:9b",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": "理解图片内容，然后输出图片内容的文字描述，不要任何格式和多余内容"},
                                {"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{base64_image}"}}
                            ]
                        }
                    ],
                    max_tokens=token_len
                )
            else:
                response = self.model.chat.completions.create(model="qwen3.5:9b",
                                messages=[
                                    {
                                        "role": "user",
                                        "content": [
                                            {"type": "text", "text": "理解图片内容，然后输出图片内容的文字描述，不要任何格式和多余内容"},
                                            {"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{base64_image}"}}
                                        ]
                                    }
                                ]
                            )
            i+=1

            # 直接返回识别结果
            res_text = response.choices[0].message.content.strip()
            if res_text!="":
                break

            finish_reason = response.choices[0].finish_reason
            if finish_reason == "length":
                token_len=int(token_len*1.5)
        
        metadata = {
            "source": src_param.pathfile.as_posix(),       
            "ocr_engine": "qwen3.5:9b",
            "type":"image",
            "image_type":suffix if suffix else "unknown"
        }

        return ResultSrc([Document(page_content=res_text, metadata=metadata)])
            