import streamlit as st
from utils.sidebar import sidebar_info, sidebar_config, img_upload, video_upload, session_state_init
from scripts.CVMode import mode_img, mode_video, mode_camera


def main():    
    
    st.title("Welcome to the YOLO Page")
    if 'inited' not in st.session_state:
        session_state_init()
        st.session_state['inited'] = True
    sidebar_info()
    
    if st.session_state['source'] == "Image":
        mode_img()
    elif st.session_state['source'] == "Video":
        mode_video()
    elif st.session_state['source'] == "Camera":
        mode_camera()
        
    sidebar_config()
        
if __name__ == '__main__':
    main()


