import streamlit as st
from transformers import pipeline

st.title('Translate Chinese to English')

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")

text_to_translate = st.text_area("Please type input: (Example: 你好，很高兴认识你)", value='', height=250, max_chars=500)

if st.button('Translate'):
    if text_to_translate:
        translation = translator(text_to_translate, max_length=400)[0]['translation_text']
        st.write("Translated result:", translation)
    else:
        st.write("Please enter some text to translate.")
