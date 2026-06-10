from ..SrcLoaderBase import BaseParameterSrcLoder, BaseSrcLoader, BaseResultSrcLoder,ResultSrcLoder
from .src_loader_image_content import ParameterSrcLoderImageContent,SrcLoaderImageContent


from pathlib import Path
from typing import Any


from langchain_community.document_loaders import UnstructuredMarkdownLoader


class ParameterLoderSrcMD(BaseParameterSrcLoder):
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

class SrcLoaderMD(BaseSrcLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,src_param: BaseParameterSrcLoder, **kwarg)->BaseResultSrcLoder:
        if isinstance(src_param, ParameterLoderSrcMD):
            src_param:ParameterLoderSrcMD
            
            loader = UnstructuredMarkdownLoader(src_param.pathfile,
                                                mode=src_param.mode, 
                                                **src_param.unstructured_kwargs)
            all_documents=loader.load()
    
            if src_param.parse_pic:
                for doc in all_documents:
                    if "image_url" in doc.metadata:
                        pathimg=Path(doc.metadata["image_url"])
                        if  not pathimg.is_absolute():
                            tmp=src_param.pathfile.parent/pathimg
                            pathimg=tmp.resolve().as_posix()
                        else:
                            pathimg=pathimg.as_posix()
                        src_param2=ParameterSrcLoderImageContent(pathfile=pathimg)  
                        sl=SrcLoaderImageContent()
                        res = sl.load(src_param2)    
                        if isinstance(res, ResultSrcLoder):
                            res:ResultSrcLoder
                            print(res.src_data)
                            doc.metadata["image_content"]=res.src_data[0].page_content

            return ResultSrcLoder(all_documents)
            
        else:
            raise ValueError("src_param must be a ParameterLoderSrcMD")
