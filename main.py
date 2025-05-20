
import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="Instrument Classifier", layout="centered")
st.title("Instrument Classifier")
st.write("Upload an image of a musical instrument to identify it.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Classifying..."):
        response = requests.post(
            "http://localhost:8000/predict",
            files={"file": uploaded_file.getvalue()},
        )
        if response.status_code == 200:
            prediction = response.json()["prediction"]
            st.success(f"Predicted Instrument: **{prediction}**")
        else:
            st.error("Prediction failed. Please try again.")
