from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor
from llama_index.llms.ollama import Ollama
from llama_index.core import get_response_synthesizer

def setup_chatbot(index):
    llm = Ollama(model="llama3.1:latest", request_timeout=1500.0)
    
    retriever = VectorIndexRetriever(
        index=index,
        similarity_top_k=10,
    )
    
    response_synthesizer = get_response_synthesizer(llm=llm)
    
    query_engine = RetrieverQueryEngine(
        retriever=retriever,
        response_synthesizer=response_synthesizer,
        node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.5)],
    )
    
    return query_engine

def ask_question(query_engine, question, conversation_history):
    # Context contains all previous conversations
    context = "\n".join(conversation_history) + f"\nYou: {question}"

    response = query_engine.query(context)
    
    # Storing the conversations
    conversation_history.append(f"You: {question}")
    conversation_history.append(f"Bot: {response.response} Thank you!")
    
    return response.response + " Thank you!"
