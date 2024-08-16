from llama_index.core.schema import TextNode

class Noder:
    def __init__(self) -> None:
        pass
    def build_nodes(self, documents, doc_idxs, text_chunks):
        nodes = []
        for idx, text_chunk in enumerate(text_chunks):
            node = TextNode(
                text=text_chunk,
            )
            src_doc = documents[doc_idxs[idx]]
            node.metadata = src_doc.metadata
            nodes.append(node)
        return nodes