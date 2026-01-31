# TODO: Add 'Mute' and 'Unmute' specific commands
# TODO: Implement brightness control for the laptop screen

import psutil
import webbrowser
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

def get_battery_status():
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugged = "plugged in" if battery.power_plugged else "discharging"
    return f"Sir, the battery is at {percent} percent and is currently {plugged}."

def set_volume(level):
    """Sets system volume (0 to 100)."""
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    
    # Pycaw uses a range of -65.25 to 0.0 (0.0 is max volume)
    # This formula converts 0-100 to the correct decibel range
    volume.SetMasterVolumeLevelScalar(level / 100, None)
    return f"System volume adjusted to {level} percent."

def search_youtube(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)
    return f"Searching YouTube for {query}."