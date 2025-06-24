import streamlit as st
from utils.sidebar import sidebar_info, sidebar_config, img_upload
from utils.path import Path
from utils.YOLO import check_model, predict_img
from PIL import Image

def main():
    
    st.title("Welcome to the YOLO Page")
    
    sidebar_info()
    
    if st.session_state['source'] == "Image":
        
        upload_img = None
        res_plot = None
        detect_boxes = None
        
        upload_img = img_upload()

        if st.sidebar.button('Detect Image Objects'):
            uploaded_image = Image.open(upload_img)
            model = check_model(st.session_state['model_name'])
            if model:
                res = predict_img(model, uploaded_image, st.session_state['confidence'])
                # st.json(res)
                detect_boxes = res['boxes']
                res_plot = res['res_plotted']
        
        col1, col2 = st.columns(2)
        with col1:
            if not upload_img:
                st.write('wait to upload objects') 
            else:    
                uploaded_image = Image.open(upload_img)
                st.image(uploaded_image, caption='Uploaded Image')
        with col2:
            if res_plot is None:
                st.write('wait to detect objects')
            else:
                st.image(res_plot, caption='Detected Objects')
        
        if detect_boxes not in [[], {}, ()] and detect_boxes is not None:    
            with st.expander("Detection Results"):
                for box in detect_boxes:
                    st.write(box.xywh)
        else:
            st.write("No target detected in the image.")
            
    elif st.session_state['source'] == "Video":
        st.write("Video source is not supported yet.")
    
    sidebar_config()
        
if __name__ == '__main__':
    main()


