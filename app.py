# import streamlit as st 

# file_uploader=st.file_uploader("Choose an image") 

# options = ["Shifting (Translation)", "Rotation", "Scaling", "Shearing","Cropping", "Brightness"] 
# selection = st.pills("Select the options for Image Augmentation", options, selection_mode="multi")
# st.markdown(f"Your selected options: {selection}.") 


# if selection == "Shifting (Translation)": 
#     img=cv2.imread(file_uploader)        
#     img=cv2.resize(img,(500,600)) 
#     tx=50  
#     ty=60 
#     tm=np.array([[1,0,tx],[0,1,ty]],dtype=np.float32) 
#     trans_img=cv2.warpAffine(img, tm, dsize=(500,600) ) 
#     st.image([img, trans_img] , captions=["Original Image", "Translation Image"],channels="BGR")
    
import streamlit as st
import cv2
import numpy as np

# Upload image
file_uploader = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# Image augmentation options
options = ["Shifting (Translation)", "Rotation", "Scaling", "Shearing", "Cropping", "Brightness"]
selection = st.pills("Select the options for Image Augmentation", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")

# Shifting (Translation)
if "Shifting (Translation)" in selection and file_uploader is not None:
    # Read image from uploaded file using NumPy + OpenCV
    file_bytes = np.frombuffer(file_uploader.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Resize for consistency
    img = cv2.resize(img, (500, 600))

    # Translation matrix
    tx, ty = 50, 60
    tm = np.array([[1, 0, tx], [0, 1, ty]], dtype=np.float32)
    trans_img = cv2.warpAffine(img, tm, dsize=(500, 600))

    # Show both images using Streamlit
    st.image([img, trans_img], caption=["Original Image", "Translated Image"], channels="BGR")
