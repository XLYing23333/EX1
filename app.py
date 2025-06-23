import streamlit as st
from utils.sidebar import sidebar

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

    
