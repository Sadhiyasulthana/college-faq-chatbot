import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🎓 College FAQ Chatbot")

# Load FAQ data
with open("data/college_faq.txt", "r", encoding="utf-8") as f:
    context = f.read()

query = st.text_input("Ask a question about college rules:")

if query:
    prompt = f"""
You are a helpful college assistant.
Answer ONLY from the context below.
If the answer is not in the context, say:
"I don't know based on the provided information."

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    answer = response.choices[0].message.content

    st.write("### Answer:")
    st.write(answer)
    
