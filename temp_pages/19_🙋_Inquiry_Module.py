import streamlit as st

st.title('Inquiry Module')

import openai
from classes import gpt_api

gpt_api = gpt_api.OpenAI_API()

question = st.text_input("Enter your queries here:")

text = gpt_api.get_answer(question)
st.write(text)

from font_utils.poppins import make_font_poppins
make_font_poppins()