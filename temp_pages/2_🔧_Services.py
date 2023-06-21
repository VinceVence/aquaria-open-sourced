import streamlit as st
import json
from streamlit_extras.colored_header import colored_header
import model_loader
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path
file_path = "json/metadata.json"

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# define services
services = [    {
                    'name': 'Fish Vision', 
                    'description': 'Computer Vision', 
                    'link':"Fish_Vision", 
                    'image': 'https://img.freepik.com/free-vector/drawn-delicious-sardine-illustration_23-2149003710.jpg?w=740&t=st=1679198780~exp=1679199380~hmac=dbe8a505b1e425f077c42fb30412be97a41c6d31c37f8aad0e62d1407bdaff61'
                },    
                {
                    'name': 'Deep Fish', 
                    'description': 'Computer Vision', 
                    'link': 'Deep_Fish', 
                    'image': 'https://img.freepik.com/free-vector/school-fishes-background-with-deep-sea-flat-style_23-2147800763.jpg?w=740&t=st=1685964166~exp=1685964766~hmac=fdd2b701b5497b2a1d752ddef9576a77dff11d76b9f2b611de85275ec8ec4beb'
                },    
                {
                    'name': 'Marine Debris', 
                    'description': 'Computer Vision', 
                    'link': 'Marine_Debris', 
                    'image': 'https://img.freepik.com/free-vector/fishing-frame-realistic-composition-with-wooden-tabletop-plate-surrounded-by-images-fish-tackle-with-rods-illustration_1284-57077.jpg?size=626&ext=jpg&ga=GA1.1.24532982.1673242717&semt=ais'
                },    
                {
                    'name': 'Marine Garbage', 
                    'description': 'Computer Vision', 
                    'link': 'Marine_Garbage', 
                    'image': 'https://img.freepik.com/free-vector/coronavirus-waste-background_23-2148788230.jpg?w=740&t=st=1679202156~exp=1679202756~hmac=3bfadf975158cc38e471420a4b8741e594a198057c2a8b1c6d823732c49d3a97'
                },    
                {
                    'name': 'Fishing Vessels', 
                    'description': 'Computer Vision', 
                    'link': 'Fishing_Vessels', 
                    'image': 'https://img.freepik.com/free-vector/commercial-fishing-boat-open-sea-loading-net-with-fish-3d-isometric-vector-illustration_1284-77865.jpg?w=360&t=st=1679202191~exp=1679202791~hmac=434702140a62e60d97cb6088c8c8ab10ffa502353a353e0635dd9e76ee384742'
                },   
                {
                    'name': 'Marine Animals', 
                    'description': 'Computer Vision', 
                    'link': 'Marine_Animals', 
                    'image': 'https://img.freepik.com/free-vector/hand-drawn-sea-animals-collection_23-2149238141.jpg?w=360&t=st=1679202535~exp=1679203135~hmac=ac9ac93315a62b9de85ee67180c1b93ef3e1e6d8d63b1b269f967ae54ab8abf1'
                },    
                {
                    'name': 'Fish Tracking', 
                    'description': 'Computer Vision', 
                    'link': 'Fish_Tracking', 
                    'image': 'https://img.freepik.com/free-vector/business-team-rowing-corporate-boat_74855-6917.jpg?w=740&t=st=1680405394~exp=1680405994~hmac=7f8d5b1ba7078af720b4bf0e88acf55851cb053c58322cbd75e5a794a8100b1c'
                },
                {
                    'name': 'Marine Markets', 
                    'description': 'Computer Vision', 
                    'link': 'Marine_Markets', 
                    'image': 'https://img.freepik.com/free-vector/seafood-market-concept_1284-37075.jpg?w=740&t=st=1685964243~exp=1685964843~hmac=4e640e1c7c1e7e2ffdbc35025ba0ce3935f7e5934fc5813c8ca12498d3bfdc87'
                },
                {
                    'name': 'TACO Vision', 
                    'description': 'Computer Vision', 
                    'link': 'TACO', 
                    'image': 'https://img.freepik.com/free-vector/plastic-garbage-ocean-water-surface-pollution_107791-7393.jpg?w=1060&t=st=1683781460~exp=1683782060~hmac=5531759d1404dce525150562130d082d36cdca3253daffb60f66d9d97f8e4543'
                },
                {
                    'name': 'Equalization', 
                    'description': 'Preprocessing', 
                    'link': 'Histogram_Equalization', 
                    'image': 'https://img.freepik.com/free-vector/online-photography-courses-isometric-concept_52683-33743.jpg?w=360&t=st=1683781568~exp=1683782168~hmac=372a858d73d245e90d307b79719d707c7f52fcd1c482ee70f7bf2f2da74e0114'
                },    
                {
                    'name': 'Inquiry Module', 
                    'description': 'Transformers', 
                    'link': 'Inquiry_Module', 
                    'image': 'https://img.freepik.com/free-vector/instruction-manual-smart-man-with-laptop-studying-handbook-reading-guidebook-cartoon-character-use-terms-tutorial-guide-digital-documentation_335657-3536.jpg?w=360&t=st=1679203050~exp=1679203650~hmac=74bc4783e7780bfff578c3b51699e131e888ae9afec1fa8a72a4a2553ef8e361'
                },    
                {
                    'name': 'Synthetica', 
                    'description': 'Data Engineering', 
                    'link': 'Synthetica', 
                    'image': 'https://img.freepik.com/free-vector/add-color-concept-illustration_114360-5494.jpg?w=360&t=st=1679203198~exp=1679203798~hmac=5b47320a297261f3de09361e18af64e038dba8bc24860b990cd48cd91f9f75a6'
                },
                
]

