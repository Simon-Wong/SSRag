import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from SrcLoader import ParameterSrcLoderJSON,SrcLoaderJSON,BaseResultSrcLoder,ResultSrcLoder

def Test1_SrcLoaderJSON():
    sl=SrcLoaderJSON()

    src_param=ParameterSrcLoderJSON( pathfile="test/data/blabla.json",
                                jq_schema='"用户名"+.body.username + ",客户ID:" + .header.client_id + ",时间戳:" + (.header.timestamp | tostring)')
    
    res = sl.load(src_param)
    
    if isinstance(res, ResultSrcLoder):
        res:ResultSrcLoder
        print(res.src_type)
        print(res.src_data)

def Test2_SrcLoaderJSON_to_documents():
    sl=SrcLoaderJSON()

    src_param=ParameterSrcLoderJSON( pathfile="test/data/blabla.json")
    
    res = sl.load(src_param)

    res2=ResultSrcLoder(res.to_documents())
    print(res2.src_type) 
    print(res2.src_data)

if __name__ =='__main__':
    Test1_SrcLoaderJSON()
    Test2_SrcLoaderJSON_to_documents() 
