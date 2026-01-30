# TODO: Add support for different voice personas
# TODO: Implement a queue system for long sentences

import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    
    # Adjusting properties for a more 'Stark-like' pace
    engine.setProperty('rate', 185)
    engine.setProperty('volume', 1.0)
    
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()