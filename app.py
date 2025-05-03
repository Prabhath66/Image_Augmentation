import streamlit as st 
import numpy as np 
import cv2

file_uploader=st.file_uploader("Choose an image") 
if file_uploader is not None:
    file_bytes = np.frombuffer(file_uploader.read(), np.uint8)
    img = cv2.imdecode(file_bytes, 1) # 1 is for color image 
    st.image(img,  caption="Original Image", channels="BGR")
    a=img.shape
    x,y = img.shape[0:2]
    st.write(a,x,y)
# options = ["Shifting (Translation)", "Rotation", "Scaling", "Shearing","Cropping", "Brightness"] 
# selection = st.pills("Select the options for Image Augmentation", options, selection_mode="multi")
# st.markdown(f"Your selected options: {selection}.") 


    #if selection == "Shifting (Translation)": 
    tx=50  
    ty=60 
    tm=np.array([[1,0,tx],[0,1,ty]],dtype=np.float32) 
    trans_img=cv2.warpAffine(img, tm, dsize=(x,y) ) 
    st.image([img, trans_img] , caption=["Original Image", "Translation Image"],  channels="BGR")
    

