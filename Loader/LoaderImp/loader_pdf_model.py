from ..LoaderBase import BaseParameterLoader, BaseLoader, BaseResultLoder,ResultLoder

from pdf2image import convert_from_path

import base64
import os
from openai import OpenAI

from langchain_core.documents import Document


class ParameterLoaderPDFModel(BaseParameterLoader):
    """
    PDF文字识别工具的参数
    """
    def __init__(self, pathfile: str,
                 temp_dir: str|None=None,
                 max_retry: int = 3,
                 use_max_tokens: bool = False,
                 max_tokens: int = 2048,
                 **kwargs):
        super().__init__(pathfile)
        self.temp_dir=temp_dir
        self.max_retry=max_retry
        self.use_max_tokens=use_max_tokens
        self.max_tokens=max_tokens
        self.kwargs=kwargs

class LoaderPDFModel(BaseLoader):
    """
    基于大模型的PDF内容提取工具
    自动识别语言，最终返回LangChain Document格式
    """

    def __init__(self):
        self.model:OpenAI = OpenAI(base_url="http://192.168.0.107:11434/v1",api_key="fake_key")

    def convert_pdf_to_pic(self,param: ParameterLoaderPDFModel)->list[str]:
        """
        将PDF转换为图片格式，返回图片路径列表
        """
        temp_dir=param.temp_dir
        if temp_dir is None:
            temp_dir = os.path.dirname(param.pathfile) or '.'
        os.makedirs(temp_dir, exist_ok=True)

        images = convert_from_path(param.pathfile.as_posix())
        image_paths = []
        for i, image in enumerate(images):
            image_path = os.path.join(temp_dir, f'page_{i+1}.jpg')
            image.save(image_path, 'JPEG')
            image_paths.append(image_path)

        return image_paths

    def load(self,param: BaseParameterLoader, **kwarg)->BaseResultLoder:
        """本地多模态大模型提取PDF内容"""

        if not isinstance(param, ParameterLoaderPDFModel):
            raise ValueError("param must be a ParameterLoaderPDFModel")

        param:ParameterLoaderPDFModel
        image_paths:list[str]=[]
        all_documents=[]

        try:
            # 转换PDF为图片
            image_paths = self.convert_pdf_to_pic(param)  

            # 读取图片转base64
            for pageid,image_path in enumerate(image_paths):
                with open(image_path, "rb") as f:
                    base64_image = base64.b64encode(f.read()).decode("utf-8")
                print(f"{pageid}/{len(image_paths)}")
                res_text=""
                # 调用本地大模型
                ntry=0
                token_len=param.max_tokens
                while ntry<param.max_retry:
                    if param.use_max_tokens is False:
                        response = self.model.chat.completions.create(model="qwen3.5:9b",
                                        messages=[
                                            {
                                                "role": "user",
                                                "content": [
                                                    {"type": "text", "text": "请详细描述这张PPT幻灯片的内容，包括标题、正文和图片内容。"},
                                                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                                                ]
                                            }
                                        ]
                                    )
                    else:
                        response = self.model.chat.completions.create(model="qwen3.5:9b",
                                        messages=[
                                            {
                                                "role": "user",
                                                "content": [
                                                    {"type": "text", "text": "请详细描述这张PPT幻灯片的内容，包括标题、正文和图片内容。"},
                                                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                                                ]
                                            }
                                        ],
                                        max_tokens=token_len
                                    )
                    ntry+=1

                    finish_reason = response.choices[0].finish_reason
                    if finish_reason == "length":
                        token_len=int(token_len*1.5)
                    else:
                        # 直接返回识别结果
                        res_text = response.choices[0].message.content.strip()
                        if res_text!="":
                            break
                    print(f"\t{ntry}/{param.max_retry}")    
                metadata = {
                    "source": param.pathfile.as_posix(),       
                    "ocr_engine": "qwen3.5:9b",
                    "page": pageid+1,
                    }       
                all_documents.append(Document(page_content=res_text, metadata=metadata))
                
        except Exception as e:
            raise ValueError(f"转换PDF为图片失败: {e}")
        finally:
            # 清理临时目录下的图片文件
            for image_path in image_paths:
                try:
                    if os.path.exists(image_path):
                        os.remove(image_path)
                except Exception:
                    pass
        
        return ResultLoder(all_documents)



            