from win32com.client import Dispatch
import time
import requests
import json
def speak(str):
    time.sleep(1)
    speak= Dispatch("SAPI.SpVoice")

    speak.Speak(str)

if __name__ == '__main__':
    response = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=c546cd7dd0e4454d81e3d3b684eff6bf")
    text = response.text
    my_json = json.loads(text)
    speak("    today's top headlines are")
    for i in range(0, 11):
        print(my_json['articles'][i]['title'])
        speak(my_json['articles'][i]['title'])
        print(my_json['articles'][i]['description'])
        speak(my_json['articles'][i]['description'])
        print()
    speak("  these were some top headlines")