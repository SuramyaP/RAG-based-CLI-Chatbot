# # from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# # from llama_index.core import VectorStoreIndex
# # from llama_index.vector_stores.qdrant import QdrantVectorStore

# def create_index(documents):
#     embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
    
#     vector_store = QdrantVectorStore(collection_name="your_collection_name")
    
#     index = VectorStoreIndex.from_documents(
#         documents,
#         vector_store=vector_store,
#         embed_model=embed_model
#     )
#     return index
# import os
# from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# from llama_index.core import VectorStoreIndex, StorageContext
# from llama_index.vector_stores.qdrant import QdrantVectorStore

# INDEX_PATH = './index'

# def create_or_load_index(documents):
#     embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
#     vector_store = QdrantVectorStore(collection_name="your_collection_name")
#     storage_context = StorageContext.from_defaults(persist_dir=INDEX_PATH)
    
#     if os.path.exists(INDEX_PATH):
#         print("Loading existing index from disk...")
#         index = VectorStoreIndex.load(storage_context=storage_context)
#     else:
#         print("Creating a new index...")
#         index = VectorStoreIndex.from_documents(
#             documents,
#             vector_store=vector_store,
#             embed_model=embed_model,
#             storage_context=storage_context
#         )
#         index.storage_context.persist()
    
#     return index

import os
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

INDEX_PATH = './index'

# def create_or_load_index(documents):
#     embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
    
#     # Initialize the Qdrant client
#     qdrant_client = QdrantClient(host="localhost", port=6333)

#     # client = QdrantClient(
#     #     url="http://localhost:6333",  # Replace with your Qdrant instance URL
#     #     api_key="your_qdrant_api_key"  # Replace with your Qdrant API key if needed
#     # )
    
    
#     vector_store = QdrantVectorStore(
#         client=qdrant_client,
#         collection_name="your_collection_name"
#     )
    
#     storage_context = StorageContext.from_defaults(persist_dir=INDEX_PATH)
    
#     if os.path.exists(INDEX_PATH):
#         print("Loading existing index from disk...")
#         index = VectorStoreIndex.load(storage_context=storage_context)
#     else:
#         print("Creating a new index...")
#         index = VectorStoreIndex.from_documents(
#             documents,
#             vector_store=vector_store,
#             embed_model=embed_model,
#             storage_context=storage_context
#         )
#         index.storage_context.persist()
    
#     return index
# def create_or_load_index(documents):
#     embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
    
#     # Initialize the Qdrant client
#     qdrant_client = QdrantClient(host="localhost", port=6333)
#     # qdrant_client = QdrantClient(
#     #     url="http://localhost:6333",  # Replace with your Qdrant instance URL
#     #     api_key="your_qdrant_api_key"  # Replace with your Qdrant API key if needed
#     # )
    
#     vector_store = QdrantVectorStore(
#         client=qdrant_client,
#         collection_name="your_collection_name"
#     )
    
#     storage_context = StorageContext.from_defaults(persist_dir=INDEX_PATH)
    
#     # Check if the index directory exists and contains the necessary files
#     # if os.path.exists(os.path.join(INDEX_PATH, 'docstore.json')):
#     #     print("Loading existing index from disk...")
#     #     index = VectorStoreIndex.load(storage_context=storage_context)
#     # else:
#     #     print("Creating a new index...")
#     #     index = VectorStoreIndex.from_documents(
#     #         documents,
#     #         vector_store=vector_store,
#     #         embed_model=embed_model,
#     #         storage_context=storage_context
#     #     )
#     #     index.storage_context.persist()
#     if os.path.exists(os.path.join(INDEX_PATH, 'docstore.json')):
#         print("Loading existing index from disk...")
#         index = VectorStoreIndex.load(storage_context=storage_context)
#     else:
#         print("Creating a new index...")
#         index = VectorStoreIndex.from_documents(
#             documents,
#             vector_store=vector_store,
#             embed_model=embed_model,
#             storage_context=storage_context
#         )
#         index.storage_context.persist()
#     return index

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