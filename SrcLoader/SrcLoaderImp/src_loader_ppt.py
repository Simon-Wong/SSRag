from ..SrcLoaderBase import BaseParameterSrc, BaseSrcLoader, BaseResultSrc,ResultSrc

from pathlib import Path
from typing import IO

from unstructured.partition.ppt import partition_ppt
from langchain_core.documents import Document

class ParameterSrcPPT(BaseParameterSrc):
    '''
    一个PPT加载器参数
    封装了partition_ppt参数，用于加载PPT文件
    '''
    file: IO[bytes] | None = None
    metadata_filename: str | None = None
    metadata_last_modified: str | None = None

    def __init__(self, 
                    pathfile: str|Path,
                    file: IO[bytes] | None = None,
                    metadata_filename: str | None = None,
                    metadata_last_modified: str | None = None,
                    **kwarg):
        super().__init__(pathfile)
        self.file=file
        self.metadata_filename=metadata_filename
        self.metadata_last_modified=metadata_last_modified
        self.kkwarg=kwarg

class SrcLoaderPPT(BaseSrcLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,src_param: BaseParameterSrc, **kwarg)->BaseResultSrc:
        if isinstance(src_param, ParameterSrcPPT):
            src_param:ParameterSrcPPT
            all_documents=[]        
            ppt_elements = partition_ppt(src_param.pathfile, 
                                  file=src_param.file,
                                  metadata_filename=src_param.metadata_filename,
                                  metadata_last_modified=src_param.metadata_last_modified,
                                  **src_param.kkwarg)

            for id,element in enumerate(ppt_elements):
                
                metadata = {
                        "source": src_param.pathfile.as_posix(),
                        "id": id,
                        } 

                all_documents.append(Document(page_content=element.text, metadata= metadata))

            return ResultSrc(all_documents) 
        else:
            raise ValueError("src_param must be a ParameterSrcPPT")
