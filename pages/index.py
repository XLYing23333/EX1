import streamlit as st


def main():
    st.title("Welcome to the Index Page")
    st.write("This is the main page of your Streamlit app.")
    

    if st.button("Click Me"):
        st.balloons()
    
if __name__ == '__main__':
    main()