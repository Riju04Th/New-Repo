import pyttsx3
import speech_recognition as sr
import datetime
import pyjokes
import os
# import wikipedia
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def Greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    elif hour>=18 and hour<22:
        print("Good Evening!")
        speak("Good Evening!")
    else:
        print("Good Night!")
        speak("Good Night!")
    print("I am EDITH Sir. Please tell me how may I help you")
    speak("I am EDITH Sir. Please tell me how may I help you")
def takeCommand():
#It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return None
    return query
if __name__ == "__main__":
    Greetings()
    # TC = takeCommand()
    # query = TC.lower()
    query = input("enter command: ")
    while True:
        if "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("Sir, the time is", strTime)
            speak(f"Sir, the time is {strTime}")
            break

        elif "date" in query:
            strDate = datetime.datetime.now().strftime("%d/%m/%Y")
            print("Sir, the date is", strDate)
            speak(f"Sir, the date is {strDate}")
            break

        # elif "wiki" in query:
        #     print("Searching Wikipedia...")
        #     speak("Searching Wikipedia...")
        #     query = query.replace("wikipedia", "")
        #     results = wikipedia.summary(query, sentences=2)
        #     print("According to Wikipedia")
        #     speak("According to Wikipedia")
        #     print(results)
        #     speak(results)
        #     break

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke(language="en", category="all")
            print(joke)
            speak(joke)
            break

        elif "play songs" in query:
            songs_dir = ""
            songs = os.listdir(songs_dir)
            print("This songs available in the directory:")
            speak("This songs available in the directory:")
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif "exit" in query:
            print("Sir, I am closing the sessions. Goodbye!")
            speak("Sir, I am closing the sessions. Goodbye!")
            break
