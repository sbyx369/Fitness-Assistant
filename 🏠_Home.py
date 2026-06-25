import streamlit as st
import base64
from utils.styles import load_css

load_css()
st.set_page_config(
    page_title="AI Fitness Assistant",
    page_icon="🏋️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# LOAD SIDEBAR IMAGE
# ==========================================

def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("assets/gym.jpg")

# ==========================================
# STYLING
# ==========================================

st.markdown(
    f"""
<style>

/* Main Background */

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

/* Hide Streamlit Elements */

#MainMenu {{
    visibility:hidden;
}}

footer {{
    visibility:hidden;
}}

header {{
    visibility:hidden;
}}

/* ==========================================
   SIDEBAR
========================================== */

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
    background: rgba(0,0,0,0.20);
    backdrop-filter: blur(12px);
    border-radius:20px;
    padding:10px;
}}

[data-testid="stSidebarNav"] li {{
    margin-bottom:10px;
}}

[data-testid="stSidebarNav"] a {{
    border-radius:15px;
}}

[data-testid="stSidebarNav"] a:hover {{

    background:
    linear-gradient(
    90deg,
    rgba(123,44,255,0.6),
    rgba(255,0,255,0.4)
    );

    transition:0.3s;
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

/* ==========================================
   HERO SECTION
========================================== */

.hero-title {{

    font-size:85px;
    font-weight:900;
    line-height:1.05;

    margin-bottom:15px;
}}

.gradient-text {{

    background:
    linear-gradient(
    90deg,
    #ff00ff,
    #7b2cff,
    #00d4ff
    );

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}}

.subtitle {{

    color:#c7c7c7;
    font-size:26px;
    line-height:1.6;
}}

.badge {{

    display:inline-block;

    padding:12px 22px;

    border-radius:50px;

    background:rgba(255,255,255,0.05);

    border:1px solid rgba(255,255,255,0.08);

    color:#c76cff;

    font-weight:700;

    margin-bottom:20px;
}}

/* ==========================================
   CARDS
========================================== */

.card {{

    background:#0c0c0c;

    border-radius:25px;

    padding:25px;

    min-height:280px;

    border:1px solid rgba(255,255,255,0.08);

    box-shadow:
    0px 0px 25px rgba(255,0,255,0.12);
}}

.card:hover {{

    transform:translateY(-5px);
}}

.card-title {{

    color:white;
    font-size:28px;
    font-weight:700;
}}

.card-desc {{

    color:#bdbdbd;
    font-size:18px;
}}

.icon {{
    font-size:60px;
}}

/* ==========================================
   BUTTONS
========================================== */

.stButton > button {{

    width:100%;

    border:none;

    border-radius:14px;

    padding:14px;

    font-size:18px;

    font-weight:700;

    color:white;

    background:
    linear-gradient(
    90deg,
    #7b2cff,
    #ff00ff
    );
}}

/* ==========================================
   METRICS
========================================== */

.metric-box {{

    background:rgba(255,255,255,0.03);

    border:1px solid rgba(255,255,255,0.08);

    border-radius:20px;

    padding:20px;

    margin-top:30px;
}}

</style>
""",
    unsafe_allow_html=True,
)

# ==========================================
# PAGE CONTENT
# ==========================================

st.markdown(
    """
<div class="badge">
✨ AI POWERED FITNESS ASSISTANT
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="hero-title">
Your Personal
<br>
<span class="gradient-text">
Fitness Companion
</span>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="subtitle">
Get personalized diet plans, workout routines,
food analysis and progress tracking powered by AI.
</div>
""",
    unsafe_allow_html=True,
)

st.write("")
st.write("")

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown(
        """
<div class="card">

<div class="icon">🏋️</div>

<br>

<div class="card-title">
Diet & Workout Planner
</div>

<br>

<div class="card-desc">
Generate personalized workout and
nutrition plans based on your goals.
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.button("🚀 Explore Planner")

with c2:

    st.markdown(
        """
<div class="card">

<div class="icon">🍱</div>

<br>

<div class="card-title">
Food Analyzer
</div>

<br>

<div class="card-desc">
Upload food images and get
protein, calories, carbs,
fat and fiber estimates.
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.button("🔍 Analyze Food")

with c3:

    st.markdown(
        """
<div class="card">

<div class="icon">📈</div>

<br>

<div class="card-title">
Progress Tracker
</div>

<br>

<div class="card-desc">
Track weight changes and
receive AI-powered feedback.
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.button("📊 Track Progress")

st.write("")
st.write("")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("🔥 Calories Burned", "2450")

with m2:
    st.metric("⚖ Weight Change", "-2.4 kg")

with m3:
    st.metric("🏆 Workouts", "18")

with m4:
    st.metric("🎯 Goal Progress", "75%")

st.markdown("---")

st.markdown(
    """
<center>

<h4 style="color:#8d8d8d;">
Strive for Progress, Not Perfection.
</h4>

</center>
""",
    unsafe_allow_html=True,
)