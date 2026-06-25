from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def analyze_food_image(image):

    prompt = """
    You are an expert nutritionist.

    Analyze the uploaded meal image.

    Identify every food item visible.

    For each item provide:
    - Estimated quantity
    - Calories
    - Protein
    - Carbohydrates
    - Fat
    - Fiber

    Then provide:

    1. Total Meal Calories
    2. Total Protein
    3. Total Carbs
    4. Total Fat
    5. Total Fiber

    Assess whether the meal is:
    - Balanced
    - High Protein
    - High Carb
    - High Fat
    - Low Fiber

    If unhealthy:
    give warnings and healthier alternatives.

    If healthy:
    appreciate and encourage the user.

    Format in markdown tables.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt, image]
    )

    return response.text