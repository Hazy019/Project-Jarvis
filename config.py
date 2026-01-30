# TODO: Add more configurations like 'User Name' in Phase 5
import os
from dotenv import load_dotenv

# Load the keys from the .env file
load_dotenv()

# This makes the key available to the rest of your app
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")