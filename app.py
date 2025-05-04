import streamlit as st 
import numpy as np 
import cv2
import random  

def translation(picture):
    tx, ty=np.random.randint(-60,60), np.random.randint(-60,60) 
    tm=np.array([[1,0,tx],[0,1,ty]],dtype=np.float32) 
    trans_img=cv2.warpAffine(picture, tm, dsize=(cols,rows)) 
    st.image(trans_img , caption= "Translation Image",  channels="BGR") 
    return trans_img 

def rotation(picture):
    center=(cols//2, rows//2)
    angle=np.random.randint(-180,180) 
    rm=cv2.getRotationMatrix2D(center, angle, 1 )
    rotat_img=cv2.warpAffine(picture, rm, dsize=(cols,rows))
    st.image(rotat_img , caption="Rotation Image",  channels="BGR" )
    return rotat_img

def scaling(picture):
    sx, sy =  np.random.uniform(0.3,1.5), np.random.uniform(0.3,1.5) 
    rm=np.array([[sx,0,0],[0,sy,0]],dtype=np.float32) 
    scale_img=cv2.warpAffine(picture, rm, dsize=(cols,rows))
    st.image(scale_img , caption="Scaling Image",  channels="BGR" )
    return scale_img 

def shearing(picture):
    shx, shy =  np.random.uniform(0,0.35), np.random.uniform(0,0.35) 
    #st.write(f"Shx:{shx}, Sy:{shy}")
    shm = np.array([[1,shx,0],[shy,1,0]],dtype=np.float32) 
    shear_img=cv2.warpAffine(picture, shm, dsize=(cols,rows))
    st.image(shear_img , caption="Shearing Image",  channels="BGR" ) 
    return shear_img  

def cropping(picture):
    x1 = random.randint(0, cols // 5)
    y1 = random.randint(0, rows // 5)
    x2 = random.randint(4 * cols // 5, cols)
    y2 = random.randint(4 * rows // 5, rows)
    crop_img = picture[y1:y2, x1:x2]
    crop_img = cv2.resize(crop_img, (cols, rows)) 
    st.image(crop_img , caption="Cropping Image",  channels="BGR" )
    return crop_img

def brightness(picture):
    bright_arr=np.full((rows,cols,3),np.random.randint(0,157,dtype=np.uint8),)
    # st.write(bright_arr.shape)  and st.write(img.shape) are equal 
    if np.random.choice(["add", "subtract"]) == "add": 
        bright_img=cv2.add(picture,bright_arr)
    else:
        bright_img=cv2.subtract(picture,bright_arr)
    st.image(bright_img , caption="Brightness Image",  channels="BGR" )
    return bright_img

def grayscale(picture):
    gray = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY) # converting img into gray scale with shape (rows,cols)
    gray_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR) # converting gray image into bgr image having 3- with shape (rows,cols,depth)
    st.image(gray_img , caption="GrayScale Image",  )
    return gray_img 


def flip_horizontally(picture):
    fliphor_img = cv2.flip(picture, 1) 
    st.image(fliphor_img , caption="Flip Horizontally Image",  channels="BGR" )
    return fliphor_img

def flip_vertically(picture):
    flipver_img = cv2.flip(picture, 0)
    st.image(flipver_img , caption="Flip Vertically Image",  channels="BGR" )
    return flipver_img

file_uploader=st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])  

options = st.sidebar.pills("Select the options for Image Augmentation", ["Translation", "Rotation", "Scaling", "Shearing","Cropping", "Brightness","Grayscale","Flip Horizontally","Flip Vertically"] ,
                             selection_mode="multi")
st.sidebar.markdown(f"Your selected options: {options}.")

number_of_images=number = st.sidebar.number_input("Number of Augmented Images Required:", value=len(options),min_value=0, step=len(options), placeholder="Type a number...")


if file_uploader is not None:
    file_bytes = np.frombuffer(file_uploader.read(), np.uint8)
    original_img = cv2.imdecode(file_bytes, 1) # 1 is for color image 
    st.image(original_img,  caption="Original Image", channels="BGR")
    rows,cols = original_img.shape[0:2]
    #st.write(rows,cols)

    if options:
        
        if (number_of_images % len(options)==0) or (number_of_images==0):                      
        
            transformed_augment_imgs=[]
            
            for i in range(int(number_of_images/len(options))):
                img=original_img.copy()         
            
                if "Translation" in options: 
                    transformed_augment_imgs.append(translation(img))
                    
                if "Rotation" in options: 
                    transformed_augment_imgs.append(rotation(img))
                
                if "Scaling" in options:
                    transformed_augment_imgs.append(scaling(img))
            
                if "Shearing" in options:
                    transformed_augment_imgs.append(shearing(img))
            
                if "Cropping" in options:
                    transformed_augment_imgs.append(cropping(img))
            
                if "Brightness" in options:
                    transformed_augment_imgs.append(brightness(img))    

                if "Grayscale" in options:
                    transformed_augment_imgs.append(grayscale(img))
            
                if "Flip Horizontally" in options:
                    transformed_augment_imgs.append(flip_horizontally(img))
            
                if "Flip Vertically" in options:
                    transformed_augment_imgs.append(flip_vertically(img))                    
    
            st.write(len(transformed_augment_imgs))
            
        else:
            st.error(f"The 'Number of Augmented Images Required' must be a multiple of the number of selected options ({len(options)}). Please enter a valid number.")
    
    else:
        st.warning("Please select at least one augmentation option.")
    


           

      

 
