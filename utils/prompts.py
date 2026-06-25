def create_prompt(
    age,
    gender,
    height,
    weight,
    goal,
    diet,
    activity
):

    prompt = f"""
    You are an expert fitness trainer and nutritionist.

    Create a personalized fitness plan.

    User Details:
    Age: {age}
    Gender: {gender}
    Height: {height} cm
    Weight: {weight} kg
    Goal: {goal}
    Diet Preference: {diet}
    Activity Level: {activity}

    Provide:

    1. BMI Analysis
    2. Daily Calories Needed
    3. Water Intake Recommendation
    4. Weekly Workout Plan
    5. 7-Day Diet Plan
    6. Health Tips

    Keep suggestions realistic and affordable for students.
    """

    return prompt