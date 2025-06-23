import streamlit as st
from utils.path import Path
import os

def readme():
    path = Path()
    readme_path = os.path.join(path.ROOT, "README.md")
    with open(readme_path, "r", encoding="utf-8") as file:
        md_text = file.read()
    st.markdown(md_text, unsafe_allow_html=True)
    
if __name__ == '__main__':
    readme()