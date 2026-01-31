import os
from engine.speak import speak
from engine.listen import listen
from engine.brain import generate_response
from engine.memory import init_db, get_memory, update_memory
from engine.visuals import refresh_ui
from skills.system_skills import get_battery_status, set_volume, search_youtube
from skills.code_assistance import read_project_file
from skills.roblox_launcher import launch_roblox

def startup():
    init_db()
    refresh_ui()
    user_name = get_memory("user_name")
    if user_name:
        speak(f"Welcome back, {user_name}. Coding environment ready.")
    else:
        speak("Systems online. What shall I call you, Sir?")
        name = listen()
        if name:
            update_memory("user_name", name)
            speak(f"Initialized for {name}.")

if __name__ == "__main__":
    startup()

    WAKE_WORD = "jarvis"
    
    while True:
        query = listen()
        if WAKE_WORD in query:
            speak("Ready.")
            command = listen()
            if not command: continue

            # --- NEW: SYSTEM OVERVIEW ---
            if "what can you do" in command or "commands" in command:
                help_text = (
                    "I can manage your system, Sir. Currently: "
                    "I can check battery levels, control volume, launch Roblox, and search YouTube. "
                    "For development, I can scan your local files for errors and generate professional code."
                )
                speak(help_text)

            # --- NEW: LEAD ENGINEER MODE (AUTO-DEBUG) ---
            elif "debug" in command:
                speak("Analyzing the current directory for architectural flaws...")
                # Add logic to scan common files
                content = read_project_file("main.py")
                prompt = f"Act as a Senior Lead Engineer. Find potential bugs or optimization points in this code: \n{content}"
                speak(generate_response(prompt))

            # --- CODING SKILL ---
            if "scan" in command and "code" in command:
                file_to_scan = "main.py" # You can expand this to listen for the filename
                content = read_project_file(file_to_scan)
                speak(f"I've read {file_to_scan}. What is your coding question?")
                question = listen()
                prompt = f"Analyze this code:\n{content}\n\nTask: {question}"
                speak(generate_response(prompt))

            # --- SYSTEM SKILLS ---
            elif "battery" in command:
                speak(get_battery_status())
            elif "youtube" in command:
                term = command.replace("youtube", "").strip()
                speak(search_youtube(term))
            elif "open roblox" in command:
                status = launch_roblox()
                speak(status)
            elif any(word in command for word in ["stop", "exit", "shutdown"]):
                speak("Understood. Jarvis offline.")
                break
            else:
                speak(generate_response(command))