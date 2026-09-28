import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from scraper import fetch_website_contents

load_dotenv(override=True)
api_key = os.getenv("GEMINI_API_KEY")

