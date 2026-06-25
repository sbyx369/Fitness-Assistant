import streamlit as st
from PIL import Image

from utils.food_analyzer import analyze_food_image
from utils.styles import load_css

st.set_page_config(
    page_title="Food Analyzer",
    page_icon="🍱",
    layout="wide"
)

load_css()

st.title("🍱 Food Calorie Analyzer")
# st.title("🍱 AI Food Calorie Analyzer")

uploaded_file = st.file_uploader(
    "Upload Food Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        use_container_width=True
    )

    if st.button("🔍 Analyze Meal"):

        with st.spinner("Analyzing your meal..."):

            result = analyze_food_image(image)

            st.success("Analysis Complete")

            st.markdown(result)