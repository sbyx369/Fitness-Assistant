import streamlit as st

from utils.gemini_helper import generate_plan
from utils.prompts import create_prompt
from utils.bmi_calculator import calculate_bmi
from utils.styles import load_css

st.set_page_config(
    page_title="Diet Planner",
    page_icon="🏋️",
    layout="wide"
)

load_css()

st.title("🏋️ Diet & Workout Planner")

# st.set_page_config(
#     page_title="AI Diet & Workout Planner",
#     page_icon="🏋️",
#     layout="wide"
# )

# st.title("🏋️ AI Personalized Diet & Workout Planner")

st.write(
    "Generate personalized fitness and nutrition plans using AI."
)

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=15,
        max_value=80,
        value=22
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    height = st.number_input(
        "Height (cm)",
        min_value=100,
        max_value=250,
        value=170
    )

with col2:

    weight = st.number_input(
        "Weight (kg)",
        min_value=30,
        max_value=200,
        value=70
    )

    goal = st.selectbox(
        "Fitness Goal",
        [
            "Weight Loss",
            "Muscle Gain",
            "Maintain Weight"
        ]
    )

    activity = st.selectbox(
        "Activity Level",
        [
            "Sedentary",
            "Moderate",
            "Active"
        ]
    )

diet = st.selectbox(
    "Diet Preference",
    [
        "Vegetarian",
        "Non-Vegetarian",
        "Vegan"
    ]
)

bmi, category = calculate_bmi(weight, height)

st.metric(
    "BMI",
    bmi
)

st.info(f"Category: {category}")

if st.button("🚀 Generate My Plan"):

    with st.spinner("Creating your personalized plan..."):

        prompt = create_prompt(
            age,
            gender,
            height,
            weight,
            goal,
            diet,
            activity
        )

        plan = generate_plan(prompt)

        st.success("Plan Generated!")

        st.markdown(plan)