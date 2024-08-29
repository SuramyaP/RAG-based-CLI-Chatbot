from llama_index.core import download_loader

def load_documents(directory_path):
    SimpleDirectoryReader = download_loader("SimpleDirectoryReader")
    loader = SimpleDirectoryReader(directory_path, recursive=True, exclude_hidden=True)
    return loader.load_data()