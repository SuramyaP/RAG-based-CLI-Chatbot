from document_loader import load_documents
from indexing import create_or_load_index
from chatbot import setup_chatbot, ask_question

def chat_with_bot(query_engine):
    print("Welcome to the CLI Chatbot! Type 'exit' to end the conversation.\n")
    
    conversation_history = []
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Bot: Goodbye! Talk to you again :)")
            break
        
        response = ask_question(query_engine, user_input, conversation_history)
        print(f"Bot: {response}\n")

def main():
    # Load documents
    documents = load_documents('./documents')
    
    # Create or load index
    index = create_or_load_index(documents)
    
    # Setup chatbot
    query_engine = setup_chatbot(index)
    
    # Start chat interface
    chat_with_bot(query_engine)

if __name__ == "__main__":
    main()
