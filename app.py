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
        center=(col//2, row//2)
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







# st.sidebar.header("🔧 Augmentation Settings")
# transform_options = st.sidebar.multiselect(
#     "🔄 Choose transformations (can select multiple)",
#     ["Translation", "Cropping", "Shearing", "Rotation", "Scaling",
#      "Grayscale", "Flip Horizontally", "Flip Vertically"],
#     placeholder="Enter multiple transformations"
# )
# count = st.sidebar.slider("📈 Number of images to generate", 10, 200, 100, step=10)


# st.markdown('<div class="main">', unsafe_allow_html=True)
# st.markdown('<div class="title">📸 Image Augmentation App</div>', unsafe_allow_html=True)
# st.markdown('<div class="subtitle">Upload an image, choose transformations, preview, and download!</div>', unsafe_allow_html=True)

# uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

# def apply_multiple_transformations(image, options, count):
#     rows, cols = image.shape[:2]
#     transformed_images = []

#     for _ in range(count):
#         img = image.copy()
#         for option in options:
#             if option == "Translation":
#                 tx, ty = random.randint(-50, 50), random.randint(-50, 50)
#                 M = np.float32([[1, 0, tx], [0, 1, ty]])
#                 img = cv2.warpAffine(img, M, (cols, rows))

#             elif option == "Cropping":
#                 x1 = random.randint(0, cols // 4)
#                 y1 = random.randint(0, rows // 4)
#                 x2 = random.randint(3 * cols // 4, cols)
#                 y2 = random.randint(3 * rows // 4, rows)
#                 img = img[y1:y2, x1:x2]
#                 img = cv2.resize(img, (cols, rows))

#             elif option == "Shearing":
#                 shear_factor = random.uniform(-0.3, 0.3)
#                 M = np.float32([[1, shear_factor, 0], [shear_factor, 1, 0]])
#                 img = cv2.warpAffine(img, M, (cols, rows))

#             elif option == "Rotation":
#                 angle = random.randint(-45, 45)
#                 center = (cols // 2, rows // 2)
#                 M = cv2.getRotationMatrix2D(center, angle, 1.0)
#                 img = cv2.warpAffine(img, M, (cols, rows))

#             elif option == "Scaling":
#                 scale = random.uniform(0.5, 1.5)
#                 resized = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
#                 img = cv2.resize(resized, (cols, rows))

#             elif option == "Grayscale":
#                 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#                 img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

#             elif option == "Flip Horizontally":
#                 img = cv2.flip(img, 1)

#             elif option == "Flip Vertically":
#                 img = cv2.flip(img, 0)

#         transformed_images.append(img)

#     return transformed_images

# if uploaded_file:
#     file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#     image = cv2.imdecode(file_bytes, 1)

#     if image is None:
#         st.error("❌ Failed to decode the image. Please upload a valid image file.")
#         st.stop()

#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     st.image(image_rgb, caption="📷 Original Image", use_container_width=True)

#     if st.button("✨ Generate Augmented Images"):
#         with st.spinner("Generating images..."):
#             augmented_images = apply_multiple_transformations(image, transform_options, count)

#             st.markdown("### 🔍 Preview of Augmented Images")
#             preview_cols = st.columns(3)
#             for i in range(min(3, len(augmented_images))):
#                 preview_img = cv2.cvtColor(augmented_images[i], cv2.COLOR_BGR2RGB)
#                 preview_cols[i].image(preview_img, use_container_width=True)

#             zip_buffer = io.BytesIO()
#             with zipfile.ZipFile(zip_buffer, "w") as zip_file:
#                 for idx, img in enumerate(augmented_images):
#                     is_success, buffer = cv2.imencode(".png", img)
#                     zip_file.writestr(f"augmented_{idx+1}.png", buffer.tobytes())
#             zip_buffer.seek(0)

#         st.success(f"✅ {count} Augmented Images Generated!")
#         st.download_button("📁 Download ZIP", zip_buffer, "augmented_images.zip", "application/zip")

# st.markdown('</div>', unsafe_allow_html=True)