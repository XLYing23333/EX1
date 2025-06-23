import streamlit as st

st.set_page_config(page_title='Streamlit YOLO', page_icon="🎯")

index_page = st.Page(r'./pages/index.py', title='🛠️ Index')
about_page = st.Page(r'./pages/about.py', title='ℹ️ About')

pg = st.navigation([
    index_page,
    about_page
    
])
pg.run()

    
