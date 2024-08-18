from gtts import gTTS
import os
from config import Config

def generate(text, language):
    try:
        tts = gTTS(text=text, lang=language)
        output_path = os.path.join(Config.OUTPUT_FOLDER, "dubbed_audio.mp3")
        tts.save(output_path)
        return output_path
    except Exception as e:
        print(f"Text-to-speech error: {e}")
        return None