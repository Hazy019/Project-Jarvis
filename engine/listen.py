import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    # Adjusting sensitivity
    r.dynamic_energy_threshold = True 
    
    with sr.Microphone() as source:
        print("SYSTEM: Calibrating...")
        # Reduce duration for faster response
        r.adjust_for_ambient_noise(source, duration=0.8) 
        
        print("Listening...")
        # Lower threshold means he waits less time after you stop talking
        r.pause_threshold = 0.6 
        
        # phrase_time_limit=5 means he WILL stop after 5 seconds no matter what
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            return ""

    try:
        print("SYSTEM: Initializing recognition...")
        query = r.recognize_google(audio, language='en-in')
        print(f"USER: {query}")
        return query.lower()
    except:
        return ""