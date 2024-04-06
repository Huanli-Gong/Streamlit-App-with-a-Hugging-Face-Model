import streamlit as st
from transformers import pipeline, set_seed

st.title("Inference API: openai-gpt")
text_input = st.text_area("Text Generation:", value="Hello, I'm a language model,")
generator = pipeline('text-generation', model='openai-gpt')
set_seed(42)

if st.button("Generate"):
    if text_input:
        for output in generator(text_input, max_length=30,num_return_sequences=5):
            st.write(output)
    else:
        st.warning("Please enter text first.")

