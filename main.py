import os
from engine.speak import speak
from engine.listen import listen
from engine.brain import generate_response
from engine.memory import init_db, get_memory, update_memory
from engine.visuals import refresh_ui, toggle_player
from skills.system_skills import get_battery_status, set_volume, search_youtube
from skills.roblox_launcher import launch_roblox 
from skills.code_assistance import read_project_file
from skills.windows_control import execute_windows_command
from skills.workspace_protocols import initiate_protocol
import sqlite3

def delete_user_name():
    """Clears the user_name from the database."""
    conn = sqlite3.connect('jarvis_memory.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM memory WHERE key = 'user_name'")
    conn.commit()
    conn.close()
    return "Data wiped. I have no memory of your name, Sir."

def show_skills():
    skills_list = (
        "I can manage your system: check battery, set volume, and search YouTube. "
        "I can assist in coding: scan your project files or write functions. "
        "I can control Windows: minimize windows or scroll. "
        "And I can launch Roblox for you. Just ask."
    )
    speak(skills_list)
    print("\n--- JARVIS CAPABILITIES ---\n1. ROBLOX: 'Open Roblox'\n2. CODING: 'Scan code'\n3. SYSTEM: 'Battery', 'Volume to X'\n4. WEB: 'YouTube [Topic]'\n5. WINDOWS: 'Minimize', 'Scroll down'\n")

def verify_user():
    """Asks for confirmation and updates name if denied."""
    user_name = get_memory("user_name") or "Sir"
    speak(f"Is that really you, {user_name}? Please confirm with a yes or no.")
    
    confirmation = listen().lower()
    
    if "yes" in confirmation or "yeah" in confirmation:
        speak(f"Access granted. Welcome back, {user_name}.")
        return True
        
    elif "no" in confirmation or "not" in confirmation:
        speak("I apologize. My records must be outdated. What is your name, then?")
        new_name = listen()
        
        if new_name and new_name != "none":
            # Save to SQLite so he remembers forever
            update_memory("user_name", new_name) 
            speak(f"Protocol updated. I shall call you {new_name} from now on.")
            return True
        else:
            speak("I didn't catch that. Security protocol active. Action aborted.")
            return False
            
    else:
        speak("Unauthorized response. Aborting task for safety.")
        return False
    
def startup():
    """Initializes the system and greets the user."""
    init_db()
    refresh_ui()
    user_name = get_memory("user_name")
    
    if user_name:
        speak(f"System online. Welcome back, {user_name}.")
    else:
        speak("System online. I don't believe we've met. What is your name?")
        name = listen()
        if name and name != "none":
            update_memory("user_name", name)
            speak(f"Pleasure to meet you, {name}.")
        else:
            speak("I didn't catch that. I'll just call you Sir for now.")

if __name__ == "__main__":
    startup()
    
    WAKE_WORD = "jarvis"
    FOLLOW_UP_MODE = False
    
    while True:
        query = listen()
        
        if not query:
            FOLLOW_UP_MODE = False # Reset if no speech detected
            continue

        # Check if we should respond
        should_respond = (WAKE_WORD in query) or FOLLOW_UP_MODE
        
        if should_respond:
            command = query.replace(WAKE_WORD, "").strip()
            
            # If they just said the wake word, prompt for command
            if not command and not FOLLOW_UP_MODE:
                speak("I'm Ready.")
                command = listen()
                if not command:
                    FOLLOW_UP_MODE = False
                    continue
            
            if not command:
                continue

            # --- SYSTEM: EXIT/SHUTDOWN ---
            if any(word in command for word in ["shutdown", "exit", "close system"]):
                if verify_user():
                    speak("Powering down all systems. Goodbye.")
                    break
                FOLLOW_UP_MODE = True
                continue

            # --- SKILLS: WINDOWS CONTROL ---
            win_response = execute_windows_command(command)
            if win_response:
                speak(win_response)
                FOLLOW_UP_MODE = True
                continue

            # --- SKILLS: ROBLOX ---
            if "roblox" in command:
                toggle_player(False)
                speak(launch_roblox())
                FOLLOW_UP_MODE = True

            # --- SKILLS: WORKSPACE PROTOCOLS ---
            elif "protocol" in command or "initiate" in command:
                protocol_name = command.replace("protocol", "").replace("initiate", "").strip()
                speak(initiate_protocol(protocol_name))
                FOLLOW_UP_MODE = True

            # --- SKILLS: YOUTUBE ---
            elif "youtube" in command:
                topic = command.replace("youtube", "").strip()
                speak(search_youtube(topic))
                FOLLOW_UP_MODE = True

            # --- SYSTEM: MEMORY WIPE ---
            elif "forget my name" in command or "drop my name" in command:
                speak("Are you sure you want me to wipe our introduction?")
                if verify_user():
                    result = delete_user_name()
                    speak(result)
                FOLLOW_UP_MODE = True

            # --- SYSTEM: HELP ---
            elif "what can you do" in command or "commands" in command:
                show_skills()
                FOLLOW_UP_MODE = True
            
            # --- SYSTEM: IDENTITY CORRECTION ---
            elif any(word in command for word in ["wrong name", "change my name", "not my name", "not zian"]):
                speak("I apologize, Sir. What is the correct way to address you?")
                new_name = listen()
                if new_name and new_name != "none":
                    update_memory("user_name", new_name)
                    speak(f"Correction logged. I shall refer to you as {new_name} from now on.")
                FOLLOW_UP_MODE = True

            # --- SKILLS: CODING ---
            elif "scan" in command and "code" in command:
                content = read_project_file()
                speak("Code analysis complete. What is your question?")
                q = listen()
                speak(generate_response(f"Code Context: {content}\nQuestion: {q}", free_speech=False))
                FOLLOW_UP_MODE = True

            # --- SKILLS: SYSTEM MONITORING ---
            elif "battery" in command:
                speak(get_battery_status())
                FOLLOW_UP_MODE = True
            elif "volume to" in command:
                try:
                    level = int(''.join(filter(str.isdigit, command)))
                    speak(set_volume(level))
                except:
                    speak("I didn't catch the volume level.")
                FOLLOW_UP_MODE = True
            elif "minimize" in command:
                import pyautogui
                pyautogui.hotkey('win', 'd')
                speak("Done.")
                FOLLOW_UP_MODE = True
            
            # --- BRAIN: GENERAL CHAT ---
            else:
                response = generate_response(command, free_speech=True)
                speak(response)
                FOLLOW_UP_MODE = True
        else:
            # Not addressed to Jarvis and not in follow-up mode
            FOLLOW_UP_MODE = False