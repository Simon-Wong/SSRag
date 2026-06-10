from ..LoaderBase import BaseParameterLoader, BaseLoader, BaseResultLoder,ResultLoder
from .loader_image_content import ParameterLoaderImageContent,LoaderImageContent


from pathlib import Path
from typing import Any


from langchain_community.document_loaders import UnstructuredMarkdownLoader


class ParameterLoaderMD(BaseParameterLoader):
    '''
    一个MD加载器参数
    封装了UnstructuredMarkdownLoader的参数，用于加载MD文件

    parse_pic用于进一步解析md文件中的图片，并添加新的“image_content”元数据
    Document(metadata={'source': '/home/thbytwo/testGit/SSRag/test/data/blabla.md', 
                        'image_url': './blabla.PNG', 
                        'languages': ['eng'], 
                        'file_directory': '/home/thbytwo/testGit/SSRag/test/data', 
                        'filename': 'blabla.md', 
                        'filetype': 'text/markdown', 
                        'last_modified': '2026-06-08T14:37:06', 
                        'category': 'Image', 
                        'element_id': '6a22b45e012c369f61f3ad57325f5a83'}, 
            page_content='吐槽')
            
    '''
    mode: str = "elements"
    unstructured_kwargs: Any = None

    def __init__(self, pathfile: str|Path, mode: str = "elements",parse_pic: bool = False, **kwarg):
        super().__init__(pathfile)
        self.mode=mode
        self.unstructured_kwargs=kwarg
        self.parse_pic=parse_pic

class LoaderMD(BaseLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,param: BaseParameterLoader, **kwarg)->BaseResultLoder:
        if isinstance(param, ParameterLoaderMD):
            param:ParameterLoaderMD
            
            loader = UnstructuredMarkdownLoader(param.pathfile,
                                                mode=param.mode, 
                                                **param.unstructured_kwargs)
            all_documents=loader.load()
    
            if param.parse_pic:
                for doc in all_documents:
                    if "image_url" in doc.metadata:
                        pathimg=Path(doc.metadata["image_url"])
                        if  not pathimg.is_absolute():
                            tmp=param.pathfile.parent/pathimg
                            pathimg=tmp.resolve().as_posix()
                        else:
                            pathimg=pathimg.as_posix()
                        src_param2=ParameterLoaderImageContent(pathfile=pathimg)  
                        sl=LoaderImageContent()
                        res = sl.load(src_param2)    
                        if isinstance(res, ResultLoder):
                            res:ResultLoder
                            print(res.src_data)
                            doc.metadata["image_content"]=res.src_data[0].page_content

            return ResultLoder(all_documents)
            
        else:
            raise ValueError("param must be a ParameterLoaderMD")
