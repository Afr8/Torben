
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI	
import json
from langchain.prompts.chat import (
    ChatPromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate
)
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import NLTKTextSplitter
from langchain.schema.output_parser import StrOutputParser


import PyPDF2

def extract_text_from_pdf(file_path):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    text = ""
    for page_num in range(pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        text += page_obj.extractText()
    pdf_file_obj.close()
    return text

# Usage
text = extract_text_from_pdf('CELEX_32022R2554_DE_TXT.pdf')
print(text)



load_dotenv()
api_key = os.getenv("OA_TOKEN")

llm = ChatOpenAI(api_key=api_key, model="gpt-4-0125-preview")


system_prompt = SystemMessagePromptTemplate.from_template("Du bist ein Helfer der Dokumente logisch in abschnitte unterteillt")


loader = PyPDFLoader("CELEX_32022R2554_DE_TXT.pdf")
pages = loader.load_document()
""" humanprompt = HumanMessagePromptTemplate.from_template("Gebe mir den ersten artikel des Dokuments aus: {document_text}")
chat_promt = ChatPromptTemplate.from_messages([system_prompt, humanprompt])
chain = chat_promt | llm | StrOutputParser()
print(chain.invoke(pages[0])) """