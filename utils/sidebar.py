import streamlit as st
import time

def session_state_init():
    st.session_state['model_size'] = 'nano'
    st.session_state['model_name'] = 'yolov8n.pt'
    st.session_state['use_gpu'] = False
    st.session_state['device'] = 'cpu'

def sidebar_info():
    st.sidebar.header("Image / Video")
    source = st.sidebar.selectbox(
        label="Choose a source",
        options=["Image", "Video", "Camera"]
    )
    confidence= float(st.sidebar.slider(
        label="Confidence",
        min_value=25,
        max_value=100,
        value=40,
    )) / 100
    st.session_state['source'] = source
    st.session_state['confidence'] = confidence
    
    
def sidebar_config():
    with st.sidebar.form("config_form"):
        st.title("YOLOv8 Config")
        cols1, cols2 = st.columns(2)
        with cols1:
            model_size = st.radio(
                label="Model size",
                options=["nano", "small", "medium"]
            )
        with cols2:
            model_type = st.radio(
                label="Model type",
                options=["Detect", "Segment", "Classify"]
            )
        model_dict = {
            'nano': 'yolov8n<TYPE>.pt',
            'small': 'yolov8s<TYPE>.pt',
            'medium': 'yolov8m<TYPE>.pt'
        }
        model_type_dict = {
            'Detect': '',
            'Segment': '-seg',
            'Classify': '-cls'
        }
        
        use_gpu = st.checkbox("USE GPU Acceleration")
        device = "cuda" if use_gpu else "cpu"
        
        if st.form_submit_button("Submit"): 
            
            model_type_id = model_type_dict[model_type]
            model_id = model_dict[model_size].replace("<TYPE>", model_type_id)
            
            st.session_state['model_size'] = model_size
            st.session_state['model_name'] = model_id
            st.session_state['use_gpu'] = use_gpu
            st.session_state['device'] = device
            st.success("Submit Success.")
            time.sleep(0.5)
            st.rerun()
        st.json(st.session_state)
    st.sidebar.write(f"Selected: {st.session_state['model_size']}, Device: {st.session_state['device']}")
    
def img_upload():
    img = st.sidebar.file_uploader(label="Upload an image", type=["png", "jpg", "jpeg", "BMP", "WEBP"])
    return img

def video_upload():
    video = st.sidebar.file_uploader(label="Upload a video", type=["mp4", "mov", "avi", "mkv"])
    return video