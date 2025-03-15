from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

class ParaquetRAG:
    def __init__(self):
        self.embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",model_kwargs={"token":"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"})
        self.load_faiss_index()

    def load_faiss_index(self):
        """Loads the FAISS index from the local storage"""
        self.vector_store = FAISS.load_local("faiss_parquet_index", self.embeddings_model,allow_dangerous_deserialization=True)
        self.retriever = self.vector_store.as_retriever(search_kwargs={"k": 3})
    
    def retrieve(self, query):
        """Retrieves the most relevant SQL context from FAISS based on the query"""
        results = self.retriever.get_relevant_documents(query)
        return results