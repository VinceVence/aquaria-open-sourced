import streamlit as st

def display_error_503():
    st.markdown("<p></p>",unsafe_allow_html=True)
    image_url = "https://img.freepik.com/free-vector/503-error-service-unavailable-concept-illustration_114360-1906.jpg?w=740&t=st=1685416380~exp=1685416980~hmac=f267c60f472c9261f7da543a31b34e48997723e19a6b9ead1289e1467b41e02a"
    st.image(image_url, use_column_width=True)
    st.markdown("<p></p>",unsafe_allow_html=True)