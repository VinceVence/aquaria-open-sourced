# Import necessary modules
import streamlit as st
from classes.yolo_service import YOLOService
from font_utils.poppins import make_font_poppins
from error_handling.error import display_error_503 

# Set page title
st.set_page_config(page_title="🐟Deep Fish")

# Add page title
st.markdown("<h1 style='text-align: center; '>🐟DEEP FISH</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; font-family: Segoe UI;'>Fish Object Detection using YOLOv8</h3>", unsafe_allow_html=True)
st.markdown('<hr>', unsafe_allow_html=True)

# Instruction text
st.markdown("""
    <body>
    <h3>📤Upload Your Images Here</h3>
    <p>To get started, you need to upload your images by drag-and-dropping the image in the uploader or clicking browse. After uploading the image, you should be able to see the original image on the left and the predictions on the right.</p>
    </body>
    """,unsafe_allow_html=True)

try:
    # Instantiate the YOLOService
    deep_fish = YOLOService("weights/deep_fish.pt", resize=(480, 270))
    # Add a file uploader widget
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # If an image is uploaded, display it on the page
    if uploaded_file is not None:
        uploaded_image = st.image(uploaded_file, caption="Uploaded image", use_column_width=True)
        detect_image = deep_fish.detect(uploaded_file)
        detected_image = st.image(detect_image, caption="Predictions", use_column_width=True)
        # Delete the images and references
        del uploaded_file
        del detect_image
        # Explicitly ask the garbage collector to collect any unreferenced objects
        import gc
        gc.collect()
except Exception as e:
    st.info('Model not yet loaded. Please visit the Service page.', icon="ℹ️")
    display_error_503()



# Set font
make_font_poppins()
