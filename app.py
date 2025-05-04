# import streamlit as st 
# import numpy as np 
# import cv2 



# def trans_rotat_scale(picture,tx=0,ty=0,sx=1,sy=1,shx=0,shy=0):    
#     tm=np.array([[sx,shx,tx],[shy,sy,ty]],dtype=np.float32) 
#     trans_img=cv2.warpAffine(picture, tm, dsize=(cols,rows)) 
#     return trans_img 

# def trans_rotation(picture,angle,tx=0,ty=0):
#     rot_mat=cv2.getRotationMatrix2D((cols//2, rows//2), angle, 1 )
#     trans_mat=np.array([[1,0,tx],[0,1,ty]],dtype=np.float32) 
#     rot_hom = np.append(rot_mat, [[0, 0, 1]], axis=0) # in homogeneous coordinates
#     tr_hom = np.append(trans_mat, [[0, 0, 1]], axis=0)
#     rm = rot_hom@tr_hom
#     rotat_img=cv2.warpAffine(picture, rm[:2,:], dsize=(cols,rows))
#     return rotat_img   

# def cropping(picture):
#     x1 = np.random.randint(0, cols // 5)
#     y1 = np.random.randint(0, rows // 5)
#     x2 = np.random.randint(4 * cols // 5, cols)
#     y2 = np.random.randint(4 * rows // 5, rows)
#     crop_img = picture[y1:y2, x1:x2]
#     crop_img = cv2.resize(crop_img, (cols, rows)) 
#     return crop_img

# def brightness(picture):
#     bright_arr=np.full((rows,cols,3),np.random.randint(0,120,dtype=np.uint8),) # st.write(bright_arr.shape) and st.write(img.shape) should be equal 
#     if np.random.choice(["add", "subtract"]) == "add": 
#         bright_img=cv2.add(picture,bright_arr)
#     else:
#         bright_img=cv2.subtract(picture,bright_arr)
#     return bright_img

# def grayscale(picture):
#     gray = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY) # converting img into gray scale with shape (rows,cols)
#     gray_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR) # converting gray image into bgr image having 3- with shape (rows,cols,depth)
#     return gray_img 


# def flip_horizontally(picture):
#     fliphor_img = cv2.flip(picture, 1) 
#     return fliphor_img

# def flip_vertically(picture):
#     flipver_img = cv2.flip(picture, 0)
#     return flipver_img 


# st.title("Image Augmentation App")
# st.sidebar.header("Image Augmentation Controls")


# file_uploader=st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])  

# options = st.sidebar.pills("Select the options for Image Augmentation", ["Translation", "Rotation", "Scaling", "Shearing","Cropping",
#                            "Brightness","Grayscale","Flip Horizontally","Flip Vertically","Combination of Translation, Scaling & Shearing","Combination of Translation & Rotation"] ,
#                              selection_mode="multi")
# st.sidebar.markdown(f"Your selected options: {options}.")

# number_of_images= st.sidebar.number_input("Number of Augmented Images Required:", value=None, min_value=1, step=1, placeholder="Type a number...")
# st.write(options)

# if file_uploader is not None:
#     file_bytes = np.frombuffer(file_uploader.read(), np.uint8) 
#     original_img = cv2.imdecode(file_bytes, 1) # 1 is for color image 
#     st.image(original_img,  caption="Original Image", channels="BGR")
#     rows,cols = original_img.shape[0:2]
#     #st.write(rows,cols)

#     if options is not None:

#         if number_of_images is not None:
            
#             img=original_img.copy() 
#             transformed_augment_imgs=[]
        
#             for i in range(number_of_images):         
#                 img=original_img.copy()
#                 option = np.random.choice(options)
                                
#                 if option =="Translation":
#                     tx, ty=np.random.randint(-60,60), np.random.randint(-60,60) 
#                     img=trans_rotat_scale(picture=img,tx=tx,ty=ty) 
#                     transformed_augment_imgs.append(img) 
                        
#                 elif option =="Rotation":
#                     angle=np.random.randint(-180,180)
#                     img=trans_rotation(picture=img,angle=angle)
#                     transformed_augment_imgs.append(img)
    
