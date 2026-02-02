# TODO: Add voice-to-coordinates mapping for more precise clicking
import time
import pyautogui
import os
import re
import webbrowser


def execute_windows_command(command):
    """Handles OS-level interactions via PyAutoGUI and simple web searches."""
    command = command.lower()
    # Distance to move per command (in pixels)
    step = 100

    # Simple mapping for common app names to speed up 'open' command
    known_apps = {
        'brave': 'brave',
        'firefox': 'firefox',
        'notepad': 'notepad',
        'calculator': 'calc',
        'explorer': 'explorer',
           'chrome': 'chrome',
           'brave': 'brave',
           'brave browser': 'brave',
           'firefox': 'firefox',
           'edge': 'microsoftedge',
           'notepad': 'notepad',
           'calculator': 'calc',
           'explorer': 'explorer',
           'vscode': 'code',
           'code': 'code',
           'spotify': 'spotify'
    }

    if "open" in command:
        app = command.replace("open", "").strip()
        exe = known_apps.get(app, app)
        pyautogui.press('win')
        time.sleep(0.25)  # faster startup
        pyautogui.write(exe)
        time.sleep(0.25)
        pyautogui.press('enter')
        return f"Opening {app}."

    if "move" in command:
        if "up" in command:
            pyautogui.moveRel(0, -step)
            return "Nudging cursor up."
        elif "down" in command:
            pyautogui.moveRel(0, step)
            return "Nudging cursor down."
        elif "left" in command:
            pyautogui.moveRel(-step, 0)
            return "Nudging cursor left."
        elif "right" in command:
            pyautogui.moveRel(step, 0)
            return "Nudging cursor right."

    if "minimize" in command:
        pyautogui.hotkey('win', 'd')
        return "Minimizing all windows."

    if "scroll" in command:
        # parse optional magnitude
        amt_matches = re.findall(r"(-?\d+)", command)
        amt = int(amt_matches[0]) if amt_matches else 500
        if "down" in command:
            pyautogui.scroll(-abs(amt))
            return "Scrolling down."
        else:
            pyautogui.scroll(abs(amt))
            return "Scrolling up." if "up" in command else "Scrolling."

    # Double click should be checked before single click
    if "double click" in command or "double-click" in command:
        # optional coordinates: 'double click at 100 200'
        coords = re.findall(r"(\d{1,4})", command)
        if len(coords) >= 2:
            x, y = int(coords[0]), int(coords[1])
            pyautogui.doubleClick(x=x, y=y)
            return f"Double clicked at {x},{y}."
        pyautogui.doubleClick()
        return "Executed double click."

    if "click" in command:
        coords = re.findall(r"(\d{1,4})", command)
        if len(coords) >= 2:
            x, y = int(coords[0]), int(coords[1])
            pyautogui.click(x=x, y=y)
            return f"Clicked at {x},{y}."
        pyautogui.click()
        return "Clicked."

    if "search" in command and "youtube" not in command:
        # 'search cats' -> google search
        query = command.replace('search', '').strip()
        if query:
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
            return f"Searching the web for {query}."

    return None