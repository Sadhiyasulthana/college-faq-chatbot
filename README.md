# College FAQ Domain-Aware Chatbot

## Problem Description
This chatbot answers questions based strictly on provided college rules data. It avoids hallucination and only responds using the given knowledge source.

## Domain Chosen
College Rules & FAQs

## LLM Used
OpenAI GPT model with LangChain

## Data Source
Custom text file stored in data/college_faq.txt

## Retrieval Method
FAISS vector store with OpenAI embeddings (RAG approach)

## Features
- Retrieval-Augmented Generation (RAG)
- Semantic search
- Low temperature for reduced hallucination
- Structured knowledge source

## How to Run
1. Install dependencies:
   pip install -r requirements.txt
2. Add your OpenAI API key in a .env file:
   OPENAI_API_KEY=your_api_key_here
3. Run the app:
   streamlit run app.py

## Sample Questions
- What is the attendance requirement?
- How many books can be borrowed?
- When is the fee deadline?
