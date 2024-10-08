from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

# INDEX_PATH = './index'

def create_or_load_index(documents):
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

    qdrant_client = QdrantClient(host="localhost", port=6333)
    
    vector_store = QdrantVectorStore(client=qdrant_client, collection_name="your_collection_name")
    
    index = VectorStoreIndex.from_documents(
        documents,
        vector_store=vector_store,
        embed_model=embed_model
    )

    
    return index