import streamlit as st
import os
from dotenv import load_dotenv
from langchain.text_splitter import characterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

load_dotenv()

st.title("🎓 College FAQ Chatbot")

# Load data
with open("data/college_faq.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split text
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_text(text)

# Create vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(docs, embeddings)

retriever = vectorstore.as_retriever()

llm = ChatOpenAI(temperature=0)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"
)

query = st.text_input("Ask a question about college rules:")

if query:
    response = qa_chain.run(query)
    st.write("### Answer:") 
  st.write(response)
    st.write(response)
