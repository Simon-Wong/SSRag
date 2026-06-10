from ..LoaderBase import BaseParameterLoader, BaseLoader, BaseResultLoder,ResultLoder

from pathlib import Path
from typing import IO

from unstructured.partition.ppt import partition_ppt
from langchain_core.documents import Document

class ParameterLoaderPPT(BaseParameterLoader):
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

class LoaderPPT(BaseLoader):
    def __init__(self):
        super().__init__()
    
    def load(self,param: BaseParameterLoader, **kwarg)->BaseResultLoder:
        if isinstance(param, ParameterLoaderPPT):
            param:ParameterLoaderPPT
            all_documents=[]        
            ppt_elements = partition_ppt(param.pathfile, 
                                  file=param.file,
                                  metadata_filename=param.metadata_filename,
                                  metadata_last_modified=param.metadata_last_modified,
                                  **param.kkwarg)

            for id,element in enumerate(ppt_elements):
                
                metadata = {
                        "source": param.pathfile.as_posix(),
                        "id": id,
                        } 

                all_documents.append(Document(page_content=element.text, metadata= metadata))

            return ResultLoder(all_documents) 
        else:
            raise ValueError("param must be a ParameterLoaderPPT")
