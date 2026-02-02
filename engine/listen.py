import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    # Adjusting sensitivity
    r.dynamic_energy_threshold = True 
    
    with sr.Microphone() as source:
        print("SYSTEM: Calibrating...")
        # Reduce duration for faster response but keep adaptive threshold
        r.adjust_for_ambient_noise(source, duration=0.4)

        print("Listening...")
        # Reduce pause threshold so recognizer stops listening sooner after speech
        r.pause_threshold = 0.45
        # Shorten non-speaking detection
        r.non_speaking_duration = 0.2
        # Optional: set a baseline energy to avoid large dynamic swings
        try:
            r.energy_threshold = 300
        except Exception:
            pass

        # phrase_time_limit and timeout tuned for responsiveness
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=4)
        except sr.WaitTimeoutError:
            return ""

    try:
        print("SYSTEM: Initializing recognition...")
        query = r.recognize_google(audio, language='en-in')
        print(f"USER: {query}")
        return query.lower()
    except:
        return ""