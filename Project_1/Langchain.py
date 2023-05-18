import os 

import streamlit as st
from langchain import HuggingFaceHub, PromptTemplate, LLMChain

api_key = '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'
os.environ['HUGGINGFACEHUB_API_TOKEN'] = api_key

repo_id = 'gpt2'
llm = HuggingFaceHub(repo_id=repo_id)

template = '''Question: {question}

Answer: Think step by step'''

prompt = PromptTemplate(template=template, input_variables=['question'])
llm_chain = LLMChain(prompt=prompt, llm=llm)

st.title('Youtube GPT Creator')
user_prompt = st.text_input('Your input here please....')

if prompt:
    response = llm_chain.run(user_prompt)
    st.write(response)

