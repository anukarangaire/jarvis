
# Windows Based
# Advantages = Fast , Offline.
# Disadvantages =  OverSpeak , Less Voices.

import pyttsx3

def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate',170)
    print(f"AI : {Text}.")
    engine.say(Text)
    engine.runAndWait()

Speak("")