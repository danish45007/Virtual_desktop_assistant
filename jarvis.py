try:
    import pyttsx3
    import speech_recognition as sr
    import datetime
    import wikipedia
    import webbrowser
    import osmsiisng 
    import smtplib
    import pyaudio
    import word2number
    from word2number import w2n
    import requests
    import reverse_geocoder as rg
    import pprint
    from selenium import webdriver
    import time
    from textblob import TextBlob as blob
except Exception as e:
    print("Some modules are missing {}".format(e)) 


coordinates = (12.817329,80.039988)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
engine.setProperty('voice', voices[-1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(mail, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(' user_email.com', 'password')
    server.sendmail('sender_email.com', mail, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'how you doing'.lower() in query:
            speak('great as i am with you right now')

        elif 'tell me a joke' in query:
            speak('searching a joke for you')
            res = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
            joke = (res.json()['joke'])
            print(joke)
            speak(joke)


        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'C:\\Users\\DANISH\\Desktop\\WAVE MUSIC\\SONGS\\EDM'
            songs = os.listdir(music_dir)
            print(songs)
            speak("Enter the song number")
            content = takeCommand()
            try:
                num = w2n.word_to_num(content)
                os.startfile(os.path.join(music_dir, songs[num]))
            except:
                speak('try again sir')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "F:\\New_pycharm\\PyCharm Community Edition 2019.1.3\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'email to friend'.lower() in query:
            try:

                # speak('Enter the email to whom you want to mail?')
                # command = takeCommand()
                mail = 'danish45007@gmail.com'
                speak("What should I say?")
                content = takeCommand()
                sendEmail(mail, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Danish. I am not able to send this email")

        elif "what's the temperature" in query:

            speak('searching your current location temperature')
            r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=1264527&APPID=7e5f1bac9c2ebf7cf42969f611f2b165&units=metric')
            weather = r.json()['main']['temp']
            speak(weather)
            speak('degree celsius')

        elif "what's my location" in query:
            speak('searching your current location')
            result = rg.search(coordinates)
            a = pprint.pprint(result)
            print(a)
            #speak(a)

        elif "whatsapp to friend" in query:
            driver = webdriver.Chrome('C:\\Users\\DANISH\\PycharmProject\\Examples\\venv\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe')
            driver.get('https://web.whatsapp.com/')
            time.sleep(15)
            sender_name = input("Enter the name to whom you want to send message: ")
            user = driver.find_element_by_xpath('//span[@title="{}"]'.format(sender_name))
            user.click()
            message = input("Enter th message: ")
            mess_box = driver.find_element_by_class_name("_3u328 copyable-text selectable-text")
            mess_box.click()
            mess_box.send_keys(message)
            button = driver.find_element_by_class_name('_3M-N-')
            button.click()
            speak('message sent successfully')


        elif 'run sentiment analysis' in query:
            speak('running the sentiment analysis')
            for _ in range(10):
                data = takeCommand()
                tb = blob(data)
                a = tb.sentiment
                print(a)
                speak(a)

        elif 'terminate' in query:
            speak("Thanks for using my service. happy to help you")
            break