#                 elif option =="Scaling":
#                     sx, sy =  np.random.uniform(0.5,1.5), np.random.uniform(0.5,1.5)
#                     img=trans_rotat_scale(picture=img,sx=sx,sy=sy) 
#                     transformed_augment_imgs.append(img) 
                    
#                 elif option =="Shearing":
#                     shx, shy =  np.random.uniform(0,0.35), np.random.uniform(0,0.35)
#                     img=trans_rotat_scale(picture=img,shx=shx,shy=shy) 
#                     transformed_augment_imgs.append(img) 
                    
#                 elif option =="Cropping":
#                     img=cropping(img) 
#                     transformed_augment_imgs.append(img) 
                        
#                 elif option =="Brightness":
#                     img=brightness(img)
#                     transformed_augment_imgs.append(img) 
                    
#                 elif option =="Grayscale":
#                     img=grayscale(img) 
#                     transformed_augment_imgs.append(img) 
                    
#                 elif option =="Flip Horizontally":
#                     img=flip_horizontally(img) 
#                     transformed_augment_imgs.append(img) 
                
#                 elif option =="Flip Vertically":
#                     img=flip_vertically(img) 
#                     transformed_augment_imgs.append(img) 
                    
#                 elif option == "Combination of Translation, Scaling & Shearing":
#                     tx, ty=np.random.randint(-60,60), np.random.randint(-60,60)
#                     sx, sy =  np.random.uniform(0.5,1.5), np.random.uniform(0.5,1.5)
#                     shx, shy =  np.random.uniform(0,0.35), np.random.uniform(0,0.35) 
#                     img=trans_rotat_scale(picture=img, tx=tx, ty=ty, sx=sx, sy=sy, shx=shx, shy=shy) 
#                     transformed_augment_imgs.append(img) 
                
#                 elif option == "Combination of Translation & Rotation":
#                     tx, ty=np.random.randint(-60,60), np.random.randint(-60,60)
#                     angle=np.random.randint(-180,180)
#                     img=trans_rotation(picture=img,angle=angle,tx=tx,ty=ty)
#                     transformed_augment_imgs.append(img)                                 
                             
        
#             st.write(len(transformed_augment_imgs))
    
    
#             for i in transformed_augment_imgs:
#                 image=cv2.cvtColor(i,cv2.COLOR_BGR2RGB)
#                 st.image(image,)

                
#         else:
#             st.info("""Please select at least one augmentation option from the sidebar.
#             Enter the number of images you want to generate in the sidebar.""")
    
#     else:
#         st.info("Please select at least one augmentation option from the sidebar to generate augmented images.")
      
   
# else:
#     st.info("Please upload an image file (JPG, JPEG, or PNG) to begin augmentation.")
    
            

    
    
import streamlit as st
import numpy as np
import cv2
from PIL import Image
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title="Image Augmentation App", page_icon="🌟", layout="centered")

