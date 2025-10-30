from Body.Listen import Listen
from Body.Speak import Speak
import os
import keyboard
from time import sleep
import datetime
import webbrowser
from numpy import tile
import requests
from bs4 import BeautifulSoup
import os
import pyautogui
import random
from plyer import notification
import speedtest
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import cv2
import time
from requests import get




print(">> Starting The JARVIS : Wait for some Seconds.")
print(">> Please say [wake up] To Activate Jarvis.")

def alarm(Data):
    timehere = open("Alarmtext.txt","a")
    timehere.write(Data)
    timehere.close()
    os.startfile("alarm.py")
def greetMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 11:
        Speak(f"good morning , its {tt}")
    elif hour >= 12 and hour <= 18:
        Speak(f"good afternoon, its {tt}")
    else:
        Speak(f"good evening, its {tt}")
    Speak("i am jarvis sir. please tell me how may i help you")

if __name__ == "__main__":
    while True:
        Data = Listen().lower()     
        # Data = input("wake: ")  
        if "wake up" in Data or "wakeup" in Data:
            greetMe()

            while True:
                Data = Listen().lower()     
                #Data = input("Query : ")  
        
        
                if "principle of everest english school" in Data or "principal of everest english school" in Data:
                    Speak ("The principle of Everest English School is Bhakta RajBhandari.")
                    exit()
                
                if "jarvis" in Data:
                     Speak("Yes, sir")
                elif "schedule my day" in Data:
                            tasks = [] #Empty list 
                            Speak("Do you want to clear old tasks (Plz Speak YES or NO)")
                            Data = Listen().lower()
                            if "yes" in Data:
                                file = open("tasks.txt","w")
                                file.write(f"")
                                file.close()
                                no_tasks = int(input("Enter the no. of tasks :- "))
                                i = 0
                                for i in range(no_tasks):
                                    tasks.append(input("Enter the task :- "))
                                    file = open("tasks.txt","a")
                                    file.write(f"{i}. {tasks[i]}\n")
                                    file.close()
                            elif "no" in Data:
                                i = 0
                                no_tasks = int(input("Enter the no. of tasks :- "))
                                for i in range(no_tasks):
                                    tasks.append(input("Enter the task :- "))
                                    file = open("schedule.txt","a")
                                    file.write(f"{i}. {tasks[i]}\n")
                                    file.close()
                elif "show my schedule" in Data:
                    open("schedule.txt")
                elif "focus mode" in Data:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                            Speak("Entering the focus mode....")
                            os.startfile("G:\\Jarvis_Final\\jarvis\\FocusMode.py")
                            exit()
                    else:
                            pass
                elif "show my focus" in Data:
                    from FocusGraph import focus_graph
                    focus_graph()
            
                # For Website
                elif "visit" in Data:
                    Nameofweb = Data.replace("visit ","")
                    Link = f"https://www.{Nameofweb}.com"
                    webbrowser.open(Link)
                elif "start " in Data:
                    Nameofweb = Data.replace("start ","")
                    Link = f"https://www.{Nameofweb}.com"
                    webbrowser.open(Link)
                # For softwares
                elif "launch" in Data:
                    import pyautogui
                    Data = Data.replace("open","")
                    Data = Data.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(Data)
                    pyautogui.sleep(2)
                    pyautogui.press("enter") 
                    
                    Nameoftheapp = Data.replace("launch ","")

                    if "chrome" in Nameoftheapp:
                        os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
                elif "open" in Data:
                    import pyautogui
                    Data = Data.replace("open","")
                    Data = Data.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(Data)
                    pyautogui.sleep(2)
                    pyautogui.press("enter") 
                    Nameoftheapp = Data.replace("open ","")

                    if "chrome" in Nameoftheapp:
                        os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
                elif "open adobe reader" in Data:
                            apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
                            os.startfile(apath)
                elif "open command prompt" in Data or "open command prompt." in Data:
                            os.system("start cmd")
                elif "open camera" in Data:
                            cap = cv2.VideoCapture(0)
                            while True:
                                ret, img = cap.read()
                                cv2.imshow('webcam', img)
                                k = cv2.waitKey(50)
                                if k==27:
                                    break;
                            cap.release()
                            cv2.destroyAllWindows()
                elif "play a game" in Data:
                    from game import game_play
                    game_play()
                elif "screenshot" in Data:
                    import pyautogui #pip install pyautogui
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

                elif "click my photo" in Data:
                    import pyautogui
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    Speak("SMILE")
                    Speak("Wait for some moment but don't forget to smile to make your photo amazing")
                    pyautogui.press("enter")
                    pyautogui.press("enter")
                elif "tired" in Data:
                    Speak("You should listen a song when tired,sir.")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=f2AewHdG3ok")
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=qyRrUEInzAs")
                    elif b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=U5syMIJ5JRA")
                    else:
                        pass
                elif "pause" in Data:
                    import pyautogui
                    pyautogui.press("k")
                    Speak("video paused")
                elif "play" in Data:
                    import pyautogui
                    pyautogui.press("k")
                    Speak("video played")
                elif "mute" in Data:
                    pyautogui.press("m")
                    Speak("video muted")
                        
                elif "volume up" in Data:
                    from keyboard import volumeup
                    Speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in Data:
                    from keyboard import volumedown
                    Speak("Turning volume down, sir")
                    volumedown()
                elif "google" in Data:
                    from SearchNow import searchGoogle
                    searchGoogle(Data)
                elif "youtube" in Data:
                    from SearchNow import searchYoutube
                    searchYoutube(Data)
                elif "wikipedia" in Data:
                    from SearchNow import searchWikipedia
                    searchWikipedia(Data)

                elif "calculate" in Data:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    Data = Data.replace("calculate","")
                    Data = Data.replace("jarvis","")
                    Calc(Data)

                elif "temperature" in Data:
                    search = "temperature in bhaktapur"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    Speak(f"current{search} is {temp}")
                elif "weather" in Data:
                    search = "temperature in bhaktapur"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    Speak(f"current{search} is {temp}")

                elif "set an alarm" in Data:
                    print("input time example:- 10 and 10 and 10")
                    Speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    Speak("Done,sir")
                                
                elif "the time" in Data:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    Speak(f"Sir, the time is {strTime}")
                
                elif "remember that" in Data:
                    rememberMessage = Data.replace("remember that","")
                    rememberMessage = Data.replace("jarvis","")
                    Speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in Data:
                    remember = open("Remember.txt","r")
                    Speak("You told me to remember that" + remember.read())

                elif "shutdown system" in Data:
                    Speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break

                elif "ip address" in Data:
                    ip = get('https://api.ipify.org').text
                    Speak(f"your IP address is {ip}")

                elif "restart system" in Data:
                            os.system("shutdown /r /t 5")

                elif "sleep system" in Data:
                            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

                elif 'switch window' in Data:
                    import pyautogui
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")

                elif "where i am" in Data or "where we are " in Data or "where are we" in Data or "where am i" in Data:
                    Speak("wait sir let me check")
                    try:
                        ipAdd= requests.get('https://api.ipify.org').text
                        print (f"{ipAdd}")
                        url ='https://get.geojs.io/v1/ip/geo/' +ipAdd+'.json'
                        geo_requests= requests.get(url)
                        geo_data =geo_requests.json()
                        city =geo_data['city']
                        country =geo_data['country']
                        Speak(f"sir i am not sure, but i think we are in {city} city of  {country} country ")
                    except Exception as e:
                        Speak("sorry sir, Due to network issue I cannot find out where we are.......")
                elif "instagram profile" in Data or "profile on instagram " in Data:
                    Speak("sir please enter the user name correctly")
                    name=input("Enter the username:")
                    webbrowser.open(f"www.instagram.com/{name}")
                    Speak(f"sir, here is your profile of the user {name}")
                    time.sleep(5)
                elif "facebook profile" in Data or "profile on facebook " in Data:
                    Speak("sir please enter the user name correctly")
                    name=input("Enter the username:")
                    webbrowser.open(f"www.facebook.com/{name}")
                    Speak(f"sir, here is your profile of the user {name}")
                    time.sleep(5)  
                elif "hello" in Data:
                    a = (1,2,3) 
                    b = random.choice(a)
                    if b==1:
                       Speak ("Hello, Welcome Back")
                    elif b==2:
                         Speak ("Hey, what's up")
                    elif b==3:
                         Speak ("Hi, I am Jarvis")
                    else:
                        pass
                elif "who am i" in Data:
                    Speak ("You are Anukaran Gaire")
                elif "what is my name" in Data:
                    Speak ("Your Name is Anukaran Gaire. and you were the one who made me.")
                elif "what's my name" in Data:
                    Speak ("Your Name is Anukaran Gaire. and you were the one who made me.")
                elif "who made you" in Data:
                    Speak ("You were the one who made me.")
                elif "what is my favorite color" in Data or "what's my favorite color" in Data:
                    Speak ("Your Favourite colour is Blue.")
                elif "what is my favorite colour" in Data or "what's my favorite colour" in Data:
                    Speak ("Your Favourite colour is Blue.")
                elif "what is your favorite color" in Data or "what's your favorite color" in Data:
                    Speak ("My Favourite colour is Blue as well.")
                elif "what is your favorite colour" in Data or "what's your favorite colour" in Data:
                    Speak ("My Favourite colour is Blue as well.")
                elif "how old i am" in Data or"how old am i" in Data:
                    Speak ("You are 15 years old")
                elif "when is my birthday " in Data or "my birthday" in Data:
                    Speak ("Your birthday is on 16th September")
                elif "where is everest english school " in Data:
                    Speak ("Everest English School is Located in Mibacchen, Bhaktapur.")
                elif "in which school do I study" in Data:
                    Speak ("You are currently in Studying in Everest English School. But you made me at the Grade of 09")
                elif "do you believe in god" in Data:
                    Speak ("Yes, as you know god made humans and as Anukaran Gaire Made me I think There is god.")
                elif "how old are you?" in Data or"how old are you" in Data:
                    Speak ("I am 1 years old")
                elif "offline" in Data or "get out" in Data:
                    exit()
                else:
                    if Data == "" :
                        Speak("")
                    else:
                        """
                        At the command line, only need to run once to install the package via pip:

                        $ pip install google-generativeai
                        """

                        import google.generativeai as genai

                        genai.configure(api_key="AIzaSyBdfi5xCZdG8Zyw3NUGh6q5WVJKWK0z7Z0")

                        # Set up the model
                        generation_config = {
                        "temperature": 0.9,
                        "top_p": 1,
                        "top_k": 1,
                        "max_output_tokens": 2048,
                        }

                        safety_settings = [
                        {
                            "category": "HARM_CATEGORY_HARASSMENT",
                            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                        },
                        {
                            "category": "HARM_CATEGORY_HATE_SPEECH",
                            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                        },
                        {
                            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                        },
                        {
                            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                        }
                        ]

                        model = genai.GenerativeModel(model_name="gemini-pro",
                                                    generation_config=generation_config,
                                                    safety_settings=safety_settings)

                        prompt_parts = [
                        ]

                        response = model.generate_content(Data)
                        Speak(response.text)

