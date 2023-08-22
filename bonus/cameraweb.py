import streamlit as st
from PIL import Image

camera_image = st.camera_input("Camera")

if camera_image:
    #create a pillow image instance
    img = Image.Open(camera_image)

    #convert a pillow image to gray
    gray_img = img.convert("L")

    #render the graye image on the page
    st.image(gray_img)