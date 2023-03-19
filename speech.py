from gtts import gTTS
import os

def speak(audio):
    tts=gTTS(text=audio,lang="en")
    tts.save("audio1.mp3")
    os.system("mpg321 audio1.mp3")
    
speak("heyy yo")