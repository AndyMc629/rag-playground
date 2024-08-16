from pathlib import Path
from llama_index.readers.file import PyMuPDFReader
from typing import List

class Loader:
    def __init__(self, file_type='pdf') -> None:
        if file_type=='pdf':
            self.loader = PyMuPDFReader()
        else:
            pass
        
    def load_docs(self, docs: List[str]):
        docs = self.loader.load(file_path="./data/llama2.pdf") #TODO: files from config
        return docs
        
