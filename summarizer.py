import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load environment variables
load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("No API key was found!")
elif api_key.strip() != api_key:
    raise ValueError("API key contains leading or trailing whitespace.")


# Create Gemini client
client = genai.Client(api_key=api_key)


# Define prompts
system_prompt = """
You are a snarky assistant that analyzes the contents of a website
and provides a short, snarky, humorous summary, ignoring navigation
related text.
Respond in markdown. Do not wrap the markdown in a code block.
"""

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, summarize these too.

"""


def summarize_website(website_content):
    """Generate a summary of the supplied website content using Gemini."""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=user_prompt_prefix + website_content,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt
        )
    )

    return response.text