import asyncio
import edge_tts
import pygame
import os

def speak(text):
    """Generates high-fidelity speech using Edge-TTS and plays it via pygame."""
    print(f"Jarvis: {text}")
    
    # en-GB-RyanNeural is a sophisticated, professional British voice
    VOICE = "en-GB-RyanNeural" 
    OUTPUT_FILE = "temp_speech.mp3"
    
    async def generate_audio():
        communicate = edge_tts.Communicate(text, VOICE)
        await communicate.save(OUTPUT_FILE)

    try:
        # Run the async audio generation
        asyncio.run(generate_audio())
        
        # Initialize pygame mixer and play
        pygame.mixer.init()
        pygame.mixer.music.load(OUTPUT_FILE)
        pygame.mixer.music.play()
        
        # Wait for audio to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
        pygame.mixer.music.unload()
        pygame.mixer.quit() # Cleanup to avoid file lock issues
        
    except Exception as e:
        print(f"Speech Error: {e}")
    finally:
        # Clean up the temporary file
        if os.path.exists(OUTPUT_FILE):
            try:
                os.remove(OUTPUT_FILE)
            except Exception:
                pass