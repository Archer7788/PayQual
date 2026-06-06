import os

from dotenv import load_dotenv

from google import genai


load_dotenv(dotenv_path=".env")


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_ai_summary(report):

    prompt = f"""
    You are a senior data quality analyst.

    Analyze this dataset quality report.

    Report:
    {report}

    Include:
    - dataset health summary
    - key issues
    - what is the dataset about?
    - improvement suggestions

    Keep response concise and professional.
    """

    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt
    )

    return response.text