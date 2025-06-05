import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import requests
import pyjokes
import pyautogui
import pyautogui as pi 
from googleapiclient.discovery import build
import urllib.parse
from nltk.corpus import wordnet
import shutdown
import requests
import urllib3


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#print(voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING")

    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON")

    else:
        speak("GOOD EVENING")

    print("\n Welcome to Dexter, Please tell me how may i help you today")
    speak("Welcome to Dexter, Please tell me how may i help you today")
    
   


def takeCommand():

    request=input("\n PLEASE ENTER COMMAND:")
    return request

news_api_key="5ca740f3869949edbace4f66577932bb"


def news():
    main_url="https://newsapi.org/v2/top-headlines?country=in&apiKey=" +news_api_key
    news=requests.get(main_url).json()
    #print(news)
    article=news["articles"]
    #print(article)

    news_article=[]
    for art in article:
        news_article.append(art['title'])
        #print(news_article)

    for i in range(5):
        print("\n")
        print(i+1,news_article[i])
        print("\n")
        speak(news_article[i])


def minimize_window():
    pyautogui.hotkey('winleft', 'down')  # Presses WinKey + DownArrow to minimize the active window


def get_weather():
    city= input("\n Which city's  weather condition do you want to know :")
    weather_api_key= "bdc594a4451b1eb4029ce1101a814117"
    url= f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    response=requests.get(url).json()
    #print(response)
    weather_description=response['weather'][0]['description']
    temperature=response['main']['temp']
    humidity =response['main']['humidity']
    wind_speed=response['wind']['speed']

    return f"The Weather in {city} has {weather_description}. Temperature: {temperature}°C, Humidity:{humidity}%, Wind Speed:{wind_speed} meter per second"



youtube_api_key="AIzaSyBRD1Dy0W2Qm7fT6JBMTYmHboVY9qSrmzs"


def search_youtube_videos(query, youtube_api_key):
    #Initialize Youtube data api client
    youtube= build('youtube', 'v3', developerKey=youtube_api_key)

    #search request to retrieve videos based on query
    search_response= youtube.search().list(q=query,part='id,snippet', type='video').execute()  
    #print(search_response) 

    #Extract video information from search response
    videos=[]
    for search_result in search_response.get('items', []):
        video_id=search_result['id']['videoId']
        title= search_result['snippet']['title']
        videos.append({'title': title, 'video_id':video_id})

    return videos

def play_youtube_video(video_query):
    play=urllib.parse.quote(video_query)
    url= f"https://www.youtube.com/results?search_query={play}"
    webbrowser.open(url)


def set_alarm(alarm_time):
    while True:
        current_time=datetime.datetime.now().strftime("%H:%M")
        if current_time==alarm_time:
            speak("Time to wake up!!!")
            print("Time to wake up!!!")
            break
        else:
            time.sleep(60)

def get_definition(word):
    synsets=wordnet.synsets(word)
    if synsets:
        #select first synset(most common usage)
        synset= synsets[0]
        return synset.definition()
    else:
        return "No definition found for the word"


def add_notes(note):
    with open('notes.txt', 'a') as file:
        file.write(note +'\n')
    print("\n Note added successfully.")
    speak("Note added successfully.")


def display_notes():
    with open('notes.txt', 'r') as file:
        notes=file.readlines()
        if notes:
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note.strip()}")
        else: 
            print("\n No notes found.")
            speak("No notes found.")

def delete_notes(index):
    try:
        with open('notes.txt', 'r') as file:
            notes=file.readlines()
        with open('notes.txt', 'w') as file:
            for i, note in enumerate(notes, start=1):
                if i!= index:
                    file.write(note)
        print("\n Note deleted succesfully.")
        speak("Note deleted succesfully.")

    except IndexError:
        print("\n Invalid notes index.")
        speak("Invalid notes index.")

def clear_notes():
    open('notes.txt', 'w').close()
    print("\n All notes cleared.")
    speak("All notes cleared.")


