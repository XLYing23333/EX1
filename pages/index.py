import streamlit as st
from utils.sidebar import sidebar_info, sidebar_config, img_upload, video_upload, session_state_init
from utils.path import Path
from utils.YOLO import check_model, predict_img, check_device
from PIL import Image
import tempfile
import cv2
import os


def main():    
    
    st.title("Welcome to the YOLO Page")
    if 'inited' not in st.session_state:
        session_state_init()
        st.session_state['inited'] = True
    sidebar_info()
    
    if st.session_state['source'] == "Image":
        
        upload_img = None
        res_plot = None
        detect_boxes = None
        
        upload_img = img_upload()

        if upload_img is not None:
        
            if st.sidebar.button('Detect Image Objects'):
                uploaded_image = Image.open(upload_img)
                device = check_device(st.session_state['device'])
                model = check_model(st.session_state['model_name'])
                if model:
                    res = predict_img(model, uploaded_image, st.session_state['confidence'], device)
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
        else:
            st.write("Please upload an image file.")
    elif st.session_state['source'] == "Video":
        source_vid = None
        source_vid = video_upload()
        stframe = st.empty()
        info_output = st.empty()

        if source_vid is not None:
            video_bytes = source_vid.read()    
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_file:
                temp_file.write(video_bytes)
                temp_video_path = temp_file.name
            if video_bytes:
                st.write('### Raw Video')
                st.video(video_bytes)
    
            

            if st.sidebar.button('Detect Video Objects'):
                if st.sidebar.button("STOP"):
                    try: os.remove(temp_video_path)
                    except: pass
                    try: cap.release()
                    except: pass
                    st.rerun()
                device = check_device(st.session_state['device'])
                model = check_model(st.session_state['model_name'])
                
                # cap = cv2.VideoCapture(temp_video_path)
                cap = cv2.VideoCapture(0)
                
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    res = predict_img(model, frame, st.session_state['confidence'], device)
                    stframe.image(res['res_plotted'], channels="RGB", caption='Detected Objects')
                    with info_output.expander("Detection Results"):
                        for box in res['boxes']:
                            st.write(box.xywh)
                cap.release()
                os.remove(temp_video_path)
        else:
            st.write("Please upload a video file.")
    
    sidebar_config()
        
if __name__ == '__main__':
    main()


