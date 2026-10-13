from langchain_text_splitters import RecursiveCharacterTextSplitter

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

splitter=RecursiveCharacterTextSplitter(chunk_size=5,chunk_overlap=2)

chunks=splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk)