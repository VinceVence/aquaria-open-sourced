import streamlit as st
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import cv2
from classes.equalizer import HistogramEqualizer  # import your class

#################### FRONTEND ########################

st.markdown("<h1 style='text-align: center; '>🎴HISTOGRAM EQUALIZATION</h1>",
            unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; font-family: Segoe UI;'>Histogram Equalization for Image Contrast Enhancement</h3>", unsafe_allow_html=True)
st.markdown('<hr>', unsafe_allow_html=True)

st.markdown("""
    <body>
    <h3>📤Upload Your Images Here</h3>
    <p>To get started, you need to upload your images by drag-and-dropping the image in the uploader or clicking browse. After uploading the image, you should be able to see the original image on the left and the predictions on the right.</p>
    </body>
    """,unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img_plt = cv2.imdecode(file_bytes, 1)
    img_plt = cv2.cvtColor(img_plt, cv2.COLOR_BGR2RGB)

    equalizer = HistogramEqualizer(mode='rgb')  # Create an instance of your class
    enhanced_img = equalizer.equalize(img_plt)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    ax1.imshow(img_plt)
    ax1.set_title("Original Image")
    ax1.axis("off")

    ax2.imshow(tf.cast(enhanced_img, tf.uint8).numpy())
    ax2.set_title("Equalized Image")
    ax2.axis("off")

    st.pyplot(fig)

from font_utils.poppins import make_font_poppins
make_font_poppins()
