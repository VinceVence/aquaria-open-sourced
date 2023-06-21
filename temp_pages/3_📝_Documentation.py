import streamlit as st

st.title("Documentation")

# Add an explanation for the download button.
st.markdown('### Download User Documentation')
st.markdown('''
             By clicking the button below, you can download a PDF file that contains 
             a detailed user documentation for this application. The PDF will be 
             downloaded to your default download location.
             ''')

# Open the file in binary format. 
with open("files/files.pdf", "rb") as file:
    # Create a download button for the file.
    btn = st.download_button(
        label="Download PDF",  
        data=file,  
        file_name="UserDocumentation.pdf",
        mime="application/pdf" 
    )



from font_utils.poppins import make_font_poppins
make_font_poppins()