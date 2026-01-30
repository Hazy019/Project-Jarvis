# TODO: Implement chat history so Jarvis remembers context
# TODO: Add specific 'System Instructions' for a more cynical Stark-era personality

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

def generate_response(user_input):
    """Processes input through Gemini 1.5 Flash."""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # System prompt to keep him in character
        personality = "You are JARVIS, the highly advanced AI from Iron Man. Be concise, witty, and helpful."
        full_prompt = f"{personality}\nUser: {user_input}"
        
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        print(f"System Error: {e}")
        return "Sir, my connection to the cloud servers seems to be fluctuating."