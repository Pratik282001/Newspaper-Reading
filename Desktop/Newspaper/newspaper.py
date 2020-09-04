from win32com.client import Dispatch
import time
import requests
import json
def speak(str):
    time.sleep(1)
    speak= Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    # in place API_KEY you can use your own api keys from website newsapi.org ;)
    # one example is given below
    response = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=c546cd7dd0e4454d81e3d3b684eff6bf")
    # response = requests.get("http://newsapi.org/v2/everything?q=apple&from=2020-09-03&to=2020-09-03&sortBy=popularity&apiKey=API_KEY")
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