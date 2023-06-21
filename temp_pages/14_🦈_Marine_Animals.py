import streamlit as st
from classes.image_classifier import ImageClassificationService
from font_utils.poppins import make_font_poppins
from error_handling.error import display_error_503 

# Set page title
st.set_page_config(page_title="Marine Animals Classification")

# Add page title
st.markdown("<h1 style='text-align: center; color: #F5EFE6;'>🦈MARINE CLASSIFICATION</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #FFFFD0; font-family: Segoe UI;'>Marine Animal Classification using Convolutional Neural Networks</h3>", unsafe_allow_html=True)

st.markdown('<hr>', unsafe_allow_html=True)

st.markdown("""

    <body>


    <h3>📤Upload Your Images Here</h3>
    <p>To get started, you need to upload your images by drag-and-dropping the image in the uploader or clicking browse. After uploading the image, you should be able to see the original image on the left and the predictions on the right.</p>
    
    </body>
    """,unsafe_allow_html=True)

# Define the class labels
class_labels = ['Clams', 'Corals', 'Crabs', 'Dolphin', 'Eel', 'Fish', 'Jelly Fish', 'Lobster', 'Nudibranchs', 'Octopus', 'Otter', 'Penguin', 'Puffers', 'Sea Rays', 'Sea Urchins', 'Seahorse', 'Seal', 'Sharks', 'Shrimp', 'Squid', 'Starfish', 'Turtle_Tortoise', 'Whale']

try:
    # Create an object of ImageClassificationService
    marine_classifier = ImageClassificationService(
    title="Marine Animals Classification",
    model_path='weights/animals.h5',
    class_labels=class_labels,
    json_data_path='json/animals_desc.json'
    )

    # Add a file uploader widget
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # If an image is uploaded, classify it
    predicted_class = marine_classifier.classify_image(uploaded_file)
    marine_classifier.display_info(predicted_class=predicted_class)

except Exception as e:
    st.info('Model not yet loaded. Please visit the Service page.', icon="ℹ️")
    display_error_503()

make_font_poppins()
