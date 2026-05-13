import os
import subprocess
import webbrowser
from skills.system_skills import set_volume

def initiate_protocol(name):
    name = name.lower()
    
    if "coding" in name or "alpha" in name:
        # Protocol Alpha: Coding
        # Change these paths to actual paths on your system if necessary
        # We use 'code' command if it's in PATH, otherwise common paths
        try:
            subprocess.Popen(['code'], shell=True) # Open VS Code
        except Exception:
            pass
            
        webbrowser.open("https://github.com")
        webbrowser.open("https://stackoverflow.com")
        set_volume(30)
        return "Initiating Protocol Alpha. VS Code and documentation are ready. Volume set for focus."

    elif "gaming" in name or "omega" in name:
        # Protocol Omega: Gaming
        # Roblox is handled by a separate skill, but we can call it here or just open the browser
        webbrowser.open("https://www.roblox.com/home")
        set_volume(80)
        return "Initiating Protocol Omega. Game launcher ready. Volume maximized for immersion."

    else:
        return f"Sir, I don't have a record for a protocol named {name}."
