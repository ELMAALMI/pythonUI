import speech_recognition as sr
import webbrowser
import time
import os 
import playsound
from gtts import gTTS
import random

r = sr.Recognizer()
def alexis_speak(audio_string):
    tts = gTTS(text=audio_string,lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError : 
            alexis_speak('yes rabie is gay')
        except sr.RequestError :
            alexis_speak('yes rabie is gay')
        return voice_data
def resond(voice_data):
    if "what's your name" in voice_data:
        alexis_speak('my name is boot')
    if "search" in voice_data:
        alexis_speak ("what do you want to search : ")
        search = record_audio()
        print(search)
        url = 'https://www.google.com/search?q='+search
        webbrowser.get().open(url)
    if "exit" in voice_data:
        alexis_speak ("goodbay")
        exit()
time.sleep(1)
alexis_speak('how i can help you : ')
while 1 :
    voice_data = record_audio()
    resond(voice_data)