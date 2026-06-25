import streamlit as st
import base64


def load_css():

    def get_base64(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()

    img = get_base64("assets/gym.jpg")

    st.markdown(
        f"""
<style>

/* MAIN APP */

.stApp {{
    background:
    radial-gradient(circle at top left,
    rgba(255,0,255,0.08),
    transparent 30%),

    radial-gradient(circle at bottom right,
    rgba(0,212,255,0.08),
    transparent 30%),

    #050505;
}}

#MainMenu {{
    visibility:hidden;
}}

footer {{
    visibility:hidden;
}}

header {{
    visibility:hidden;
}}

/* SIDEBAR */

[data-testid="stSidebar"] {{

    background-image:
    linear-gradient(
    rgba(0,0,0,0.82),
    rgba(0,0,0,0.88)
    ),
    url("data:image/jpg;base64,{img}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

[data-testid="stSidebar"] * {{
    color:white !important;
}}

[data-testid="stSidebarNav"] {{
    background: rgba(0,0,0,0.25);
    backdrop-filter: blur(12px);
    border-radius:20px;
    padding:10px;
}}

[data-testid="stSidebarNav"] a[aria-current="page"] {{

    background:
    linear-gradient(
    90deg,
    #7b2cff,
    #ff00ff
    );

    border-radius:15px;

    box-shadow:
    0px 0px 25px rgba(255,0,255,0.7);
}}

/* GLOBAL TEXT */

h1,h2,h3,h4,h5,h6 {{
    color:white;
}}

p,label,span {{
    color:#d9d9d9;
}}

/* INPUTS */

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {{
    background:#111111;
    color:white;
}}

/* BUTTONS */

.stButton > button {{

    width:100%;
    border:none;

    border-radius:15px;

    padding:14px;

    color:white;

    font-weight:700;

    background:
    linear-gradient(
    90deg,
    #7b2cff,
    #ff00ff
    );
}}

.stButton > button:hover {{

    box-shadow:
    0px 0px 20px rgba(255,0,255,0.6);
}}

/* METRICS */

[data-testid="stMetric"] {{

    background:#111111;

    border-radius:15px;

    padding:15px;

    border:1px solid rgba(255,255,255,0.05);
}}

</style>
""",
        unsafe_allow_html=True,
    )