if __name__== "__main__":
    wishMe()
    while True:
        request=takeCommand()
    
    
        if 'wikipedia' in request:
            speak('searching wikipedia')
            request = request.replace("wikipedia","")
            results = wikipedia.summary(request, sentences=2)
            print("\n According to Wikipedia")
            speak("according to Wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in request:
            webbrowser.open("www.youtube.com")
            speak("Opening Youtube")

        elif 'hello' in request:
            speak("heyy")
            print("hi")

        elif 'open google' in request:
            webbrowser.open("www.google.com")
            speak("Opening Google")

        elif 'search google' in request:
            result= input("\n Enter Search query:")
            webbrowser.open_new_tab("https://www.google.com/search?q="+ result)
            speak("Searching Google") 

        elif 'open msbte' in request:
            webbrowser.open("msbte.org.in")
            speak("Opening Msbte website")


        elif 'open plgpl' in request:
            webbrowser.open("plgpl.org")
            speak("Opening PLGPL website")


        elif 'play music' in request:
            music_dir = 'C:\\Users\\Public\\Music'
            songs = os.listdir(music_dir)
            #print(songs)
            speak('Playing songs')
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'time' in request:
            strTime =  datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Greetings, the time is {strTime}")
            print("\n",strTime)

        elif 'open code' in request:
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak('Opening VS code')

        elif 'open word' in request:
            wordPath= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word 2016.lnk"
            speak("Opening Microsoft Word")
            os.startfile(wordPath)
            

        elif 'open microsoft edge'in request:
            edgePath= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk"
            speak("Opening Microsoft Edge")
            os.startfile(edgePath)
            

        elif 'news' in request:
            speak("Todays top headlines...")
            news()

        elif 'joke' in request:
            jokes=(pyjokes.get_joke())
            print(jokes)
            speak(jokes)
            

        elif 'exit' in request:
            print("\n Thanks for giving me your time")
            speak("Thanks for giving me your time")
            exit()

        elif 'minimize window' in request:
            speak("minimizing window")
            minimize_window()

        elif 'who are you' in request:
            print("\n I am a Virtual Assistant. You can call me Dexter")  
            speak("I am a Virtual Assistant. You can call me Dexter")

        elif 'how are you'in request:
            print("\n I am fine, Thank you")
            speak("I am fine, Thank you")
            print("\n How are you?") 
            speak("How are you?") 

        elif 'fine' in request:
            print("\n It is good to know that")
            speak("It is good to know that")

        elif 'weather' in request:
            weather_info=get_weather()
            print(weather_info)
            speak(weather_info)

        elif 'search youtube' in request: 
            youtube_api_key="AIzaSyBRD1Dy0W2Qm7fT6JBMTYmHboVY9qSrmzs"
            query= input ("\n Enter Your Youtube Search Query:")
            videos= search_youtube_videos(query, youtube_api_key)
            if videos:
                print("\n Search Results:")
                speak("Search Results:")
                for video in videos:
                    print(f"Title: {video['title']}")
                    print(f"Video ID: {video['video_id']}")
                    print()
            else:
                print("\n No video found For Search query")

        elif 'play video' in request:
            video_query= input("\n Enter The Title of the video You want to play: ")
            speak("Searching Youtube")
            play_youtube_video(video_query)

        elif 'set alarm' in request:
            alarm_time=input("Enter time for your alarm(HH:MM format)")
            set_alarm(alarm_time)

        elif 'definition' in request:
            word=input("\n Enter a word to define:")
            definition=get_definition(word)
            print(definition)
            speak(definition)
  

        elif 'add note' in request:
            note= input("\n Please Enter your note:")
            add_notes(note)

        elif 'display notes' in request:
            display_notes()

        elif 'delete note' in request:
            index= int(input("\n Please Enter the index of note you want to delete:"))
            delete_notes(index)

        elif 'clear notes' in request:
            clear_notes()


        elif'search app'in request:
            app=input("\n Enter name of App to open:")
            pi.press('win')
            time.sleep(1)
            pi.typewrite(app,0.1)
            pi.press('center')
            time.sleep(2)            
            

        elif'move cursor'in request:
            pi.moveTo(142,547,1)
            pi.dragTo(300,300,2)

        elif'whatsapp'in request:
            print("\n Message will be sent automatically")
            speak("Message will be sent automatically")
            time.sleep(10)
            count=0
            while count<=1:
                pyautogui.typewrite("hello")
                pyautogui.press("enter")
                count=count+1

        elif'shutdown system'in request:
            print ("\n Are you sure you want to shutdown")
            speak ("are you sure you want to shutdown")
            shutdown=input("\n do you wish to shutdown your computer (yes/no)") 
            if shutdown =="yes":
                os.system("shutdown /s /t 1")

            elif shutdown =="no":
                break;  

        else:
            print("\n I Dont Understand, Please Try Again.")
            speak("I Dont Understand, Please Try Again.")
        
                    
            
    


        


        




