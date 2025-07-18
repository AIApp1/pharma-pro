import streamlit as st
import openai
import os

# Get your API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Pharma Promo Generator")

product = st.text_input("Product name")
audience = st.text_input("Target audience (e.g. HCPs)")
key_messages = st.text_area("Key messages (bullet points or phrases)")

if st.button("Generate Copy"):
    prompt = f"""
    Write compliant promotional copy for a product named {product}, targeting {audience}.
    Include these key messages: {key_messages}.
    Do not use superlatives or make off-label claims.
    """

  from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ],
    temperature=0.7
)

output = response.choices[0].message.content

    )

    output = response['choices'][0]['message']['content']
    st.text_area("Generated Copy", value=output, height=300)
