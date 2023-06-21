import streamlit as st


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """


def make_font_poppins():
    with open("css/styles.css") as css:
        st.markdown(f'<style>{css.read()}</style>' , unsafe_allow_html= True)

    # Render the custom CSS style
    st.markdown("<link href='https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap' rel='stylesheet'>", unsafe_allow_html=True)

    # Hide Streamlit style
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)