import sys
from pathlib import Path

ROOT_DIR=Path(__file__).parent.parent.parent
#print(ROOT_DIR)
sys.path.append(str(ROOT_DIR))


from utility import doc_langchain_to_llamaindex
from utility import doc_langchain_to_llamaindex_batch
from utility import doc_llamaindex_to_langchain
from utility import doc_llamaindex_to_langchain_batch
from utility import LangChainDocument,LlamaIndexDocument

import unittest
from typing import List

class TestConvertDoc(unittest.TestCase):
    def test_doc_langchain_to_llamaindex_with_id(self):
        """测试单个 LangChain Document 转换为 LlamaIndex Document（带 id）"""
        langchain_doc = LangChainDocument(
            page_content="test content",
            metadata={"source": "test.txt"},
            id="test-id-123"
        )
        
        result = doc_langchain_to_llamaindex(langchain_doc,666)
        
        self.assertIsInstance(result, LlamaIndexDocument)
        self.assertEqual(result.text, "test content")
        self.assertEqual(result.metadata, {"source": "test.txt"})
        self.assertEqual(result.doc_id, "test-id-123")

    def test_doc_langchain_to_llamaindex_without_id(self):
        """测试单个 LangChain Document 转换为 LlamaIndex Document（不带 id）"""
        langchain_doc = LangChainDocument(
            page_content="test content",
            metadata={"source": "test.txt"}
        )
        
        result = doc_langchain_to_llamaindex(langchain_doc)
        
        self.assertIsInstance(result, LlamaIndexDocument)
        self.assertEqual(result.text, "test content")
        self.assertEqual(result.metadata, {"source": "test.txt"})
        self.assertEqual(result.doc_id,"1")

    def test_doc_langchain_to_llamaindex_empty_content(self):
        """测试空内容的 LangChain Document 转换"""
        langchain_doc = LangChainDocument(
            page_content="",
            metadata={}
        )
        
        result = doc_langchain_to_llamaindex(langchain_doc)
        
        self.assertIsInstance(result, LlamaIndexDocument)
        self.assertEqual(result.text, "")
        self.assertEqual(result.metadata, {})

    def test_doc_llamaindex_to_langchain(self):
        """测试单个 LlamaIndex Document 转换为 LangChain Document"""
        llamaindex_doc = LlamaIndexDocument(
            text="test content",
            metadata={"source": "test.txt"},
            doc_id="test-id-456"
        )
        
        result = doc_llamaindex_to_langchain(llamaindex_doc)
        
        self.assertIsInstance(result, LangChainDocument)
        self.assertEqual(result.page_content, "test content")
        self.assertEqual(result.metadata, {"source": "test.txt"})
        self.assertEqual(result.id, "test-id-456")

    def test_doc_llamaindex_to_langchain_empty(self):
        """测试空内容的 LlamaIndex Document 转换"""
        llamaindex_doc = LlamaIndexDocument(
            text="",
            metadata={}
        )
        
        result = doc_llamaindex_to_langchain(llamaindex_doc)
        
        self.assertIsInstance(result, LangChainDocument)
        self.assertEqual(result.page_content, "")
        self.assertEqual(result.metadata, {})

    def test_doc_langchain_to_llamaindex_batch(self):
        """测试批量 LangChain Document 转换为 LlamaIndex Document"""
        langchain_docs = [
            LangChainDocument(page_content="content 1", metadata={"source": "1.txt"}, id="doc-1"),
            LangChainDocument(page_content="content 2", metadata={"source": "2.txt"}, id="doc-2"),
            LangChainDocument(page_content="content 3", metadata={"source": "3.txt"})
        ]
        
        result = doc_langchain_to_llamaindex_batch(langchain_docs,format_style="doc-{i}",diff_i=1)
        
        self.assertEqual(len(result), 3)
        for i, doc in enumerate(result):
            self.assertIsInstance(doc, LlamaIndexDocument)
            self.assertEqual(doc.text, f"content {i+1}")
            self.assertEqual(doc.metadata, {"source": f"{i+1}.txt"})
            expected_id = f"doc-{i+1}" #if i < 2 else None
            self.assertEqual(doc.doc_id, expected_id)

    def test_doc_langchain_to_llamaindex_batch_empty(self):
        """测试空列表的批量转换"""
        result = doc_langchain_to_llamaindex_batch([])
        self.assertEqual(result, [])

    def test_doc_llamaindex_to_langchain_batch(self):
        """测试批量 LlamaIndex Document 转换为 LangChain Document"""
        llamaindex_docs = [
            LlamaIndexDocument(text="content 1", metadata={"source": "1.txt"}, doc_id="doc-1"),
            LlamaIndexDocument(text="content 2", metadata={"source": "2.txt"}, doc_id="doc-2")
        ]
        
        result = doc_llamaindex_to_langchain_batch(llamaindex_docs)
        
        self.assertEqual(len(result), 2)
        for i, doc in enumerate(result):
            self.assertIsInstance(doc, LangChainDocument)
            self.assertEqual(doc.page_content, f"content {i+1}")
            self.assertEqual(doc.metadata, {"source": f"{i+1}.txt"})
            self.assertEqual(doc.id, f"doc-{i+1}")

    def test_doc_llamaindex_to_langchain_batch_empty(self):
        """测试空列表的批量转换"""
        result = doc_llamaindex_to_langchain_batch([])
        self.assertEqual(result, [])

    def test_conversion_roundtrip(self):
        """测试 LangChain -> LlamaIndex -> LangChain 的往返转换"""
        original = LangChainDocument(
            page_content="original content",
            metadata={"key": "value", "number": 42},
            id="roundtrip-id"
        )
        
        converted = doc_langchain_to_llamaindex(original)
        roundtripped = doc_llamaindex_to_langchain(converted)
        
        self.assertEqual(roundtripped.page_content, original.page_content)
        self.assertEqual(roundtripped.metadata, original.metadata)
        self.assertEqual(roundtripped.id, original.id)

    def test_batch_conversion_roundtrip(self):
        """测试批量往返转换"""
        originals = [
            LangChainDocument(page_content="doc 1", metadata={"idx": 1}, id="id-1"),
            LangChainDocument(page_content="doc 2", metadata={"idx": 2}, id="id-2")
        ]
        
        converted = doc_langchain_to_llamaindex_batch(originals)
        roundtripped = doc_llamaindex_to_langchain_batch(converted)
        
        self.assertEqual(len(roundtripped), len(originals))
        for original, roundtripped_doc in zip(originals, roundtripped):
            self.assertEqual(roundtripped_doc.page_content, original.page_content)
            self.assertEqual(roundtripped_doc.metadata, original.metadata)
            self.assertEqual(roundtripped_doc.id, original.id)


if __name__ == "__main__":
    unittest.main()
