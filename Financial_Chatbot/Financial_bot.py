from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from langchain_core.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers.ensemble import EnsembleRetriever
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import Chroma
import os
app = Flask(__name__)

# Set up your Google API key
os.environ['GOOGLE_API_KEY'] = 'AIzaSyBkw7f0n_lyrxwV-L4JeQjsT5GU2Ks3w3k'

# Load and process the PDF
file_path = "General.pdf"
data_file = PyPDFDirectoryLoader(file_path)
docs = data_file.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# Set up embeddings and retrievers
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = Chroma.from_documents(chunks, embeddings)
vectorstore_retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

keyword_retriever = BM25Retriever.from_documents(chunks)
keyword_retriever.k = 3

ensemble_retriever = EnsembleRetriever(
    retrievers=[vectorstore_retriever, keyword_retriever],
    weights=[0.5, 0.5]
)

# Set up the chat model and prompt
template = """You are an AI assistant that helps people with financial advice. The answer should be descriptive.

CONTEXT: {context} </s>

QUERY: {query} </s>

INSTRUCTIONS: - Use only the information provided in the CONTEXT section to answer the QUERY.
              - Do not provide information or answers outside of the given CONTEXT.
              - Provide only the answer to the query without additional information.
              -provide the answers in proper formatting
ANSWER:
"""
prompt = ChatPromptTemplate.from_template(template)
output_parser = StrOutputParser()

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro-001",
                               max_token="1024",
                               temperature=0.3)

# Create the chain
def create_chain():
    chain = (
        {"context": ensemble_retriever, "query": RunnablePassthrough()}
        | prompt
        | model
        | output_parser
    )
    return chain

bot_chain = create_chain()

def extract_answer(response):
    parts = response.split('ANSWER:')
    if len(parts) > 1:
        return parts[1].strip()
    return response.strip()

@app.route('/')
def home():
    return render_template('chatbot.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.form['query']
    raw_response = bot_chain.invoke(user_query)
    answer = extract_answer(raw_response)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)