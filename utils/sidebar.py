import streamlit as st

def sidebar():
    st.sidebar.header("Image / Video")
    source = st.sidebar.selectbox(
        label="Choose a source",
        options=["Image", "Video"]
    )
    conflidence = st.sidebar.slider(
        label="Confidence",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
    )
    st.sidebar.title("YOLOv8 Config")
    model_size = st.sidebar.radio(
        label="Model size",
        options=["nano", "small", "medium"]
    )
    use_gpu = st.sidebar.checkbox("USE GPU Acceleration")
    st.sidebar.write(f"Selected: {model_size}, GPU: {use_gpu}")

