from langchain_community.document_loaders import PyPDFLoader

def load_pdf_text(file_path):
    file_path = r"C:\Users\ch computer\OneDrive\Desktop\project\2501.01305v1.pdf"
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs
  






