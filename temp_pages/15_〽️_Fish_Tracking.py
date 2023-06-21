import streamlit as st
import os
from tracking.obj_det_and_trk_streamlit import *
from error_handling.error import display_error_503 

from font_utils.poppins import make_font_poppins
make_font_poppins()

#--------------------------------Web Page Designing------------------------------
hide_menu_style = """
    <style>
        MainMenu {visibility: hidden;}
        
        
         div[data-testid="stHorizontalBlock"]> div:nth-child(1)
        {  
            border : 2px solid #doe0db;
            border-radius:5px;
            text-align:center;
            color:black;
            background:dodgerblue;
            font-weight:bold;
            padding: 25px;
            
        }
        
        div[data-testid="stHorizontalBlock"]> div:nth-child(2)
        {   
            border : 2px solid #doe0db;
            background:dodgerblue;
            border-radius:5px;
            text-align:center;
            font-weight:bold;
            color:black;
            padding: 25px;
            
        }
    </style>
    """

main_title = """
            <div>
                <h1 style="color:black;
                text-align:center; font-size:35px;
                margin-top:-90px;">
                〽️FISH TRACKING</h1>
            </div>
            """
    
sub_title = """
            <div>
                <h6 style="color:dodgerblue;
                text-align:center;
                margin-top:-40px;">
                Streamlit Basic Dasboard </h6>
            </div>
            """
#--------------------------------------------------------------------------------


#---------------------------Main Function for Execution--------------------------
def main():
    
    st.markdown(hide_menu_style, 
                unsafe_allow_html=True)

    st.markdown(main_title,
                unsafe_allow_html=True)

    st.markdown(sub_title,
                unsafe_allow_html=True)

    inference_msg = st.empty()
    st.title("USER Configuration")
    

    input_source = 'Video'

    conf_thres = st.slider("Class confidence threshold", 0.01, 1.0, 0.25)

 
    save_output_video = st.radio("Save output video?",
                                         ('Yes', 'No'))

    if save_output_video == 'Yes':
        nosave = False
        display_labels=False
   
    else:
        nosave = True
        display_labels = True 
           
    try:
        weights = "weights/best_fish.pt"
        # ------------------------- LOCAL VIDEO ------------------------
        if input_source == "Video":
            
            video = st.file_uploader("Select input video", 
                                            type=["mp4", "avi", "mov"], 
                                            accept_multiple_files=False)
            
            if st.button("Start Tracking"):
                if video is not None:
                    with open(os.path.join(os.getcwd(), video.name), "wb") as f:
                        f.write(video.getbuffer())
                    st.write("Video saved successfully.")
                else:
                    st.write("Please upload a video first.")
                
                stframe = st.empty()
                
                st.markdown("""<h4 style="color:black;">
                                Memory Overall Statistics</h4>""", 
                                unsafe_allow_html=True)
                kpi5, kpi6 = st.columns(2)

                with kpi5:
                    st.markdown("""<h5 style="color:black;">
                                CPU Utilization</h5>""", 
                                unsafe_allow_html=True)
                    kpi5_text = st.markdown("0")
                
                with kpi6:
                    st.markdown("""<h5 style="color:black;">
                                Memory Usage</h5>""", 
                                unsafe_allow_html=True)
                    kpi6_text = st.markdown("0")
                
                detect(weights=weights, 
                    source=video.name,  
                    stframe=stframe, 
                    kpi5_text=kpi5_text,
                    kpi6_text = kpi6_text,
                    conf_thres=float(conf_thres),
                    device="cpu",
                        classes=[0, 1 ,2, 3, 4, 5 ,6 ,7 ,8, 9],nosave=nosave, 
                        display_labels=display_labels)

                inference_msg.success("Inference Complete!")
            
        torch.cuda.empty_cache()
        device="cpu"
        # --------------------------------------------------------------
    except Exception as e:
        st.info('Model not yet loaded. Please visit the Service page.', icon="ℹ️")
        display_error_503()


# --------------------MAIN FUNCTION CODE------------------------
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
# ------------------------------------------------------------------

