import streamlit as st
import pandas as pd
from datetime import date
from utils.styles import load_css

st.set_page_config(
    page_title="Progress Tracker",
    page_icon="📈",
    layout="wide"
)

load_css()

st.title("📈 Progress Tracker")

# st.title("📈 Fitness Progress Tracker")

FILE_PATH = "data/progress.csv"

today = date.today()

weight = st.number_input(
    "Current Weight (kg)",
    min_value=20.0,
    max_value=300.0,
    value=70.0
)

if st.button("Save Progress"):

    new_entry = pd.DataFrame(
        {
            "Date":[today],
            "Weight":[weight]
        }
    )

    try:
        existing = pd.read_csv(FILE_PATH)

        updated = pd.concat(
            [existing,new_entry],
            ignore_index=True
        )

    except:
        updated = new_entry

    updated.to_csv(
        FILE_PATH,
        index=False
    )

    st.success("Progress Saved!")

try:

    df = pd.read_csv(FILE_PATH)

    st.subheader("Weight History")

    st.dataframe(df)

    st.line_chart(
        df.set_index("Date")["Weight"]
    )

    if len(df) > 1:

        change = (
            df["Weight"].iloc[-1]
            - df["Weight"].iloc[0]
        )

        st.metric(
            "Overall Change",
            f"{change:.2f} kg"
        )

except:
    st.info(
        "Start tracking your progress."
    )