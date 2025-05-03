# import streamlit as st 
# import numpy as np 
# import cv2
# import random  



# file_uploader=st.file_uploader("Choose an image")  

# options = st.sidebar.pills("Select the options for Image Augmentation", ["Translation", "Rotation", "Scaling", "Shearing","Cropping", "Brightness","Grayscale","Flip Horizontally","Flip Vertically"] ,
#                              selection_mode="multi")
# st.sidebar.markdown(f"Your selected options: {selection}.")

# number_of_images=number = st.sidebar.number_input("Number of Augmented Images Required:", value=None,min_value=0, step=1, placeholder="Type a number...")


# if file_uploader is not None:
#     file_bytes = np.frombuffer(file_uploader.read(), np.uint8)
#     original_img = cv2.imdecode(file_bytes, 1) # 1 is for color image 
#     st.image(original_img,  caption="Original Image", channels="BGR")
#     rows,cols = original_img.shape[0:2]
#     #st.write(rows,cols)


# for i in range(number_of_images):
#     img=original_img.copy() 

#     for option in options:
#         #st.write(i)
#         if i == "Translation": 
#             tx, ty=np.random.randint(-60,60), np.random.randint(-60,60) 
#             #st.write(f"Tx: {tx}, Ty={ty}")
#             tm=np.array([[1,0,tx],[0,1,ty]],dtype=np.float32) 
#             trans_img=cv2.warpAffine(img, tm, dsize=(cols,rows)) 
#             st.image(trans_img , caption= "Translation Image",  channels="BGR") 
    
#         elif option == "Rotation": 
#             center=(cols//2, rows//2)
#             angle=np.random.randint(-360,360) 
#             #st.write(f"Center:{center}, Angle:{angle}")
#             rm=cv2.getRotationMatrix2D(center, angle, 1 )
#             rotat_img=cv2.warpAffine(img, rm, dsize=(cols,rows))
#             st.image(rotat_img , caption="Rotation Image",  channels="BGR" )
    
#         elif option == "Scaling": 
#             sx, sy =  np.random.uniform(0.3,1.5), np.random.uniform(0.3,1.5) 
#             #st.write(f"Sx:{sx}, Sy:{sy}")
#             rm=np.array([[sx,0,0],[0,sy,0]],dtype=np.float32) 
#             scale_img=cv2.warpAffine(img, rm, dsize=(cols,rows))
#             st.image(scale_img , caption="Scaling Image",  channels="BGR" )

#         elif option == "Shearing": 
#             shx, shy =  np.random.uniform(0,0.35), np.random.uniform(0,0.35) 
#             #st.write(f"Shx:{shx}, Sy:{shy}")
#             shm = np.array([[1,shx,0],[shy,1,0]],dtype=np.float32) 
#             shear_img=cv2.warpAffine(img, shm, dsize=(cols,rows))
#             st.image(shear_img , caption="Shearing Image",  channels="BGR" )
    
#         elif option == "Cropping":
#             x1 = random.randint(0, cols // 5)
#             y1 = random.randint(0, rows // 5)
#             x2 = random.randint(4 * cols // 5, cols)
#             y2 = random.randint(4 * rows // 5, rows)
#             st.write(f"x1,x2=({x1},{x2}) and y1,y2=({y1},{y2})")
#             crop_img = img[y1:y2, x1:x2]
#             crop_img = cv2.resize(crop_img, (cols, rows)) 
#             st.image(crop_img , caption="Cropping Image",  channels="BGR" )      
    
#         elif option == "Brightness": 
#             bright_arr=np.full((rows,cols,3),np.random.randint(0,157,dtype=np.uint8),)
#             # st.write(bright_arr.shape)
#             # st.write(img.shape)
#             if np.random.choice(["a","b"]) =="a": 
#                 bright_img=cv2.add(img,bright_arr)
#             else:
#                 bright_img=cv2.subtract(img,bright_arr)
                
#             st.image(bright_img , caption="Brightness Image",  channels="BGR" )


#         elif option == "Grayscale":
#             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converting img into gray scale with shape (rows,cols)
#             gray_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR) # converting gray image into bgr image having 3- with shape (rows,cols,depth)
#             st.image(gray_img , caption="GrayScale Image",  )
    
#         elif option == "Flip Horizontally":
#             fliphor_img = cv2.flip(img, 1) 
#             st.image(fliphor_img , caption="Flip Horizontally Image",  channels="BGR" )
    
