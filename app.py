import streamlit as st 
import numpy as np 
import cv2
import random 

file_uploader=st.file_uploader("Choose an image")  

options = ["Translation", "Rotation", "Scaling", "Shearing","Cropping", "Brightness"] 
selection = st.pills("Select the options for Image Augmentation", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")

if file_uploader is not None:
    file_bytes = np.frombuffer(file_uploader.read(), np.uint8)
    img = cv2.imdecode(file_bytes, 1) # 1 is for color image 
    #st.image(img,  caption="Original Image", channels="BGR")
    a=img.shape
    row,col = img.shape[0:2]
    st.write(a,row,col)



st.write(selection)
for i in selection:
    st.write(i)
    if i == "Translation": 
        tx, ty=np.random.randint(-60,60), np.random.randint(-60,60) 
        st.write(f"Tx: {tx}, Ty={ty}")
        tm=np.array([[1,0,tx],[0,1,ty]],dtype=np.float32) 
        trans_img=cv2.warpAffine(img, tm, dsize=(col,row)) 
        st.image([img, trans_img] , caption=["Original Image", "Translation Image"],  channels="BGR") 

    elif i == "Rotation": 
        center=(col//2, row//2)
        angle=np.random.randint(-360,360) 
        st.write(f"Center:{center}, Angle:{angle}")
        rm=cv2.getRotationMatrix2D(center, angle, 1 )
        rotat_img=cv2.warpAffine(img, rm, dsize=(col,row))
        st.image(rotat_img , caption="Rotation Image", )

