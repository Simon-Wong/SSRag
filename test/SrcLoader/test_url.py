import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from SrcLoader import ParameterSrcURL,SrcLoaderURL,BaseResultSrc,ResultSrc

def Test1_SrcLoaderURL():
    sl=SrcLoaderURL()

    src_param=ParameterSrcURL(  web_urls=["https://www.cnblogs.com/wlsandwho/p/18673629","https://www.cnblogs.com/wlsandwho/p/18948512"],
                                using_loader="UnstructuredURLLoader")
    
    res = sl.load(src_param)
    
    if isinstance(res, ResultSrc):
        res:ResultSrc
        print(res.src_type)
        print(res.src_data)

def Test2_SrcLoaderURL_to_documents():
    import os

    # 保存原始 USER_AGENT 环境变量
    original_user_agent = os.environ.get("USER_AGENT")

    try:
        os.environ["USER_AGENT"] = "SSRag/1.0.0"
        sl = SrcLoaderURL()

        src_param = ParameterSrcURL(  web_urls=["https://www.cnblogs.com/wlsandwho/p/18673629","https://www.cnblogs.com/wlsandwho/p/18948512"],
                                    using_loader="WebBaseLoader",
                                    parse_only="cnblogs_post_body")
        
        res = sl.load(src_param)

        res2 = ResultSrc(res.to_documents())
        print(res2.src_type)
        print(res2.src_data)

    finally:
        # 恢复原始 USER_AGENT 环境变量
        if original_user_agent is not None:
            os.environ["USER_AGENT"] = original_user_agent
        else:
            os.environ.pop("USER_AGENT", None)

if __name__ =='__main__':
    Test1_SrcLoaderURL()
    Test2_SrcLoaderURL_to_documents() 