# Custom Style
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 24px;
        }
        .stFileUploader > div {
            background-color: #ffffff;
            border: 2px dashed #4CAF50;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>📸 Image Augmentation Playground</h1>
    <p style='text-align: center;'>Upload an image and apply a variety of transformations to explore data augmentation techniques!</p>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
    <h2 style='color: #4CAF50;'>🔧 Controls</h2>
""", unsafe_allow_html=True)

# Image augmentation functions
def trans_rotat_scale(picture, tx=0, ty=0, sx=1, sy=1, shx=0, shy=0):
    tm = np.array([[sx, shx, tx], [shy, sy, ty]], dtype=np.float32)
    return cv2.warpAffine(picture, tm, dsize=(cols, rows))

def trans_rotation(picture, angle, tx=0, ty=0):
    rot_mat = cv2.getRotationMatrix2D((cols // 2, rows // 2), angle, 1)
    trans_mat = np.array([[1, 0, tx], [0, 1, ty]], dtype=np.float32)
    rot_hom = np.append(rot_mat, [[0, 0, 1]], axis=0)
    tr_hom = np.append(trans_mat, [[0, 0, 1]], axis=0)
    rm = rot_hom @ tr_hom
    return cv2.warpAffine(picture, rm[:2, :], dsize=(cols, rows))

def cropping(picture):
    x1, y1 = np.random.randint(0, cols // 5), np.random.randint(0, rows // 5)
    x2, y2 = np.random.randint(4 * cols // 5, cols), np.random.randint(4 * rows // 5, rows)
    crop_img = picture[y1:y2, x1:x2]
    return cv2.resize(crop_img, (cols, rows))

def brightness(picture):
    bright_arr = np.full((rows, cols, 3), np.random.randint(0, 120, dtype=np.uint8))
    return cv2.add(picture, bright_arr) if np.random.rand() > 0.5 else cv2.subtract(picture, bright_arr)

def grayscale(picture):
    return cv2.cvtColor(cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)

def flip_horizontally(picture):
    return cv2.flip(picture, 1)

def flip_vertically(picture):
    return cv2.flip(picture, 0)

# File uploader
file_uploader = st.file_uploader("Upload an Image 📂", type=["jpg", "jpeg", "png"])

options = st.sidebar.multiselect(
    "🌀 Choose Augmentations:",
    ["Translation", "Rotation", "Scaling", "Shearing", "Cropping", "Brightness", "Grayscale",
     "Flip Horizontally", "Flip Vertically",
     "Combination of Translation, Scaling & Shearing", "Combination of Translation & Rotation"]
)

number_of_images = st.sidebar.number_input("🌟 Number of Augmented Images:", min_value=1, value=5)

# Image processing logic
if file_uploader is not None:
    file_bytes = np.frombuffer(file_uploader.read(), np.uint8)
    original_img = cv2.imdecode(file_bytes, 1)
    rows, cols = original_img.shape[:2]

    st.image(original_img, caption="📷 Original Image", channels="BGR")

    if options:
        st.success(f"Generating {number_of_images} augmented image(s)...")
        transformed_imgs = []

        for _ in range(number_of_images):
            img = original_img.copy()
            option = np.random.choice(options)

            if option == "Translation":
                img = trans_rotat_scale(img, tx=np.random.randint(-60, 60), ty=np.random.randint(-60, 60))
            elif option == "Rotation":
                img = trans_rotation(img, angle=np.random.randint(-180, 180))
            elif option == "Scaling":
                img = trans_rotat_scale(img, sx=np.random.uniform(0.5, 1.5), sy=np.random.uniform(0.5, 1.5))
            elif option == "Shearing":
                img = trans_rotat_scale(img, shx=np.random.uniform(0, 0.35), shy=np.random.uniform(0, 0.35))
            elif option == "Cropping":
                img = cropping(img)
            elif option == "Brightness":
                img = brightness(img)
            elif option == "Grayscale":
                img = grayscale(img)
            elif option == "Flip Horizontally":
                img = flip_horizontally(img)
            elif option == "Flip Vertically":
                img = flip_vertically(img)
            elif option == "Combination of Translation, Scaling & Shearing":
                img = trans_rotat_scale(img,
                    tx=np.random.randint(-60, 60), ty=np.random.randint(-60, 60),
                    sx=np.random.uniform(0.5, 1.5), sy=np.random.uniform(0.5, 1.5),
                    shx=np.random.uniform(0, 0.35), shy=np.random.uniform(0, 0.35))
            elif option == "Combination of Translation & Rotation":
                img = trans_rotation(img, angle=np.random.randint(-180, 180),
                    tx=np.random.randint(-60, 60), ty=np.random.randint(-60, 60))

            transformed_imgs.append(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        st.subheader(":sparkles: Augmented Images")
        for i, img in enumerate(transformed_imgs):
            st.image(img, caption=f"Augmented #{i+1}", use_column_width=True)

        rain(emoji="🌟", font_size=40, falling_speed=5, animation_length=1.5)
    else:
        st.warning("Please select at least one augmentation option from the sidebar.")
else:
    st.info("Upload a JPG, JPEG, or PNG file to get started.")

