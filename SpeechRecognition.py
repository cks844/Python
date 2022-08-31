import speech_recognition as sr
AUDIO_FILE=("cks.wav")#use audio file as source
r=sr.Recognizer() #intitialise the recogniser

with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source) #to read the audio file
try:
    print("Audio file contains:"+ r.recognize_google(audio))
except sr.UnknownValueError: #incase if it fails to understand,exception occurrs
    print("Could not understand the audio")
except sr.RequestError:
    print("Could not get the data")
