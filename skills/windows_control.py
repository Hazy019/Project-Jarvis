# TODO: Add voice-to-coordinates mapping for more precise clicking
import pyautogui
import os

def execute_windows_command(command):
    """Handles OS-level interactions via PyAutoGUI."""
    command = command.lower()
    # Distance to move per command (in pixels)
    step = 100 

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
        return "Minimizing all windows, Sir."
    
    elif "scroll down" in command:
        pyautogui.scroll(-500)
        return "Scrolling down."
        
    elif "scroll up" in command:
        pyautogui.scroll(500)
        return "Scrolling up."
        
    elif "click" in command:
        pyautogui.click()
        return "Clicked."

    elif "double click" in command:
        pyautogui.doubleClick()
        return "Executed double click."

    elif "open" in command:
        app = command.replace("open", "").strip()
        pyautogui.press('win')
        pyautogui.write(app)
        pyautogui.press('enter')
        return f"Attempting to launch {app}."

    return None