#         elif option == "Flip Vertically":
#             flipver_img = cv2.flip(img, 0)
#             st.image(flipver_img , caption="Flip Vertically Image",  channels="BGR" )




import streamlit as st
import cv2
import numpy as np
import io
import zipfile
import random

st.set_page_config(page_title="✨ Image Augmenter", layout="centered")

st.markdown("""
    <style>
    stApp {
        background-color: #f0f4f8;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
        max-width: 800px;
        margin: auto;
    }
    .title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #0066cc;
        text-align: center;
        margin-bottom: 0.5rem;
        animation: fadeInDown 1s ease-out;
    }
    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #333333;
        margin-bottom: 2rem;
        animation: fadeInUp 1.5s ease-out;
    }
    .stButton > button {
        background-color: #0066cc;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        transition: all 0.3s ease-in-out;
    }
    .stButton > button:hover {
        background-color: #004999;
        transform: scale(1.05);
    }
    @keyframes fadeInDown {
        0% { transform: translateY(-20px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    @keyframes fadeInUp {
        0% { transform: translateY(20px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)


st.sidebar.header("🔧 Augmentation Settings")
transform_options = st.sidebar.multiselect(
    "🔄 Choose transformations (can select multiple)",
    ["Translation", "Cropping", "Shearing", "Rotation", "Scaling",
     "Grayscale", "Flip Horizontally", "Flip Vertically"],
    placeholder="Enter multiple transformations"
)
count = st.sidebar.slider("📈 Number of images to generate", 10, 200, 100, step=10)


st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title">📸 Image Augmentation App</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload an image, choose transformations, preview, and download!</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

def apply_multiple_transformations(image, options, count):
    rows, cols = image.shape[:2]
    transformed_images = []

    for _ in range(count):
        img = image.copy()
        for option in options:
            if option == "Translation":
                tx, ty = random.randint(-50, 50), random.randint(-50, 50)
                M = np.float32([[1, 0, tx], [0, 1, ty]])
                img = cv2.warpAffine(img, M, (cols, rows))

            elif option == "Cropping":
                x1 = random.randint(0, cols // 4)
                y1 = random.randint(0, rows // 4)
                x2 = random.randint(3 * cols // 4, cols)
                y2 = random.randint(3 * rows // 4, rows)
                img = img[y1:y2, x1:x2]
                img = cv2.resize(img, (cols, rows))

            elif option == "Shearing":
                shear_factor = random.uniform(-0.3, 0.3)
                M = np.float32([[1, shear_factor, 0], [shear_factor, 1, 0]])
                img = cv2.warpAffine(img, M, (cols, rows))

            elif option == "Rotation":
                angle = random.randint(-45, 45)
                center = (cols // 2, rows // 2)
                M = cv2.getRotationMatrix2D(center, angle, 1.0)
                img = cv2.warpAffine(img, M, (cols, rows))

            elif option == "Scaling":
                scale = random.uniform(0.5, 1.5)
                resized = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
                img = cv2.resize(resized, (cols, rows))

            elif option == "Grayscale":
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

            elif option == "Flip Horizontally":
                img = cv2.flip(img, 1)

            elif option == "Flip Vertically":
                img = cv2.flip(img, 0)

        transformed_images.append(img)

    return transformed_images

if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    if image is None:
        st.error("❌ Failed to decode the image. Please upload a valid image file.")
        st.stop()

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    st.image(image_rgb, caption="📷 Original Image", use_container_width=True)

    if st.button("✨ Generate Augmented Images"):
        with st.spinner("Generating images..."):
            augmented_images = apply_multiple_transformations(image, transform_options, count)

            st.markdown("### 🔍 Preview of Augmented Images")
            preview_cols = st.columns(3)
            for i in range(min(3, len(augmented_images))):
                preview_img = cv2.cvtColor(augmented_images[i], cv2.COLOR_BGR2RGB)
                preview_cols[i].image(preview_img, use_container_width=True)

            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, "w") as zip_file:
                for idx, img in enumerate(augmented_images):
                    is_success, buffer = cv2.imencode(".png", img)
                    zip_file.writestr(f"augmented_{idx+1}.png", buffer.tobytes())
            zip_buffer.seek(0)

        st.success(f"✅ {count} Augmented Images Generated!")
        st.download_button("📁 Download ZIP", zip_buffer, "augmented_images.zip", "application/zip")

st.markdown('</div>', unsafe_allow_html=True)
