from idlelib import search

import win32com.client
import speech_recognition as sr
import pyttsx3
import os
import subprocess as sp
import webbrowser
import openai
import datetime
import keyboard
import imdb
import wolframalpha


from conv import random_text
from random import choice
import pywhatkit as kit
from decouple import config
from online import find_my_ip,search_on_wikipedia ,search_on_google ,youtube_vedio,send_email,get_news,weather_forcast
# import webdriver for openinstagram




speaker =win32com.client.Dispatch("SAPI.SpVoice")

#while 1:
 #   print(" enter command / comments ")
  #  s= input()
   # speaker.Speak(s)

engine = pyttsx3.init()





listening = False
def say(text):
    engine.say(text)
    engine.runAndWait()

# def greet_me():
#         hour = datetime.now().hour
#         if (hour >= 6) and (hour < 12):
#             say("Good morning")
#         elif (hour >= 12) and (hour <= 16):
#             say("Good afternoon")
#         elif (hour >= 16) and (hour < 19):
#             say("Good evening" )
#         say("I am your voice assistant. How may i assist you? ")
#

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=0.6
        audio =r.listen(source)
        try:
            print("recognizing..")
            query =r.recognize_google(audio,language="en-in")
            print(f"user said :{query}")
            if not 'stop' in query or 'exit' in query:
                say(choice(random_text))



            if  'stop'in query or 'exit' in query:
                say(" okay  thank you sir  see you soon have a good day")
                exit()

                # else:
                #     hour = datetime.now().hour
                #     if hour >= 21 and hour < 6:
                #         say("Good night sir,take care!")
                #     else:
                #         say("Have a good day sir!")
                #     exit()


            return query
        except Exception as e:
          return " some error"




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')
    say(" hello  sir  , i am your voice assistant what can i do for you ")
    while True:
     print ("listening ...")
     query =takeCommand()
     sites = [["whatsapp", "https://web.whatsapp.com"],["application","http://127.0.0.1:5501/weather.html"],["youtube","https://www.youtube.com/"]]
     for site in sites:
         if f"Open {site[0]}".lower() in query.lower():
             say(f"Opening {site[0]} sir...")
             webbrowser.open(site[1])
    # if "Open Youtube".lower() in query.lower():
     #      # say(" opening youtube sir...")
      #      webbrowser.open("https://www.youtube.com/")


         if "open music" in query:
             musicPath=r"C:\Users\ASUS\Downloads\Ram Ji Ringtone Download Mp3 Pagalworld - MobCup.Com.Co.mp3"
             os.startfile(musicPath)

         if "time" in query:
             # musicPath = r"C:\Users\ASUS\Downloads\Ram Ji Ringtone Download Mp3 Pagalworld - MobCup.Com.Co.mp3"
             #strfTime = datetime.datetime.now().strftime("%H:%M:%S")
             #say(f"sir the time is {strfTime}")

             # Get current time
             current_time = datetime.datetime.now()

             # Format the time as HH:MM:SS (24-hour format)
             strfTime = current_time.strftime("%H:%M:%S")
             say(f"sir the time is {strfTime}")

             print("Current time:", strfTime)

         #if "open vs code".lower() in query.lower():
          #   os.system(f"C:\\Users\\ASUS\\Downloads\\VSCodeUserSetup-x64-1.84.0.exe")
         if "open command prompt" in query:
            say(" opening command prompt sir..")
            os.system('start cmd')

         elif "open camera" in query:
             say(" opening camera sir..")
             sp.run('start microsoft.windows.camera:',shell=True)

         # elif "ip address" in query:
         #     ip_address=find_my_ip()
         #     say(
         #         f"your ip address is{ip_address}"
         #     )
         #     print(f" your ip address is :- {ip_address}")

         elif "open Youtube" in query:
             say("what do you want to play on youtube sir.")
             video=takeCommand().lower()
             youtube_vedio(video)

         # elif "open Google" in query:
         #         say("what do you want to search on  google sir.")
         #         print("what do you want to search on  google sir.")
         #         query = takeCommand().lower()
         #         results = search_on_google(search)
         #         say(f"according to wikipedia ,{results}")
         #         say(" i also print statement on terminal ")
         #         print(results)
         #


         #
         elif "open Google" in query:
             say("what do you want to search on  google sir.")
             print("what do you want to search on  google sir.")
             query = takeCommand().lower()
             search_on_google(query)


         elif "open Wikipedia" in query:
             say("what do you want to search on  wikipedia sir.")
             search = takeCommand().lower()
             results =search_on_wikipedia(search)
             say(f"according to wikipedia ,{results}")
             say(" i also print statement on terminal ")
             print(results)



         elif "give some news" in query:
             say("i am reading a latest headlines of today ")
             news = get_news()
             print(news)
             say(get_news())
             say(" i am print it on screen also")

             exit()

             # search = takeCommand().lower()
             #
             # say(f"according to wikipedia ,{results}")
             # say(" i also print statement on terminal ")
             # print(results)

         elif 'weather' in query:
             ip_address = find_my_ip()
             say("tell me the name of your city")

             query = takeCommand().lower()
             say(f"Getting weather report for your city {query}")
             weather, temp, feels_like = weather_forcast(query)
             say(f"The current temperature is {temp}, but it feels like {feels_like}")
             say(f"Also, the weather report talks about {weather}")
             say("For your convenience, I am printing it on the screen sir.")
             print(f"Description: {weather}\nTemperature: {temp}\nFeels like: {feels_like}")
             exit()




         elif "movie" in query:
             movies_db = imdb.IMDb()#it contents all movie web series T.V contents
             say("Please tell me the movie name:")
             text = takeCommand()
             movies = movies_db.search_movie(text)
             say("searching for" + text)
             say("I found these")

             for movie in movies:
                 title = movie["title"]
                 year = movie["year"]
                 say(f"{title}-{year}")
                 info = movie.getID()
                 movie_info = movies_db.get_movie(info)
                 rating = movie_info["rating"]
                 cast = movie_info["cast"]
                 actor = cast[0:5]
                 plot = movie_info.get('plot outline', 'plot summary not available')
                 say(f"{title} was released in {year} has imdb ratings of {rating}.It has a cast of {actor}. "
                       f"The plot summary of movie is {plot}")

                 print(f"{title} was released in {year} has imdb ratings of {rating}.\n It has a cast of {actor}. \n"
                       f"The plot summary of movie is {plot}")


    #
    #
    #          elif  "send email" in query:
    #           say("please, entre email address in the terminal")
    #          print("please, entre email address in the terminal")
    #          receiver_add=input("Email address :-")
    #          subject=takeCommand().capitalize()
    #          say("what is the message send  on given email")
    # message =takeCommand().capitalize()
    #
    #     if send_email(receiver_add,subject,message):
    #                  say("i have sent the emil sir ")
    #              print("i have sent the emil sir")
    #           else:
    #         say("something went wrong sir ,check the error and try again")
    #
    #

  #  say(query)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
