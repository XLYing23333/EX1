import streamlit as st


def main():
    st.title("Welcome to the Index Page")
    st.write("This is the main page of your Streamlit app.")
    
    # Add more content or functionality as needed
    st.button("Click Me", on_click=lambda: st.write("Button clicked!"))
    
if __name__ == '__main__':
    main()