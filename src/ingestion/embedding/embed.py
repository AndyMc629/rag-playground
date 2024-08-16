'''
We will use the BGE-small-en embedding model,
we will wrap in a class that returns the model for later use
'''
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.schema import TextNode
from typing import List

class EmbeddingModel:
    def __init__(self) -> None:
        self.embed_model = self._model()
    def _model(self):
        return HuggingFaceEmbedding(model_name="BAAI/bge-small-en") # TODO: replace with config values
    #Note: nodes are of the type 'llama_index.core.schema.TextNode'
    def embed_nodes(self, nodes: List[TextNode]):
        for node in nodes:
            node_embedding = self.embed_model.get_text_embedding(
                node.get_content(metadata_mode="all")
            )
            node.embedding = node_embedding
        return nodes

        