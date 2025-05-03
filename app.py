import streamlit as st 

file_uploader=st.file_uploader("Choose an image") 

options = ["Shifting (Translation)", "Rotation", "Scaling", "Shearing","Cropping"]
selection = st.pills("Directions", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")