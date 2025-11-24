import streamlit as st
import os
import photo_data

st.title("Photo Me")
st.image("IMG_6127.jpeg")
st.subheader("Upload photo,\n Choose a file\n Choose a Photo")
st.markdown("__________")

# View only selected photos
if st.button("Photo Set"):
    st.subheader("Photo Set")

    data = photo_data.load_data()

    if not data["photo_set"]:
        st.info("No photos selected for the photo set.")
    else:
        for filename in data["photo_set"]:
            path = os.path.join("photos", filename)
            if os.path.exists(path):
                st.image(path, caption=filename)
            else:
                st.error(f"Missing file: {filename}")
