from llama_index.core.node_parser import SentenceSplitter
from typing import Tuple, List

class DocumentSplitter:
    def __init__(self) -> None:
        self.text_parser = SentenceSplitter(chunk_size=1204) #TODO: make this config driven
   
    def chunk_data(self, documents) -> Tuple[List, List]: #TODO: what type is documents? add hint?
        text_chunks = []
        # maintain relationship with source doc index, to help inject doc metadata in (3)
        doc_idxs = []
        for doc_idx, doc in enumerate(documents):
            cur_text_chunks = self.text_parser.split_text(doc.text)
            text_chunks.extend(cur_text_chunks)
            doc_idxs.extend([doc_idx] * len(cur_text_chunks))
        return doc_idxs, text_chunks
    
    