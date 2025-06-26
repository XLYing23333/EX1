import streamlit as st
from dotenv import load_dotenv
import os
import torch
from utils.YOLO import check_model
import numpy as np

load_dotenv()
init_img = np.random.randint(0, 255, size=(10, 10, 3), dtype=np.uint8)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
check_model('yolov8n.pt').predict(init_img, device=device)
print(device)

# Set page title and icon

st.set_page_config(page_title='Streamlit YOLO', page_icon="🎯")

index_page = st.Page(r'./pages/index.py', title='🎯 YOLO')
about_page = st.Page(r'./pages/about.py', title='📃 About')
# demo_page = st.Page(r'./pages/demo.py', title='🛠️ Demo')

pg = st.navigation([
    index_page,
    about_page,
    # demo_page,
])

pg.run()




