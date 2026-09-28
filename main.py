import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from scraper import fetch_website_contents

load_dotenv(override=True)
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("No API key was found!")
elif api_key.strip() != api_key:
    raise ValueError("API key contains leading or trailing whitespace.")
else:
    print("API key found and looks good so far!")

client = genai.Client(api_key=api_key)

# Fetch website contents
url = input("Enter URL: ").strip()
ask = fetch_website_contents(url)

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

# Generate the summary
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=user_prompt_prefix + ask,
    config=types.GenerateContentConfig(
        system_instruction=system_prompt
    )
)

print(response.text)