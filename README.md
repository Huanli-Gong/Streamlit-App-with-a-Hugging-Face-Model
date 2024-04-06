# Week 9 Mini-Project
## Author
Ziyu Shi

## Requirements
- Create a website using Streamlit
- Connect to an open source LLM (Hugging Face)
- Deploy model via Streamlit or other service (accessible via browser)

## App Detail
### Functionaliy
My Streamlit App is able to translate sentences from Chinese into English by connecting to an open source LLM - `transformers`. An example has been provided for testing. After clicking the "translate" button, the translated content will appear under the text window.

### Deployment URL
My Streamlit App is deployed via Streamlit at https://zs148-ids721-week9-btkkfloe3a4qjpqtfgf6mn.streamlit.app/

## Project Steps
### Install necessary packages
Streamlit and transformers are necessary for this app. And the tensorflow and sentencepiece are required for this translation task.
```
sudo pip install streamlit transformers tensorflow sentencepiece
```

### Create streamlit app content
Create a python file to implement the task, here is my translation task:
```python
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
```
To test the app locally, run:
```
sudo streamlit run streamlit_app.py
```
For different tasks with corresponding models, [Hugging face model repository](https://huggingface.co/models) is useful.

### Deployment model via Streamlit
Streamlit needs a `requirements.txt` to initialize the deployment environment. Add all the dependencies into the `requirements.txt`.
Push the local repo onto the GitHub repo. Connect the GitHub repo from Streamlit account and deploy the model.

## Screenshots
### Run locally
![image](/images/runLocally.png)

### Test functionality locally
![image](/images/testLocally.png)

### Deploy via Streamlit
![image](/images/testDeploy.png)

### Error prompts if input is empty
![image](/images/EmptyPrompt.png)