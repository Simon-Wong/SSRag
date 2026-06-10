from ..LoaderBase import BaseParameterLoader, BaseLoader, BaseResultLoder,ResultLoder

from rapidocr_onnxruntime import RapidOCR
from langdetect import detect, LangDetectException
from langchain_core.documents import Document


class ParameterLoaderImageOCR(BaseParameterLoader):
    """
    图片文字识别工具的参数
    """
    def __init__(self, pathfile: str,
                 reocr: bool = False,
                 config_path: str|None = None,
                 lang: str|None = None,
                 **kwargs):
        super().__init__(pathfile)
        
        self.reocr=reocr
        self.config_path=config_path
        self.lang=lang
        self.kwargs=kwargs

        self.need_new_model=False
        if config_path is not None or lang is not None:
            self.need_new_model=True

class LoaderImageOCR(BaseLoader):
    """
    基于RapidOCR的图片文字识别工具
    自动识别语言，最终返回LangChain Document格式
    """

    def __init__(self):
        self.model: RapidOCR = None
        self.lang_map = {"zh": "ch", 
                        "zh-cn": "ch",  # 简体中文
                        "zh-tw": "ch",  # 繁体中文
                        "en": "en", 
                        "ja": "ja", 
                        "ko": "korean"
                        }

    def _ocr_with_model(self,param: ParameterLoaderImageOCR, model: RapidOCR = None) -> str:
        """使用指定模型执行OCR识别"""
        param:ParameterLoaderImageOCR

        if model is None:
            model = self.model
            if model is None or param.need_new_model==True:
                model = RapidOCR(param.config_path,**param.kwargs)
                self.model=model

        result , _ = self.model(param.pathfile.as_posix())

        return "\n".join([item[1] for item in result]) if result else ""

    def _detect_language(self, text: str) -> str:
        """检测文本语言"""
        if not text:
            return "unknown"
        try:
            lang = detect(text)
            return lang
        except LangDetectException:
            return "unknown"

    def load(self,param: BaseParameterLoader, **kwarg)->BaseResultLoder:
        """自动语言适配的完整OCR流程"""

        if not isinstance(param, ParameterLoaderImageOCR):
            raise ValueError("param must be a ParameterLoaderImageOCR")

        param:ParameterLoaderImageOCR

        # Step 1: 先用默认模型（中英文混合）获取初步文本
        res_text = self._ocr_with_model(param)

        # Step 2: 检测文本语言
        detected_lang = self._detect_language(res_text)
        lang=self.lang_map.get(detected_lang, "unknown")
        # Step 3【可选】: 使用最优参数重建模型、重新识别
        if lang != "unknown" and  param.reocr ==True:        
            self.model=RapidOCR(param.config_path,lang=lang,**param.kwargs)
            res_text = self._ocr_with_model(param,self.model)
            
        # Step 4: 返回Document格式结果
        metadata = {
            "source": param.pathfile.as_posix(),       
            "language": lang,
            "langdetect": detected_lang,
            "ocr_engine": "RapidOCR",
            "type":"image",
            "image_type":param.pathfile.suffix[1:] if param.pathfile.suffix else "unknown"
        }

        return ResultLoder([Document(page_content=res_text, metadata=metadata)])
            