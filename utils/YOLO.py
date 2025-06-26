import os
import cv2
import streamlit as st
from utils.path import Path
from ultralytics import YOLO
import torch


def check_model(model_name):
    path = Path()
    model_path = os.path.join(path.MODELS, model_name)  
    try:
        model = YOLO(model_path)
        # st.success("模型加载成功！")    
        return model
    except Exception as ex:
        st.error(f" 无法加载模型，请检查路径: {model_path}")
        st.error(f"错误详情: {str(ex)}")
        return False

def check_device(device):
    if device == 'cuda':
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print(f'CUDA-test-device: {device}')
        if device == 'cpu':
            st.sidebar.warning("CUDA is not available, using CPU instead.")
            print("[INFO] CUDA is not available, using CPU instead.")
        elif device == 'cuda':
            st.sidebar.success("CUDA is available, using GPU instead.")   
            print("[INFO] CUDA is available, using GPU instead.")
    else:
        print("[INFO] Using CPU.")
        st.sidebar.success('Model is running on CPU.')
    return device
  
def predict_img(model, uploaded_image, confidence, device: str = 'cuda'):
    if st.session_state['detect_mode'] == 'Normal':
        res = model.predict(uploaded_image, conf=confidence, device=device)
    elif st.session_state['detect_mode'] == 'Track':
        res = model.track(uploaded_image, conf=confidence, device=device, persist=True)
    boxes = res[0].boxes

    res_plotted = res[0].plot()[:, :, ::-1]
    return {
        'boxes': boxes,
        'res_plotted': res_plotted
    }

    