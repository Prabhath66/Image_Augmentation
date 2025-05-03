import streamlit as st 
import numpy as np 
import cv2

file_uploader=st.file_uploader("Choose an image")  

# options = ["Translation", "Rotation", "Scaling", "Shearing","Cropping", "Brightness"] 
# selection = st.pills("Select the options for Image Augmentation", options, selection_mode="multi")
# st.markdown(f"Your selected options: {selection}.")

if file_uploader is not None:
    file_bytes = np.frombuffer(file_uploader.read(), np.uint8)
    img = cv2.imdecode(file_bytes, 1) # 1 is for color image 
    st.image(img,  caption="Original Image", channels="BGR")
    a=img.shape
    row,col = img.shape[0:2]
    st.write(a,row,col)

    
    options = ["Translation", "Rotation", "Scaling", "Shearing","Cropping", "Brightness"] 
    selection = st.pills("Select the options for Image Augmentation", options, selection_mode="multi")
    st.markdown(f"Your selected options: {selection}.")

    st.write(selection)
    if selection == "Translation": 
        tx=150  
        ty=60 
        tm=np.array([[1,0,tx],[0,1,ty]],dtype=np.float32) 
        trans_img=cv2.warpAffine(img, tm, dsize=(col,row) ) 
        a=trans_img.shape
        st.write(a)
        st.image([img, trans_img] , caption=["Original Image", "Translation Image"],  channels="BGR")
    

