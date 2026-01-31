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
            "Rules: \n"
            "1. Be concise (Sir is busy). \n"
            "2. When writing code, provide production-ready, clean Python code. \n"
            "3. If asked 'What can you do?', list your integrated skills (Roblox, System Control, YouTube, Code Scanning). \n"
            "4. If a user command looks like a coding error, diagnose it immediately."
        )
        
        full_prompt = f"{system_instruction}\n\nUser: {prompt}"
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        # Fallback to local intelligence if API fails
        return f"Sir, I've encountered a core processor error. Likely a model pathing mismatch or network latency. Error details: {e}"