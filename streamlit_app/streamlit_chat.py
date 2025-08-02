#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 10 17:33:48 2025

@author: matheoeymar
"""
import streamlit as st
import time
import google.generativeai as genai
from streamlit_extras.stylable_container import stylable_container
from translations import translations

st.set_page_config(layout="wide")

key="" #use your own

if "explications" not in st.session_state:
    st.session_state.explications = []

if "prompts" not in st.session_state:
    st.session_state.prompts = []

def stream_data(sentence):
    for word in sentence.split(" "):
        yield word + " "
        time.sleep(0.1)
        
user ="user.png"
ai="google-gemini-icon.png"

with st.sidebar:
    language = st.selectbox("Select Language", ["English 🇺🇸", "French 🇫🇷"])
    st.divider()
    t = translations[language]
    add_text=st.write(t['welcome'])
    if (key!=""):
        add_badge=st.badge(t['key_provided'], icon=":material/check:", color="green")
    else:
        add_badge=st.badge(t["key_not_provided"], icon=":material/close:", color="red")
        st.write(f":red[{t['key_error']}]")
    st.divider()

    if st.button(t['reset']):
        st.session_state.prompts = []
        st.session_state.explications = []
    
    st.write(f"### {t['history']} ")
    for prompt in st.session_state.prompts:
        st.write(f"- {prompt}")

st.title(t['title'])
st.logo(
    "Google_Gemini_logo.svg.png",
    size="large"
)
             
col1, col2 = st.columns([1,1])  

genai.configure(api_key=key)
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

with col1:
    st.write(t['message'])
    
messages = st.container(height=380)

with col2:
    with stylable_container(
        key=t['button'],
        css_styles="""
        button{
            float: right;
        }
        """
    ):
        st.write("\n")
        if st.button(t['button'], disabled=len(st.session_state.explications)<10):
            response = model.generate_content(t['explications'].format(len=len(st.session_state.explications),explications=st.session_state.explications))
            messages.chat_message("assistant",avatar=ai).write_stream(stream_data(t['explications_message']))
            messages.chat_message("assistant",avatar=ai).write_stream(stream_data(response.text))

if prompt := st.chat_input(t['bar']):
    messages.chat_message("user",avatar=user).write_stream(stream_data(prompt))
    st.session_state.prompts.append(prompt)
    response = model.generate_content(t['evaluation'].format(prompt=prompt))
    pred_gemini=int(response.text[0])
    explication=response.text
    commentary = explication.strip("01\n")
    st.session_state.explications.append(commentary)
    if (pred_gemini==1):
        messages.chat_message("assistant",avatar=ai).write_stream(stream_data(t['positive']))
    else:
        messages.chat_message("assistant",avatar=ai).write_stream(stream_data(t['negative']))
    messages.chat_message("assistant",avatar=ai).write_stream(stream_data(commentary))

    
    