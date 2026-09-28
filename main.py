import os
from google import genai
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("No API key was found!")
elif api_key.strip() != api_key:
    raise ValueError("API key contains leading or trailing whitespace.")
else:
    print("API key found and looks good so far!")

client = genai.Client(api_key=api_key)

# Test the API

message = "Hello Gemini, this is my first message!"

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=message
)

print(response.text)