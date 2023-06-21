import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header
from utils.page_rerouting import move_files
import time

st.markdown("<h1 style='text-align: center; color: #F5EFE6;'>🚣AQUARIA</h1>",
            unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #FFFFD0; font-family: Segoe UI;'>A web-based AI as a Service for Precision Fishing and Aquaculture in the Philippines</h3>", unsafe_allow_html=True)

# st.markdown('<hr>', unsafe_allow_html=True)

HAS_LOGGED_IN = False

def display_image(url):
    st.markdown("<p></p>",unsafe_allow_html=True)
    image_url = url
    st.image(image_url, caption='image: Freepik.com', use_column_width=True)
    st.markdown("<p></p>",unsafe_allow_html=True)

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
            # Move files from temp_pages to pages when password is correct
            move_files('temp_pages', 'pages')
        else:
            st.session_state["password_correct"] = False
            # Move files from pages to temp_pages when password is incorrect
            move_files('pages', 'temp_pages')
            st.session_state["tries"] += 1  # increment tries counter
            if st.session_state["tries"] >= 5:
                st.warning("Timeout for 30 seconds.")
                time.sleep(30)  # pause execution for 30 seconds
                st.session_state["tries"] = 0  # reset tries counter

    if "password_correct" not in st.session_state:
        # First run, initialize tries counter and show input for password.
        st.session_state["tries"] = 0
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        # Move files from pages to temp_pages when password is not yet entered
        move_files('pages', 'temp_pages')
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True



if check_password():

    # Use the function to move files
    move_files('temp_pages', 'pages')

    tab1, tab2, tab3, tab4 = st.tabs(["📖Overview", 
                                    "🤖Artificial Intelligence", 
                                    "🐠Philippine Fisheries", 
                                    "🗺️State of Philippine Technology"])

    with tab1:
        display_image('https://img.freepik.com/free-photo/fishing-boat-port_1339-7111.jpg?w=826&t=st=1684847025~exp=1684847625~hmac=f48dbde381265fb04a93426050f5a69cdf135a01d30b10ffb8360c8cb5898382')

        colored_header(
            label="Overview",
            color_name="blue-green-70",
            description=""
            )

        st.markdown(
            """
            <style>
            .tab {
                text-indent: 50px;  /* adjust as needed */
                text-align: justify;  /* Add this line */
            }
            </style>
            <div class="tab" style="text-align=justify;">Aquaria is a web-based AI as a Service platform that uses cut, paste, and learn image synthesis and computer vision algorithms to optimize precision fishing and aquaculture in the Philippines. The platform aims to help small-scale fisherfolk and aquaculture farmers improve their productivity, sustainability, and profitability by providing them with easy-to-use, affordable, and accurate AI-powered tools.</div>
            <p></p>
            <div class="tab">The core technology behind Aquaria is cut, paste, and learn image synthesis, a state-of-the-art deep learning approach that enables the system to generate high-quality synthetic images of fish and other aquatic organisms. This technology allows the platform to build accurate and comprehensive datasets of fish species, which are essential for training computer vision algorithms. These algorithms, in turn, can identify and classify fish species in real-time, track their movement and behavior, and detect anomalies such as diseases and pollution.</div>
            <p></p>
            <div class="tab">Aquaria's computer vision capabilities are also used to optimize fish farming practices, such as feeding, growth monitoring, and disease prevention. By analyzing real-time data from underwater cameras and sensors, the platform can provide farmers with actionable insights and recommendations on how to improve their operations. For instance, Aquaria can detect when fish are underfed or overfed, when water quality is suboptimal, or when there are signs of stress or illness.</div>
            <p></p>
            <div class="tab">Overall, Aquaria represents a significant advancement in the field of aquaculture and fisheries management. By leveraging AI and computer vision technologies, the platform can help small-scale fisherfolk and farmers increase their yield, reduce their environmental impact, and improve the health and welfare of their fish. Moreover, the platform's web-based and pay-per-use model makes it accessible and affordable to a wide range of users, regardless of their technical expertise or financial resources.</div>
            """
            ,unsafe_allow_html=True)

    with tab2:
        display_image("https://img.freepik.com/free-photo/close-up-scientist-analysing-health-informations-tablet-while-specialist-sport-supervises-exercise-sportsman-monitoring-his-physical-endurance-examining-medical-scan-notepad-laboratory_482257-13199.jpg?w=900&t=st=1685002147~exp=1685002747~hmac=78756010229d16419a1257870e310b12691562bd3a88253c8336ffed63b2ed3f")

        colored_header(
            label="Artificial Intelligence in the Fishing Industry",
            description="",
            color_name="blue-green-70",
            )
        
        st.markdown(
            """
            <style>
            .tab {
                text-indent: 50px;  /* adjust as needed */
            }
            </style>
            <div class="tab" style="text-align=justify>Artificial intelligence (AI) is becoming increasingly important in the fisheries and aquaculture industry. As the global demand for fish and seafood continues to rise, the industry faces numerous challenges, including overfishing, pollution, climate change, and disease outbreaks. AI technologies can help address these challenges by providing new tools and solutions for more efficient, sustainable, and profitable fisheries and aquaculture operations.</div>
            <p></p>
            <div class="tab">One of the most significant applications of AI in fisheries and aquaculture is in monitoring and management. By using AI-powered sensors, cameras, and other devices, operators can gather real-time data on fish populations, water quality, weather conditions, and other relevant variables. This information can then be analyzed using machine learning algorithms to predict trends, identify anomalies, and optimize operations. For example, AI can help identify areas where overfishing is occurring and recommend strategies for reducing fishing pressure in those areas.</div>
            <p></p>
            <div class="tab">Another important use of AI in fisheries and aquaculture is in disease prevention and management. Aquaculture farms are particularly vulnerable to disease outbreaks, which can cause significant economic losses and have serious implications for human health. AI-powered systems can detect early warning signs of disease outbreaks and provide farmers with targeted recommendations for preventive measures. For instance, AI can help farmers identify which fish are most susceptible to particular diseases and recommend appropriate vaccinations or treatments.</div>
            <p></p>
            <div class="tab">AI can also help improve the sustainability and environmental impact of the fisheries and aquaculture industry. By providing more accurate and comprehensive data on fish populations, AI can help operators make better decisions about when and where to fish or harvest. This can reduce the risk of overfishing and enable more sustainable fishing practices. Additionally, AI can help monitor and mitigate the impact of aquaculture on the surrounding ecosystem, by analyzing water quality, nutrient levels, and other environmental variables.</div>
            <p></p>
            <div class="tab">Overall, the use of AI in the fisheries and aquaculture industry represents a significant opportunity for improving sustainability, productivity, and profitability. By leveraging AI technologies, the industry can better monitor and manage fish populations, prevent and manage disease outbreaks, and reduce its environmental impact. As the technology continues to evolve and become more accessible, it is likely that AI will play an increasingly important role in shaping the future of the fisheries and aquaculture industry.</div>
            """,
            unsafe_allow_html=True)

    with tab3:
        display_image("https://img.freepik.com/free-photo/man-is-fishing-with-net_72229-1073.jpg?w=900&t=st=1684849177~exp=1684849777~hmac=159d631fda0ef1bb9005566a2bdc3a99d3b43420cd54fc964f422c5ea79e6ec6")

        colored_header(
            label="Fisheries in the Philippines",
            description="",
            color_name="blue-green-70",
            )
        
        st.markdown(
            """
            <style>
            .tab {
                text-indent: 50px;  /* adjust as needed */
            }
            </style>
            <div class="tab" style="text-align=justify>The Philippines is an archipelagic nation located in Southeast Asia and is considered one of the world's leading fisheries and aquaculture producers. The industry is a significant contributor to the country's economy, providing employment opportunities to millions of Filipinos and supporting livelihoods in rural communities. The Philippines has a rich marine biodiversity and is home to over 2,000 fish species, making it an ideal location for fisheries and aquaculture activities.</div>
            <p></p>
            <div class="tab">The fisheries industry in the Philippines is composed of both commercial and municipal fishery sectors. The commercial sector is dominated by large-scale fishing fleets, while the municipal sector is comprised of small-scale fisherfolk who use traditional fishing methods. The industry produces a wide range of fish and seafood products, including tuna, sardines, milkfish, and shrimp. The Philippines is also a major producer of seaweed and other aquatic plants.</div>
            <p></p>
            <div class="tab">In addition to the fisheries industry, the Philippines has a thriving aquaculture sector. The industry is focused primarily on the production of milkfish, tilapia, and shrimp. The aquaculture sector has undergone significant growth in recent years, driven by increasing demand for fish and seafood products and the need to supplement declining fish stocks from wild capture fisheries. However, the industry also faces several challenges, including disease outbreaks, water pollution, and climate change.</div>
            <p></p>
            <div class="tab">The Philippine government has implemented various policies and programs to support the fisheries and aquaculture industry, including the creation of the Bureau of Fisheries and Aquatic Resources and the establishment of marine protected areas. Additionally, the government has partnered with various international organizations and private sector stakeholders to promote sustainable fisheries and aquaculture practices. While the industry faces several challenges, the Philippines has the potential to become a major player in the global fisheries and aquaculture market with continued investment in technology, innovation, and sustainable practices.</div>
            """,
            unsafe_allow_html=True)

    with tab4:
        display_image("https://img.freepik.com/free-photo/portrait-happy-asian-man-friends-sitting-chair-camp-with-talking-looking-smartphone-cooking-set-front-ground-outdoor-cooking-traveling-camping-lifestyle-concept_1150-61510.jpg?w=900&t=st=1684849634~exp=1684850234~hmac=5e46e38a893e45a40e859d1baf88617e0fd9fc7e9ca4dac9509cc0aec51055a4")

        colored_header(
            label="State of Technology in the Philippines' Fishing Industry",
            description="",
            color_name="blue-green-70",
            )
        
        st.markdown(
            """
            <style>
            .tab {
                text-indent: 50px;  /* adjust as needed */
            }
            </style>
            <div class="tab" style="text-align=justify>The fisheries and aquaculture industry of the Philippines has been evolving and adapting to new technologies and modern innovations. In recent years, there has been an increase in the use of technology in the industry, including artificial intelligence (AI), machine learning, and Internet of Things (IoT) devices. These technologies have been deployed in various applications across the industry to improve efficiency, sustainability, and profitability.</div>
            <p></p>
            <div class="tab">One of the most significant technological advancements in the fisheries and aquaculture industry of the Philippines is the use of IoT devices. These devices are used to monitor water quality, temperature, oxygen levels, and other parameters that affect the health and growth of aquatic organisms. The data collected from these devices is then analyzed using machine learning algorithms to optimize aquaculture operations and improve productivity. Additionally, IoT devices are used to monitor fishing fleets and provide real-time data on fishing activities, which can help reduce illegal fishing and overfishing.</div>
            <p></p>
            <div class="tab">Another technology that is being used in the fisheries and aquaculture industry of the Philippines is AI. AI is being used to monitor fish populations and track their movements, which can help fishermen and aquaculture farmers optimize their operations. AI-powered systems are also used to detect early warning signs of disease outbreaks, providing farmers with targeted recommendations for preventive measures.</div>
            <p></p>
            <div class="tab">The use of mobile apps and cloud-based platforms has also become more prevalent in the fisheries and aquaculture industry of the Philippines. These technologies enable farmers and fishermen to access real-time data on weather conditions, market prices, and other relevant information. This information can be used to make informed decisions about when and where to fish or harvest, improving the efficiency and profitability of the industry.</div>
            <p></p>
            <div class="tab">Overall, the adoption of new technologies and modern innovations is changing the face of the fisheries and aquaculture industry of the Philippines. These technologies are enabling the industry to become more sustainable, efficient, and profitable, while also reducing its impact on the environment. As the industry continues to evolve, it is likely that new technologies will emerge, further revolutionizing the way that fish and seafood products are produced and managed in the Philippines.</div>
            """,
            unsafe_allow_html=True)

from font_utils.poppins import make_font_poppins
make_font_poppins()