# define the headers
st.markdown("<h1 style='text-align: center; '>🔧SERVICES🔧</h1>",
            unsafe_allow_html=True)
# st.markdown("<h3 style='text-align: center; font-family: Segoe UI;'>Optimize Your Operations with Aquaria's AI-Powered Fisheries and Aquaculture Solutions</h3>", unsafe_allow_html=True)

st.markdown("""
    <h3 style='text-align: center; font-family: Segoe UI; margin-bottom: -0.8em;'>Optimize Your Operations with Aquaria's</h3>
    <h3 style='text-align: center; font-family: Segoe UI; margin-top: -0.8em; margin-bottom: -0.8em;'>AI-Powered Fisheries and</h3>
    <h3 style='text-align: center; font-family: Segoe UI; margin-top: -0.8em;'>Aquaculture Solutions</h3>
""", unsafe_allow_html=True)



st.markdown('<hr>', unsafe_allow_html=True)

if os.path.exists('weights') and os.listdir('weights'):
    st.success('🚀Models Successfully Loaded')
else:
    model_loader.download_weights(
        bucket_name='yolo-models-aquaria', 
        s3_folder='weights/',
        aws_access_key_id=st.secrets['ACCESS_KEY'],
        aws_secret_access_key=st.secrets['SECRET_KEY'],
        local_dir='weights'
    )

# style for the blocks
block_style = """
<style>
    .block {
        display: inline-block;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
        width: 200px;
        height: 250px;
        margin: 10px;
        padding: 10px;
        text-align: center;
        font-size: 20px;
        color: #fff;
        transition: transform 0.2s ease-in-out;
        position: relative;
        overflow: hidden;
    }
    
    .block:before {
        content: "";
        display: block;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(100, 100, 100, 0.7);
        transition: opacity 0.2s ease-in-out;
    }
    
    .block:hover:before {
        opacity: 0;
    }
    
    .block:nth-child(odd):before {
        background-color: rgba(0, 0, 0, 0);
    }

    .row .block:nth-child(even) {
        background-color: rgba(69, 189, 219, 0.73);
    }
    
    .block img {
        display: block;
        margin: 0 auto;
        width: 80%;
        height: 60%;
        object-fit: cover;
        border-radius: 10px;
        margin-top: 5px;
    }
    
    .block h3 {
        margin-top: 10px;
        margin-bottom: 5px;
        font-size: 20px;
    }
    
    .block p {
        font-size: 18px;
        color: black;
        font-family: Poppins;
    }
    
    .block:hover {
        transform: scale(1.08);
        box-shadow: 0px 5px 15px rgba(0,0,0,0.3);
        background-color: rgba(69, 189, 219, 0.16);
        
    }
</style>
"""

# background-color: rgba(69, 189, 219, 0.16);

# display the services in clickable blocks
st.markdown(block_style, unsafe_allow_html=True)

for i in range(len(services)):
    if i % 3 == 0:
        row = ''
    row += f'<a href="{services[i]["link"]}"><div class="block"><img src="{services[i]["image"]}"><h3>{services[i]["name"]}</h3><p>{services[i]["description"]}</p></div></a>'

    if i % 3 == 2 or i == len(services) - 1:
        st.markdown(f'<div class="row">{row}</div>', unsafe_allow_html=True)

st.markdown(f'<hr>', unsafe_allow_html=True)


from font_utils.poppins import make_font_poppins
make_font_poppins()