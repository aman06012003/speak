from win32com.client import Dispatch

def speak(str):
    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)

name = input('Whats your name: ')
speak(f'nice to meet you {name}')

