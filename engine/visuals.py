# TODO: Add logic to change skin colors based on Jarvis's 'mood'
# TODO: Create a custom skin that displays Jarvis's current status text

import subprocess
import os

# Standard path for Rainmeter
RAINMETER_PATH = r"C:\Program Files\Rainmeter\Rainmeter.exe"

def rainmeter_command(bang):
    """Sends a specific Bang command to Rainmeter."""
    if os.path.exists(RAINMETER_PATH):
        subprocess.call([RAINMETER_PATH, bang])

def refresh_ui():
    """Refreshes all active skins."""
    rainmeter_command("!RefreshApp")

def toggle_player(show=True):
    """Shows or hides the Mond Music Player."""
    state = "!ShowFade" if show else "!HideFade"
    rainmeter_command(f"{state} \"Mond\\Player\"")