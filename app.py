import streamlit as st 

file_uploader=st.file_uploader("Choose an image") 

if file_uploader is not None:
    st.write(file_uploader.getvalue())