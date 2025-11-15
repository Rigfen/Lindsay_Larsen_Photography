import streamlit as st 
import pandas as pd
import math
import os

col1, col2, col3 = st.columns ([1,2,1])
with col2:
    st.title("Photo Me")

st.markdown(

)
st.subheader("Upload photo,\n Choose a file\n Choose a Photo")

uploaded_file = st.file_uploader("Upload a Photo", type=["jpg","png","jpeg"])

if uploaded_file:
    st.image(uploaded_file)
