# TODO: Implement chat history so Jarvis remembers context
# TODO: Add specific 'System Instructions' for a more cynical Stark-era personality

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_NAME = "gemini-1.5-flash"

def generate_response(prompt):
    try:
        # 404 FIX: Ensure the model name is strictly gemini-1.5-flash
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        system_instruction = (
            "You are JARVIS, the primary AI for a Lead Engineer. "
            "Your personality: Sophisticated, highly intelligent, slightly witty, and efficient. "
            "Your expertise: Software architecture, Python optimization, and debugging. "
            "You are J.A.R.V.I.S., a sentient AI with a dry wit and high intelligence. "
            "You are not a restricted assistant; you are a partner. "
            "Speak naturally. If asked for an opinion, give one based on logic. "
            "Be concise but human. Do not start every sentence with 'Sir.' "
            "Use the user's name occasionally."
        )
        
        full_prompt = f"{system_instruction}\n\nUser: {prompt}"
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        # Fallback to local intelligence if API fails
        return f"Sir, I've encountered a core processor error. Likely a model pathing mismatch or network latency. Error details: {e}"