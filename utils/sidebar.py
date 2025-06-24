import streamlit as st

def sidebar_info():
    st.sidebar.header("Image / Video")
    source = st.sidebar.selectbox(
        label="Choose a source",
        options=["Image", "Video"]
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
    st.sidebar.title("YOLOv8 Config")
    model_size = st.sidebar.radio(
        label="Model size",
        options=["nano", "small", "medium"]
    )
    model_dict = {
        'nano': 'yolov8n.pt',
        'small': 'yolov8s.pt',
        'medium': 'yolov8m.pt'
    }
    
    use_gpu = st.sidebar.checkbox("USE GPU Acceleration")
    device = "cuda" if use_gpu else "cpu"
    st.sidebar.write(f"Selected: {model_size}, GPU: {use_gpu}")
    st.session_state['model_size'] = model_size
    st.session_state['model_name'] = model_dict[model_size]
    st.session_state['use_gpu'] = use_gpu
    st.session_state['device'] = device
    # st.sidebar.json(st.session_state)

def img_upload():
    img = st.sidebar.file_uploader(label="Upload an image", type=["png", "jpg", "jpeg", "BMP", "WEBP"])
    return img

def video_upload():
    video = st.sidebar.file_uploader(label="Upload a video", type=["mp4", "mov", "avi", "mkv"])
    return video