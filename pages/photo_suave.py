import streamlit as st
import os
import photo_data

st.title("Upload & Select Photos")

# Ensure photos folder exists
os.makedirs("photos", exist_ok=True)

# Load existing data
data = photo_data.load_data()

# Upload a new image
uploaded_file = st.file_uploader("Upload a Photo", type=["jpg", "png", "jpeg"])

if uploaded_file:
    file_path = os.path.join("photos", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if uploaded_file.name not in data["uploaded_photos"]:
        data["uploaded_photos"].append(uploaded_file.name)
        photo_data.save_data(data)

    st.success("Photo uploaded!")

st.markdown("---")
st.subheader("Select photos for Photo Set")

# Multi-select UI
selected = st.multiselect(
    "Choose photos to include:",
    data["uploaded_photos"],
    default=data["photo_set"]
)

if st.button("Save Photo Set"):
    data["photo_set"] = selected
    photo_data.save_data(data)
    st.success("Photo Set updated!")
