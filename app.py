import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import os
import yfinance as yf
import pyjokes
import pyaudio
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#Listen to our microphone and return the audio as text using google

def transform():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="en")
        return text

def response(text):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=text
    )
    return response.text
        
def speaking(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def query_day():
    day = datetime.date.today()
    print(day)

speaking('Hello Aryan, How can I Help You?')
query=transform()
answer = response(query)
speaking(answer)
query_day()

