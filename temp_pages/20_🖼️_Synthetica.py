# Frontend
import streamlit as st

# Backend
import base64
from pathlib import Path
from colorama import Fore, Style
from PIL import Image
import requests

# System
import os
import subprocess
import shutil

# Set page configs
PAGE_CONFIG = {"page_title": "Synthetica",
               "page_icon": "🧊",
               "layout": "wide",
               "initial_sidebar_state": "auto",
               }
st.set_page_config(**PAGE_CONFIG)


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


# Header
st.markdown("<h1 style='text-align: center; color: #F5EFE6;'>🖼️SYNTHETICA</h1>",
            unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #FFFFD0; font-family: Segoe UI;'>A Website that Generates Synthetic Images using the Cut-Paste Algorithm</h3>", unsafe_allow_html=True)
st.markdown("""---""")

# Foreground File Uploader
st.markdown("<h3 style='text-align: left; color: #FFFFD0; font-family: Segoe UI;'>FOREGROUND IMAGES</h3>",
            unsafe_allow_html=True)
foreground_images = st.file_uploader("",
                                     type=['png'],
                                     accept_multiple_files=True,
                                     key="foreground",
                                     help="Import PNG images",
                                     on_change=None,
                                     disabled=False,
                                     )


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


def img_to_html(img_url):
    response = requests.get(img_url)
    img_bytes = base64.b64encode(response.content).decode()
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid' width=75px>".format(img_bytes)
    return img_html


def make_directories():
    dirs_to_create = [
        'image_composition/datasets/dataset_synthetic/input/foregrounds/supercategory/category',
        'image_composition/datasets/dataset_synthetic/input/backgrounds',
        'image_composition/datasets/dataset_synthetic/output/images'
    ]

    for dir_path in dirs_to_create:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)


def generate_images():
    # The command you want to run
    command = [
        "python3",
        "./image_composition/python/image_composition.py",
        "--input_dir",
        "./image_composition/datasets/dataset_synthetic/input",
        "--output_dir",
        "./image_composition/datasets/dataset_synthetic/output",
        "--count",
        str(num_of_images),
        "--width",
        "512",
        "--height",
        "512",
        "--silent"
    ]

    subprocess.run(command)

def load_image(path):
    return Image.open(path)


def zip_images():
    # Directory containing the files you want to zip
    directory = "./image_composition/datasets/dataset_synthetic/output/images"
    shutil.make_archive('generated_images', 'zip', directory)


def delete_directories():
    # Delete images
    shutil.rmtree(
        './image_composition/datasets/dataset_synthetic/input/foregrounds/supercategory/category')
    shutil.rmtree(
        './image_composition/datasets/dataset_synthetic/input/backgrounds')
    shutil.rmtree('./image_composition/datasets/dataset_synthetic/output/images')


def download_zip_file():
    with open("generated_images.zip", "rb") as fp:
        btn = st.download_button(
            label="Download ZIP",
            data=fp,
            file_name="generated_images.zip",
            mime="application/zip",
        )
    os.remove('generated_images.zip')


@st.cache_data
def save_file(uploaded_files, dir):
    for uploaded_file in uploaded_files:
        with open(os.path.join(dir, uploaded_file.name), "wb") as f:
            f.write(uploaded_file.read())


st.markdown("<p style='text-align: center; color: grey;'>" +
            img_to_html("https://cdn-icons-png.flaticon.com/512/20/20183.png?w=740&t=st=1684911416~exp=1684912016~hmac=2c432892a3d94778a83f2a7bb5e5a6302a54026782d6dcf795bfca539ed6ece5")+"</p>", unsafe_allow_html=True)

# Background File Uploader
st.markdown("<h3 style='text-align: left; color: #FFFFD0; font-family: Segoe UI;'>BACKGROUND IMAGES</h3>",
            unsafe_allow_html=True)
background_images = st.file_uploader("",
                                     type=["png", "jpg", "jpeg"],
                                     accept_multiple_files=True,
                                     key="background",
                                     help="Import JPG, JPEG, PNG images",
                                     on_change=None,
                                     disabled=False,
                                     )

# Slider
num_of_images = st.slider(label= "Number of Images", 
                          min_value=1,
                          max_value=100,
                          value=5)

columns = st.columns((2.5, 1, 2))
generatee_button = columns[1].button('Generate')

if generatee_button:
    if len(foreground_images) == 0:
        st.info('No Foreground images were found! Please include atleast one. ', icon="🚨")
    elif len(background_images) == 0:
        st.info('No Background images were found! Please include atleast one. ')
    else:
        make_directories()
        save_file(foreground_images,
                  "./image_composition/datasets/dataset_synthetic/input/foregrounds/supercategory/category")
        save_file(background_images,
                  "./image_composition/datasets/dataset_synthetic/input/backgrounds")
        generate_images()
        zip_images()
        delete_directories()
        download_zip_file()


st.markdown("""---""")


st.image(load_image("images/TUTS/1.png"))


from font_utils.poppins import make_font_poppins
make_font_poppins()