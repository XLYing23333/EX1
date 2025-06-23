import streamlit as st
from utils.sidebar import sidebar
from ultralytics import YOLO
from utils.path import Path
import os

# Set page title and icon

st.set_page_config(page_title='Streamlit YOLO', page_icon="🎯")

index_page = st.Page(r'./pages/index.py', title='🎯 YOLO')
about_page = st.Page(r'./pages/about.py', title='📃 About')
demo_page = st.Page(r'./pages/demo.py', title='🛠️ Demo')

pg = st.navigation([
    index_page,
    about_page,
    demo_page,
])

pg.run()

sidebar()

path = Path()
model_path = os.path.join(path.MODELS, "yolov8n.pt")  
try:
    model = YOLO(model_path)
    st.success("模型加载成功！")    
except Exception as ex:
    st.error(f" 无法加载模型，请检查路径: {model_path}")
    st.error(f"错误详情: {str(ex)}")
