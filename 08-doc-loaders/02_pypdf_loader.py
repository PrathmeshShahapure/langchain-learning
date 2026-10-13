from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader( "08-doc-loaders/data/dl-curriculum.pdf")

doc = loader.load()

print("Number of documents:", len(doc))

print("\nFirst page content:")
print(doc[0].page_content)
print(doc[0].metadata)