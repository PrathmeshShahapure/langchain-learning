
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

texts = [
    "Python is a programming language.",
    "Dogs are loyal animals.",
    "Machine learning uses data to make predictions.",
      "Cats are independent pets."
]

metadatas = [
    {"category": "programming"},
    {"category": "animals"},
    {"category": "AI"},
    {"category": "animals"}
]
vector_store=Chroma.from_texts(texts=texts,embedding=embeddings,metadatas=metadatas, collection_name="first_vector_store")

results = vector_store.similarity_search(
    "Dogs are loyal animals",
    k=2
)

for i,doc in enumerate(results):
    print("Content:", doc.page_content)
    print("Metadata:", doc.metadata)