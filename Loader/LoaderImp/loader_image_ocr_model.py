from ..LoaderBase import BaseParameterLoader, BaseLoader, BaseResultLoder,ResultLoder

import base64
import os
from openai import OpenAI

from langdetect import detect, LangDetectException
from langchain_core.documents import Document


class ParameterLoaderImageOCRModel(BaseParameterLoader):
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

class LoaderImageOCRModel(BaseLoader):
    """
    基于OCR大模型的图片文字识别工具
    自动识别语言，最终返回LangChain Document格式
    """

    def __init__(self):
        self.model:OpenAI = OpenAI(base_url="http://192.168.0.107:11434/v1",api_key="fake_key")

        self.lang_map = {"zh": "ch", 
                        "zh-cn": "ch",  # 简体中文
                        "zh-tw": "ch",  # 繁体中文
                        "en": "en", 
                        "ja": "ja", 
                        "ko": "korean"
                        }

    def _detect_language(self, text: str) -> str:
        """检测文本语言"""
        if not text:
            return "unknown"
        try:
            lang = detect(text)
            return lang
        except LangDetectException:
            return "unknown"

    def load(self,src_param: BaseParameterLoader, **kwarg)->BaseResultLoder:
        """本地多模态大模型提取图片所有文字（通用OCR）"""

        if not isinstance(src_param, ParameterLoaderImageOCRModel):
            raise ValueError("src_param must be a ParameterLoaderImageOCRModel")

        src_param:ParameterLoaderImageOCRModel

        # 读取图片转base64
        with open(src_param.pathfile.as_posix(), "rb") as f:
            base64_image = base64.b64encode(f.read()).decode("utf-8")

        suffix = src_param.pathfile.suffix.lower().strip('.')
        if suffix == 'jpg':
            mime_type = f"image/jpeg"
        else:
            mime_type = f"image/{suffix}"

        i=0
        token_len=src_param.max_tokens 
        while i<src_param.max_retry:
            # 调用本地大模型
            if src_param.use_max_tokens is True:
                response = self.model.chat.completions.create(model="qwen3.5:9b",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": "提取图片中所有可见文字，只输出文字内容，不要任何解释、格式和多余内容"},
                                {"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{base64_image}"}}
                            ]
                        }
                    ],
                    max_tokens=src_param.max_tokens
                )
            else:
                response = self.model.chat.completions.create(model="qwen3.5:9b",
                                messages=[
                                    {
                                        "role": "user",
                                        "content": [
                                            {"type": "text", "text": "提取图片中所有可见文字，只输出文字内容，不要任何解释、格式和多余内容"},
                                            {"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{base64_image}"}}
                                        ]
                                    }
                                ]
                            )
            i+=1
        
            # 直接返回识别文字
            res_text = response.choices[0].message.content.strip()
            if res_text!="":
                break

            finish_reason = response.choices[0].finish_reason
            if finish_reason == "length":
                token_len=int(token_len*1.5)

        # Step 2: 检测文本语言
        detected_lang = self._detect_language(res_text)
        lang=self.lang_map.get(detected_lang, "unknown")

        # Step 4: 返回Document格式结果
        metadata = {
            "source": src_param.pathfile.as_posix(),       
            "language": lang,
            "langdetect": detected_lang,
            "ocr_engine": "qwen3.5:9b",
            "type":"image",
            "image_type":src_param.pathfile.suffix[1:] if src_param.pathfile.suffix else "unknown"
        }

        return ResultLoder([Document(page_content=res_text, metadata=metadata)])
            