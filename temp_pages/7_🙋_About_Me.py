import streamlit as st
from PIL import Image

def load_image(path):
    return Image.open(path)


st.title("About Me ")
st.write("Hi! I'm Lanz Vincent Vencer!")

st.image(load_image("images/me.jpg"))
st.markdown("""
I am currently an undergraduate student-athlete at Lyceum of the Philippines University - Manila. Throughout my educational journey at LPU, I have taught myself how to code through online courses available on Coursera, Udemy, and YouTube. I have honed my skills in Python Programming, Data Science, Machine Learning, Deep Learning, and Research Writing. I also graduated as one of the scholars of the DOST Project Sparta under the Data Science Pathway. 

As a chess athlete for nearly a decade, I have found it motivating to involve myself in strategic ventures that enable me to think critically and creatively. My chess career has not only helped fund my education through scholarships but also given me the opportunity to represent my school in different sporting events like Palarong Pambansa and NCAA. 

My aspiration is to become an Artificial Intelligence (AI) Engineer someday and develop algorithms that would contribute to advancements in Computer Vision, Natural Language Processing, and MLOps.
"""
, unsafe_allow_html=True)

from font_utils.poppins import make_font_poppins
make_font_poppins()