import os
from langchain_google_genai import ChatGoogleGenerativeAI
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY
)

def clean_document_text(pdf):
    cleaning_prompt = f"""
    Please carefully clean the following document text:
    - Remove any irrelevant data, disclaimers, stray punctuation, fix spacing.
    - Normalize headings to Title Case.
    Keep meaningful content intact. Return only cleaned text.
    Document text:
    {pdf}
    """
    response = llm.invoke(cleaning_prompt)
    return response.content