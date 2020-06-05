import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser     #it enables the feature to open web browser like youtube, wikipedia facebook etc
import os
import smtplib   # we can send email through this module

engine=pyttsx3.init('sapi5')  #it will take the audio and give as an text , so basically this help to take voice
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():   #this will wish me according to datetime module
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    elif hour>=18 and hour<=24:
        speak("Good Night")
    
    speak("i am jarvis sir, how may i help you ")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=.8
        r.energy_threshold=400
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please sir...")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587) #this is a port number 587
    server.ehlo()
    server.starttls()
    server.login('akramnadim1999@gmail.com', 'nadimakram@901')
    server.sendmail('akramnadim1999@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    wishMe()
    # takeCommand()
    # while True:  #this will continuosly run the while loop till end
    if 1:
        
        query= takeCommand().lower()   #this fun take input and gives result from wikipedia 
        if 'wikipedia' in query:
            speak('please wait ,searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=10)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak('please wait i am opening youtube for you')
            webbrowser.open("YouTube.com")
        elif 'stack overflow' in query:
            webbrowser.open("stack overflow")
        elif 'google' in query:
            speak("according to google")
            webbrowser.open('www.google.com')
        elif 'geeksforgeeks' in query:
            webbrowser.open('geeksforgeeks')             #we may add millions of sites in this AI project and enjoy unlimited experience
        elif 'play music' in query:
            music_dir='D:\\music'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))
        elif 'play movie' in query:
            movie_dir='D:\\chacha vidhayak hai hamare'
            movie=os.listdir(movie_dir)
            print(movie)
            os.startfile(os.path.join(movie_dir,movie[2]))
        elif 'open code' in query:
            speak("openning code...")
            codePath=('C:\\Users\\Acer\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code')
            os.startfile(codePath)
        elif 'open chrome' in query:
            speak("opening chrome please wait")
            codePath=('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Google Chrome')
        elif 'open paint' in query:
            speak("opening paint")
            codePath=('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\\Paint')
        elif 'send email' in query:
            try:
                speak("what should i say sir?")
                content= takeCommand()
                to= "najiyafalak09@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                # print(e)
                speak("sorry nadim bhaai i am not sending email at this time")
