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
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        if device == 'cpu':
            st.warning("CUDA is not available, using CPU instead.")
        elif device == 'cuda':
            st.success("CUDA is available, using GPU instead.")   
    return device
  
def predict_img(model, uploaded_image, confidence, device: str = 'cpu'):
    # device = check_device(device)
    res = model.predict(uploaded_image, conf=confidence, device=device)
    boxes = res[0].boxes
    res_plotted = res[0].plot()[:, :, ::-1]
    return {
        'boxes': boxes,
        'res_plotted': res_plotted
    }

    