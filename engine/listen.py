# pyrefly: ignore [missing-import]
import speech_recognition as sr

# Global recognizer to avoid re-initializing and re-calibrating every time
recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True
recognizer.energy_threshold = 300 
recognizer.pause_threshold = 0.5
recognizer.non_speaking_duration = 0.3

# We will calibrate once on the first call
is_calibrated = False

def listen():
    global is_calibrated
    
    with sr.Microphone() as source:
        if not is_calibrated:
            print("SYSTEM: Calibrating for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            is_calibrated = True
            print("SYSTEM: Calibration complete. Ready.")

        print("Listening...")
        try:
            # Shorter timeout for much snappier response
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            return ""

    try:
        print("SYSTEM: Initializing recognition...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"USER: {query}")
        return query.lower()
    except sr.UnknownValueError:
        # Don't print error for silence/noise to keep terminal clean
        return ""
    except sr.RequestError:
        print("SYSTEM: Speech Service unavailable.")
        return ""
    except Exception:
        return ""