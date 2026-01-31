# TODO: Add specific GameID support to launch into a direct server
# TODO: Add Roblox Studio launcher support

import os
import subprocess

def launch_roblox():
    """Locates the latest Roblox player and executes it."""
    # Roblox typically installs in the local AppData folder
    base_path = os.path.join(os.environ['LOCALAPPDATA'], "Roblox", "Versions")
    
    if not os.path.exists(base_path):
        return "Sir, it appears Roblox is not installed on this system."

    # Scan the Versions folder for the executable
    for root, dirs, files in os.walk(base_path):
        if "RobloxPlayerBeta.exe" in files:
            exe_path = os.path.join(root, "RobloxPlayerBeta.exe")
            try:
                subprocess.Popen(exe_path)
                return "Launching Roblox now, Sir. Enjoy your session."
            except Exception as e:
                return f"I encountered an error while trying to start the engine: {e}"
                
    return "I found the folder, but the executable is missing. Re-installation may be required."