from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader =DirectoryLoader(path="08-doc-loaders/data/pdfs",glob="*.pdf",loader_cls=PyPDFLoader, )

docs=loader.load()

print(len(docs))
print(docs[3].metadata)