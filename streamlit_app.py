import streamlit as st 
import pandas as pd
import math
import os

st.title("Photo Me")

st.markdown("_________")

st.subheader("Upload photo,\n Choose a file\n Choose a Photo")

uploaded_file = st.file_uploader("Upload a Photo", type=["jpg","png","jpeg"])

if uploaded_file:
    st.image(uploaded_file)
st.button("Upload File")
st.button("Photo Set")

st.image(f"{type}")
