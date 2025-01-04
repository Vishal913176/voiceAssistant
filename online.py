import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

EMAIL="vishal9131@gmail.com"
PASSWORD="vishal9865"



def find_my_ip():
    ip_address=requests.get('https://api.ipify.org?format=json').json()
    return ip_address["ip"]

def search_on_wikipedia(query):
    results = wikipedia.summary(query,sentence=2)
    return results

def search_on_google(query):
    kit.search(query)
    # results = search_on_google().summary(query, sentence=2)
    # return results



def youtube_vedio(video):
    kit.playonyt(video)

def get_news():
    news_headline=[]
    result=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey"
                        f"=327e126108934838a8c9e40c945657bd").json()
    articles=result["articles"]
    for article  in articles:
        news_headline.append(article["title"])
    return news_headline[:6]#month


def weather_forcast(city):
    res =requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9938be7a20846d8c7add21047038fa20").json()
    # res = requests.getget(f"https://api.openweathermap.org/data/2.5/weather?q={city }&appid={API key}").json()
    weather = res["weather"][0]["main"]
    temp = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temp}°C", f"{feels_like}°C"


def send_email(receiver_add,subject,message):
    try:
        email=EmailMessage()
        email['to'] =receiver_add
        email['subject']= subject
        email['from']= EMAIL

        email.set_content(message)
        s=smtplib.SMTP("smtp.gmail.com",587)
        s.login(EMAIL,PASSWORD)
        s.send_message(email)
        s.close()
        return True

    except Exception as e:
      print(e)
      return False




