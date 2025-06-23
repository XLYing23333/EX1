import streamlit as st


col1, col2, col3 = st.columns(3)

with col1:
    st.title("Column 1")
with col2:  
    st.title("Column 2")
with col3:
    st.title("Column 3")
    
