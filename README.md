# 🏋️ AI Fitness Assistant

An AI-powered fitness companion that helps users plan workouts, analyze meals, and track fitness progress using Generative AI.

## 🚀 Features

### 🏋️ Personalized Diet & Workout Planner

* Generates customized workout routines
* Creates personalized diet plans
* Calculates BMI
* Provides water intake recommendations
* Tailored to fitness goals and activity levels

### 🍱 AI Food Calorie Analyzer

* Upload a food image
* Detects food items in the meal
* Estimates:

  * Calories
  * Protein
  * Carbohydrates
  * Fat
  * Fiber
* Provides nutritional feedback and health recommendations

### 📈 Progress Tracker

* Track weight changes over time
* Visualize progress with charts
* Monitor fitness goals
* Receive AI-generated progress insights

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Gemini AI (Google GenAI)
* Pandas
* Pillow
* Plotly
* Python Dotenv

---

## 📂 Project Structure

```text
AI_Fitness_Assistant/

├── app.py

├── pages/
│   ├── 1_🏋️_Diet_Workout_Planner.py
│   ├── 2_🍱_Food_Calorie_Analyzer.py
│   └── 3_📈_Progress_Tracker.py

├── utils/
│   ├── bmi_calculator.py
│   ├── food_analyzer.py
│   ├── gemini_helper.py
│   ├── prompts.py
│   └── styles.py

├── assets/
│   └── gym.jpg

├── data/
│   └── progress.csv

├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd AI_Fitness_Assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment File

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 🎯 Future Enhancements

* User Authentication
* Progress Prediction using AI
* Workout Demonstration Videos
* Daily Fitness Challenges
* Health Report Generation
* Smart Meal Recommendations

---

## 👨‍💻 Developed By

Bhargav Yadav

Built using Streamlit and Gemini AI.

