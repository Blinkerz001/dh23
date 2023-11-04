from gtts import gTTS
import os
import time
import playsound
import speech_recognition
# from io import BytesIO
from pydub import AudioSegment #changes speed of text 
#identify object usiing openCV, then play the identified object.

file = open("draft.txt", "r").read().replace("\n", " ")

def speak(text):
    tts = gTTS(text = text, lang = "en", tld="co.uk")
    file = "Object.mp3"
    tts.save(file)
    playsound.playsound(file)