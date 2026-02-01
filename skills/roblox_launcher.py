import os
import subprocess

def launch_roblox():
    """Checks multiple common installation paths for Roblox."""
    # Path 1: Local AppData (Standard)
    # Path 2: Program Files (Newer installs)
    search_paths = [
        os.path.join(os.environ['LOCALAPPDATA'], "Roblox", "Versions"),
        os.path.join(os.environ['ProgramFiles(x86)'], "Roblox", "Versions")
    ]
    
    for base_path in search_paths:
        if os.path.exists(base_path):
            for root, dirs, files in os.walk(base_path):
                if "RobloxPlayerBeta.exe" in files:
                    exe_path = os.path.join(root, "RobloxPlayerBeta.exe")
                    try:
                        # 'start' command via shell is more reliable for game launchers
                        os.startfile(exe_path)
                        return "Launching Roblox Player. Systems optimized for gaming."
                    except Exception as e:
                        return f"Error executing binary: {e}"
                
    return "Sir, I searched the internal archives but Roblox is not installed in the standard directories."