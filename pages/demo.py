import streamlit as st
import numpy as np
import pandas as pd
from utils.sidebar import sidebar


def static_stable():
    st.write("Here's our first attempt at using data to create a table")
    st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    }))


def dynamic_table():
    dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=[f'column_{i}' for i in range(20)]
    )
    st.dataframe(dataframe.style.highlight_max(axis=0))

def plot():
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
    )
    st.line_chart(chart_data)

def map_demo():
    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
    )
    st.map(map_data)

def widgets():
    # slider
    x = st.slider('x', 0, 100, 50)  
    st.write(x, 'squared is', x * x)
    # text input
    user_name = st.text_input("Your name", key="name")
    st.write("Hello,", user_name)
    st.json(st.session_state)
    # selectbox
    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
        })
    option = st.selectbox(
        'Which number do you like best?',
        df['first column']
    )
    st.write('You selected:', option)

def columns():
    col1, col2 = st.columns(2)
    with col1:
        st.header("Original Image")
        st.image(r"./data/static/img/Small.jpg", caption="Original Image")
    with col2:
        st.header("Detected Image")
        st.image(r"./data/static/img/Small2.jpg", caption="Detected Image")
    left, right = st.columns([1, 2])  
    with left:
        st.button("Generate Random Data")
    with right:
        data = np.random.randn(10, 5)
        st.dataframe(data)

if __name__ == '__main__':
    static_stable()
    dynamic_table()
    plot()
    map_demo()
    st.markdown('------')
    widgets()
    # sidebar()
    columns()
