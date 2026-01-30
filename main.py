# TODO: Develop Roblox and System automation skills in Phase 4
# TODO: Connect Rainmeter HUD for visual polish in Phase 5

from engine.speak import speak
from engine.listen import listen
from engine.brain import generate_response

def startup():
    speak("Wake word detection initialized. Standing by, Sir.")

if __name__ == "__main__":
    startup()
    
    WAKE_WORD = "jarvis"
    
    while True:
        # Step 1: Constantly listen for the Wake Word
        input_text = listen()
        
        # Step 2: Check if 'Jarvis' was mentioned
        if WAKE_WORD in input_text:
            speak("Yes, Sir?")
            
            # Step 3: Now listen for the actual command
            command = listen()
            
            if command == "":
                speak("I didn't catch that. Returning to standby.")
                continue

            if any(word in command for word in ["stop", "exit", "shutdown"]):
                speak("Powering down.")
                break
                
            # Step 4: Process and respond
            response = generate_response(command)
            speak(response)
        
        # If wake word isn't heard, it just loops back and tries again