import streamlit as st
from classes.image_classifier import ImageClassificationService
from font_utils.poppins import make_font_poppins
from error_handling.error import display_error_503 

# Set page title
st.set_page_config(page_title="🦀Marine Market Classification")

# Add page title
st.markdown("<h1 style='text-align: center; color: #F5EFE6;'>🦀MARINE MARKET CLASSIFICATION</h1>",
            unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #FFFFD0; font-family: Segoe UI;'>Marine Markets Classification using Convolutional Neural Networks</h3>", unsafe_allow_html=True)

st.markdown('<hr>', unsafe_allow_html=True)

st.markdown("""

    <body>


    <h3>📤Upload Your Images Here</h3>
    <p>To get started, you need to upload your images by drag-and-dropping the image in the uploader or clicking browse. After uploading the image, you should be able to see the original image on the left and the predictions on the right.</p>
    
    </body>
    """,unsafe_allow_html=True)

try:
    marine_market_classifier = ImageClassificationService(
    title="Marine Market Classification",
    model_path='weights/marine_market.h5',
    class_labels=['Crabs', 'Lobster', 'Sea Urchins', 'Squid'],
    json_data_path='json/animals_desc.json'
    )

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    predicted_class = marine_market_classifier.classify_image(uploaded_file)
    marine_market_classifier.display_info(predicted_class=predicted_class)
except Exception as e:
    st.info('Model not yet loaded. Please visit the Service page.', icon="ℹ️")
    st.warning(e)
    display_error_503()

make_font_poppins()