# TODO: Implement background noise cancellation
# TODO: Add local/offline recognition for basic commands

import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Dynamic energy threshold helps Jarvis adjust to room noise
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=5)

    try:
        query = r.recognize_google(audio, language='en-in')
        return query.lower()
    except:
        return ""