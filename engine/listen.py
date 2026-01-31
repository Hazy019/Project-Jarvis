# TODO: Implement background noise cancellation
# TODO: Add local/offline recognition for basic commands

import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Add this line to calibrate for background noise
        r.adjust_for_ambient_noise(source, duration=1) 
        print("Listening...")
        r.pause_threshold = 1 # Wait 1 second of silence before stopping
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        return query.lower()
    except:
        return ""