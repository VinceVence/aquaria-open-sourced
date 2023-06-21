from classes.yolo_service import YOLOService
import streamlit as st
from error_handling.error import display_error_503 

# Set page title
st.set_page_config(page_title="🌮TACO")

#################### FRONTEND ########################

st.markdown("<h1 style='text-align: center; '>🌮TRASH ANNOTATIONS IN CONTEXT (TACO)</h1>",
            unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; font-family: Segoe UI;'>TACO Object Detection using YOLOv8</h3>", unsafe_allow_html=True)
st.markdown('<hr>', unsafe_allow_html=True)


st.markdown("""

    <body>


    <h3>📤Upload Your Images Here</h3>
    <p>To get started, you need to upload your images by drag-and-dropping the image in the uploader or clicking browse. After uploading the image, you should be able to see the original image on the left and the predictions on the right.</p>
    
    </body>
    """,unsafe_allow_html=True)


try:
    # Instantiate the YOLOService with required resize dimensions
    taco_detector = YOLOService("weights/taco.pt", resize=(416, 416))
    # Add a file uploader widget
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # If an image is uploaded, display it on the page
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded image", use_column_width=True)
        detect_image = taco_detector.detect(uploaded_file)
        st.image(detect_image, caption="Detected image", use_column_width=True)
except Exception as e:
    st.info('Model not yet loaded. Please visit the Service page.', icon="ℹ️")
    display_error_503()


from font_utils.poppins import make_font_poppins
make_font_poppins()
