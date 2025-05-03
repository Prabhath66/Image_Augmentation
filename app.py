import streamlit as st 
import numpy as np 
import cv2
import random  



file_uploader=st.file_uploader("Choose an image")  

options = ["Translation", "Rotation", "Scaling", "Shearing","Cropping", "Brightness","Grayscale","Flip Horizontally","Flip Vertically"] 
selection = st.sidebar.pills("Select the options for Image Augmentation", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")

if file_uploader is not None:
    file_bytes = np.frombuffer(file_uploader.read(), np.uint8)
    img = cv2.imdecode(file_bytes, 1) # 1 is for color image 
    #st.image(img,  caption="Original Image", channels="BGR")
    a=img.shape
    rows,cols = img.shape[0:2]
    st.write(a,rows,cols)



st.write(selection)
for i in selection:
    st.write(i)
    if i == "Translation": 
        tx, ty=np.random.randint(-60,60), np.random.randint(-60,60) 
        st.write(f"Tx: {tx}, Ty={ty}")
        tm=np.array([[1,0,tx],[0,1,ty]],dtype=np.float32) 
        trans_img=cv2.warpAffine(img, tm, dsize=(cols,rows)) 
        st.image(trans_img , caption= "Translation Image",  channels="BGR") 

    elif i == "Rotation": 
        center=(cols//2, rows//2)
        angle=np.random.randint(-360,360) 
        st.write(f"Center:{center}, Angle:{angle}")
        rm=cv2.getRotationMatrix2D(center, angle, 1 )
        rotat_img=cv2.warpAffine(img, rm, dsize=(cols,rows))
        st.image(rotat_img , caption="Rotation Image",  channels="BGR" )

    elif i == "Scaling": 
        sx, sy =  np.random.uniform(0.3,1.5), np.random.uniform(0.3,1.5) 
        st.write(f"Sx:{sx}, Sy:{sy}")
        rm=np.array([[sx,0,0],[0,sy,0]],dtype=np.float32) 
        scale_img=cv2.warpAffine(img, rm, dsize=(cols,rows))
        st.image(scale_img , caption="Scaling Image",  channels="BGR" )

    elif i == "Shearing": 
        shx, shy =  np.random.uniform(0,0.35), np.random.uniform(0,0.35) 
        st.write(f"Shx:{shx}, Sy:{shy}")
        shm = np.array([[1,shx,0],[shy,1,0]],dtype=np.float32) 
        shear_img=cv2.warpAffine(img, shm, dsize=(cols,rows))
        st.image(shear_img , caption="Shearing Image",  channels="BGR" )

    elif i == "Cropping":
        x1 = random.randint(0, cols // 5)
        y1 = random.randint(0, rows // 5)
        x2 = random.randint(4 * cols // 5, cols)
        y2 = random.randint(4 * rows // 5, rows)
        crop_img = img[y1:y2, x1:x2]
        crop_img = cv2.resize(crop_img, (cols, rows)) 
        st.image(crop_img , caption="Cropping Image",  channels="BGR" )


    elif i == "Brightness": 
        bright_arr=np.full((rows,cols,3),np.random.randint(0,157,dtype=np.uint8),)
        # st.write(bright_arr.shape)
        # st.write(img.shape)
        if np.random.choice(["a","b"]) =="a": 
            bright_img=cv2.add(img,bright_arr)
        else:
            bright_img=cv2.subtract(img,bright_arr)
            
        st.image(bright_img , caption="Brightness Image",  channels="BGR" )


    elif i == "Grayscale":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converting img into gray scale with shape (rows,cols)
        gray_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR) # converting gray image into bgr image having 3- with shape (rows,cols,depth)
        st.image(gray_img , caption="GrayScale Image",  )

    elif i == "Flip Horizontally":
        fliphor_img = cv2.flip(img, 1) 
        st.image(fliphor_img , caption="Flip Horizontally Image",  channels="BGR" )

    elif i == "Flip Vertically":
        flipver_img = cv2.flip(img, 0)
        st.image(flipver_img , caption="Flip Vertically Image",  channels="BGR" )


# st.sidebar.header("🔧 Augmentation Settings")
# transform_options = st.sidebar.multiselect(
#     "🔄 Choose transformations (can select multiple)",
#     ["Translation", "Cropping", "Shearing", "Rotation", "Scaling",
#      "Grayscale", "Flip Horizontally", "Flip Vertically"],
#     placeholder="Enter multiple transformations"
# )
# count = st.sidebar.slider("📈 Number of images to generate", 10, 200, 100, step=10)



