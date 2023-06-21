import streamlit as st
from PIL import Image

def load_image(path):
    return Image.open(path)

st.title("Aquaria User Guide")
st.text("Welcome to Aquaria, your comprehensive AI-powered marine image analysis tool.")

st.subheader("1. Accessing Aquaria")
st.text("Upon opening the Aquaria link, you will be prompted to enter a password.")
st.text("For this guide, the password is 'admin'. Enter the password and proceed to the Aquaria homepage.")
st.image(load_image('images/1.png'))

st.subheader("2. The Homepage")
st.text("The Aquaria homepage serves as an overview page providing an outline on the state of fisheries, AI, and technology in the Philippines.")
st.image(load_image("images/2.png"))

st.subheader("3. Navigation")
st.text("On the left of the homepage, you will find a sidebar which contains various tabs that lead to the different services provided by Aquaria.")
st.image(load_image("images/3.png"))

st.subheader("4. Accessing Services")
st.text("To access the computer vision services, click on the 'Service' tab. If the model weights for the service you chose are not yet downloaded, Aquaria will automatically download these.")
st.image(load_image("images/4.png"))

st.header("5. Model Download")
st.text("If the weights are already downloaded, you will see the message: '🚀Models Successfully Loaded'.")
st.image(load_image("images/5.png"))

st.subheader("6. Using a Service")
st.text("After the model weights have been downloaded, you can now access and use the services. Select the service you wish to use.")
st.text("For instance, if you select 'Fish Vision Service', you will be directed to the Fish Vision Service page.")
st.image(load_image("images/6.png"))
st.image(load_image("images/7.png"))

st.subheader("7. Uploading an Image")
st.text("On the Fish Vision Service page, you will be prompted to upload a photo. Click on the ‘Browse Files’ button, select your photo, and confirm your selection to upload the image. You may also choose to drag-and-drop your photo.")
st.image(load_image("images/8.png"))

st.subheader("8. Model Processing and Results Display")
st.text("Once the image is successfully uploaded, the computer vision model processes the image in the background and subsequently displays the predicted output to the user.")
st.image(load_image("images/9.png"))
st.image(load_image("images/10.png"))

st.text("You can now use Aquaria to analyze your marine images using our AI-powered computer vision models.")



from font_utils.poppins import make_font_poppins
make_font_poppins()