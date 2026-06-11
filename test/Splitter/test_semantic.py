import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))

from Loader import ParameterLoaderTxt,LoaderTxt,ResultLoader
from Splitter import SplitterSemantic,ParameterSplitterSemantic,ResultSplitter

def Test1_SplitterSemantic():

    sl=LoaderTxt()

    src_param=ParameterLoaderTxt(pathfile="test/data/hwk-wiki.txt")
    
    res_loader = sl.load(src_param)
    # res:ResultLoader
    # print(res.src_data)
    # print('-'*20)

    spliter_param=ParameterSplitterSemantic()
    splitter=SplitterSemantic(spliter_param)
    res_spliter=splitter.load(res_loader)

    print(res_spliter.src_type) 
    print('-'*20)
    print(res_spliter.src_data)
    print('-'*20)
    print(res_spliter.to_documents())

def Test2_SplitterSemantic():

    #test_semantic.py似乎对xiyouji-02_03.txt西游记这种行文风格的半文言文的理解不够，不能切分出多个。但对hwk-wiki.txt可以。
    sl=LoaderTxt()

    src_param=ParameterLoaderTxt(pathfile="test/data/xiyouji-02_03.txt")
    #src_param=ParameterLoaderTxt(pathfile="test/data/hwk-wiki.txt")
    
    res_loader = sl.load(src_param)
    # res:ResultLoader
    # print(res.src_data)
    # print('-'*20)

    spliter_param=ParameterSplitterSemantic(breakpoint_percentile_threshold=0,buffer_size=10)
    splitter=SplitterSemantic(spliter_param)
    res_spliter=splitter.load(res_loader)

    print(res_spliter.src_type) 
    print('-'*20)
    print(res_spliter.src_data)
    print('-'*20)
    print(res_spliter.to_documents())

    print('='*20)
    docs = res_spliter.to_documents()
    print(f"切分结果: 共 {len(docs)} 个文档")
    print('-'*40)
    for i, doc in enumerate(docs):
        print(f"\n--- 第 {i+1} 个语义块 ---")
        print(f"长度: {len(doc.page_content)} 字符")
        # 显示前200字符作为预览
        preview = doc.page_content[:200] + "..." if len(doc.page_content) > 200 else doc.page_content
        print(f"内容预览:\n{preview}")
        print('-'*40)

if __name__ =='__main__':
    #Test1_SplitterSemantic()
    Test2_SplitterSemantic()
