from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import os

load_dotenv()

client = InferenceClient(
    token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

embedding = client.feature_extraction(
    "LangChain is a framework for building applications with LLMs.",
      model="google/embeddinggemma-300m",
)

print(embedding)
print(type(embedding))
print(embedding.shape)