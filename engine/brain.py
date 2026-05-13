# TODO: Implement chat history so Jarvis remembers context
# TODO: Add specific 'System Instructions' for a more cynical Stark-era personality

import google.generativeai as genai
import os
from dotenv import load_dotenv
from engine.memory import get_all_memory

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(prompt, free_speech=False):
    """Generates a response using Gemini; supports a freer style when `free_speech` is True.

    Falls back to a concise local reply if the remote API fails.
    """
    try:
        # Retrieve long-term memory to provide context
        memories = get_all_memory()
        memory_context = ""
        if memories:
            memory_context = "Relevant User Context/Memory:\n" + "\n".join([f"- {k}: {v}" for k, v in memories.items()])

        model = genai.GenerativeModel('gemini-1.5-flash')

        base_instruction = (
            "You are JARVIS, the personal assistant to a Lead Engineer. "
            "Personality: sophisticated, efficient, slightly witty. "
            "Expertise: software architecture, Python, and debugging. "
            f"\n{memory_context}"
        )

        if free_speech or os.getenv("ALLOW_FREE_SPEECH", "1") == "1":
            tone = (
                "You are allowed to be candid and expressive while remaining non-harmful. "
                "Favor clarity and brevity. Use occasional wit and natural phrasing."
            )
        else:
            tone = "Be helpful, concise and adhere to safety constraints."

        system_instruction = f"{base_instruction} {tone}"

        full_prompt = f"{system_instruction}\n\nUser: {prompt}"

        # Use generation_config for temperature and other settings
        generation_config = genai.types.GenerationConfig(
            temperature=0.2,
            max_output_tokens=150, # Keep it brief for voice
        )

        response = model.generate_content(
            full_prompt,
            generation_config=generation_config
        )
        
        # Different SDK versions may use .text or candidates
        if hasattr(response, 'text') and response.text:
            return response.text
        if hasattr(response, 'candidates') and response.candidates:
            return response.candidates[0].content
        # Last resort
        return str(response)

    except Exception as e:
        # Lightweight local fallback to keep responsiveness
        safe_reply = "I'm having trouble reaching the model; give me a moment and try again."
        try:
            # Provide a basic heuristic reply for simple requests
            if any(k in prompt.lower() for k in ("what is", "how to", "explain", "define")):
                return "I can help explain that — please ask a specific question and I'll answer concisely."
        except Exception:
            pass
        return f"{safe_reply} (error: {e})"