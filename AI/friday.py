import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pywhatkit
from keyboard import press
import subprocess as sp
import pywhatkit as pwt
import wikipedia as googleScrap
from pynput.keyboard import Key, Controller
import time
from pyautogui import click, leftClick, rightClick, doubleClick, tripleClick
keyboard=Controller()
import pyautogui
import winsound 
from winsound import PlaySound
# from playsound import playsound
import openai
import pyjokes
openai.api_key="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"
# time.sleep(2)

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[1].id)

def speak(voice):
    engine.say(voice)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good morning,Anand sir!')
    elif hour>=12 and hour<16:
        speak('Good afternoon,Anand sir!')
    else:
        speak('Good evening,Anand sir!')
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        voice = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(voice, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.
    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
     
if __name__ == "__main__" :
    wishme()
    # speak('Haaye aayi am FRIDAY. how can i help you?')

def google():
    glpath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    os.startfile(glpath)

def write():
    speak('What should I type')
    print('What should I type')
    z=takeCommand().lower()
    speak('Okay sir')
    print('Okay sir')
    keyboard.type(z)

# def beep():
    # playsound("C:\\Users\\HP\\Documents\\Audacity\\Active.mp3")
# beep()


print('Initialising your system.....')
speak('Initialising your system.....')
while True:
    print('hello')
    alpha = takeCommand().lower()
    if 'wake up' in alpha and 'friday' in alpha: 
      print('welcome Anand sir how can i help you')
      speak('welcome Anand sir how can i help you')
# print("ghg")betaalpha

      i=0
      while i<1: 
        query = takeCommand().lower()

        # if 'friday' in query:
        #     speak("yess sir")
        #online system
        #wikipedia   
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    query = query.replace("friday", "")
                    results = wikipedia.summary(query, sentences=2) 
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

        # elif 'wake up' in query:
        #     wishme()

        elif 'friday' in query:
            # if 'wake up' in query:
            #     wishme()
            speak('yes sir')
            print('yes sir')
        # elif 'jarvis' in query:
        #     speak('Sir I am friday, not jarvis.')
        #     print('Sir I am friday, not jarvis.')
        elif 'hriday' in query:
            # if 'wake up' in query:
            #     wishme()
            speak('yes sir')
            print('yes sir')
        #google
        elif 'google' in query:
            if 'open' in query:
                print("Googlewa")
                speak('Opening google')
                # webbrowser.open("www.google.com")
                google()
                speak('What you would like to search')
                print('What you would like to search')
                z=takeCommand().lower()
                z=z.replace("search","")
                speak("According to google")
                keyboard.type(z)
                press('enter')
                # results = googleScrap.summary(z, sentences=2)
                # print(results)
                # speak(results)
            elif 'search' in query:
                query=query.replace("search","")
                query=query.replace("google","")
                speak('searching in google')
                google()
                # pywhatkit.search(query)
                speak("According to google")
                keyboard.type(query)
                press('enter')
                results = googleScrap.summary(query, sentences=2)
                print(results)
                speak(results)
        elif 'close' in query:
            query=query.replace("close","")
            os.system("taskkill/im {}.exe".format(query))
            # pyautogui.hotkey("alt","f4")
        elif 'exit' in query:
            pyautogui.hotkey("alt","f4")

        #temperature and climate
        elif 'temperature' in query:
            google()
            time.sleep(2)
            keyboard.type(query)
            press('enter')

        elif 'weather' in query:
            google()
            time.sleep(2)
            keyboard.type(query)
            press('enter')

        elif 'joke' in query:
            print("okay sir , here is a joke for you")
            speak("okay sir , here is a joke for you")
            a=pyjokes.get_jokes
            speak(a)

        
        #youtube
        elif 'youtube' in query:
            if 'open' in query:
                print("Opening youtube")
                speak("Opening youtube")
                google()
                time.sleep(2)
                keyboard.type('https://www.youtube.com/')
                press('enter')
                time.sleep(2)
                speak('What you would like to view')
                print('What you would like to view')
                z=takeCommand().lower()
                # z=z.replace("search","")
                speak("Searching all the results of " + z)
                print("Searching all the results of " + z)
                time.sleep(2)
                press('?')
                keyboard.type(z)
                time.sleep(2)
                press('enter')

            elif 'search' in query:
                query=query.replace("search","")
                query=query.replace("youtube","")
                print("Searching on youtube")
                speak("Searching on youtube")
                google()
                time.sleep(2)
                keyboard.type('https://www.youtube.com/')
                press('enter')
                time.sleep(2)
                press('?')
                keyboard.type(query)
                time.sleep(2)
                press('enter')
            elif 'play' in query:
                query=query.replace("play","")
                query=query.replace("youtube","")
                print("playing on youtube")
                speak("playing on youtube")
                google()
                time.sleep(2)
                keyboard.type('https://www.youtube.com/')
                press('enter')
                time.sleep(2)
                press('?')
                keyboard.type(query)
                time.sleep(2)
                press('enter')

        #music
        elif 'music' in query:
                # if 'music' in query:
                    speak('which song should i play')
                    print('which song should i play')
                    z=takeCommand().lower()
                    speak('playing ' + z)
                    print('playing ' + z)
                    pywhatkit.playonyt(z)
        elif 'video' in query:
                 if 'play' in query:
                    speak('on which topic should i play video')
                    print('on which topic should i play video')
                    z=takeCommand().lower()
                    speak('playing ' + z)
                    print('playing ' + z)
                    pywhatkit.playonyt(z)
        elif 'song' in query:
            speak('Okay sir, playing a song for you')
            print('Okay sir, playing a song for you')
            mysong="C:\\Users\\HP\\Desktop\\Desktop!\\My Songs\\Audios"
            song=os.listdir(mysong)
            os.startfile(os.path.join(mysong,song[random.randint(5,10)]))
        #communication
        elif 'message' in query:
            speak('Okay sir')
            print('Okay sir')
            whpath="C:\\Users\\Anand Jha\\OneDrive\\Desktop\\WhatsApp - Shortcut.lnk"
            os.startfile(whpath)
            time.sleep(15)
            click(x=285, y=141)
            pyautogui.hotkey('ctrl','a')
            # speak('To whom should i send the message')
            # print('To whom should i send the message')
            time.sleep(2)
            query=query.replace("message","")
            keyboard.type(query)
            time.sleep(2)
            click(x=265, y=250)
            time.sleep(1)
            speak('What message do you want to send')
            print('What message do you want to send')
            a=takeCommand().lower()
            time.sleep(1)
            speak('Messaging ' + query)
            print('Messaging ' + query)
            keyboard.type(a)
            time.sleep(2)
            press('enter')
        elif 'call' in query:
            speak('Okay sir')
            print('Okay sir')
            whpath="C:\\Users\\Anand Jha\\OneDrive\\Desktop\\WhatsApp - Shortcut.lnk"
            os.startfile(whpath)
            time.sleep(15)
            if 'voice' in query:
                click(x=285, y=141)
                pyautogui.hotkey('ctrl','a')
                time.sleep(2)
                query=query.replace("call","")
                query=query.replace("voice","")
                keyboard.type(query)
                time.sleep(2)
                click(x=265, y=250)
                time.sleep(1)
                speak('Voice Calling' + query)
                print('Voice Calling' + query)
                click(x=1780, y=70)
            elif 'video' in query:
                click(x=285, y=141)
                pyautogui.hotkey('ctrl','a')
                time.sleep(2)
                query=query.replace("call","")
                query=query.replace("video","")
                keyboard.type(query)
                time.sleep(2)
                click(x=265, y=250)
                time.sleep(1)
                speak('Video Calling' + query)
                print('Video Calling' + query)
                click(x=1690, y=70)
            else:
                click(x=285, y=141)
                pyautogui.hotkey('ctrl','a')
                time.sleep(2)
                query=query.replace("call","")
                query=query.replace("voice","")
                keyboard.type(query)
                time.sleep(2)
                click(x=265, y=250)
                time.sleep(1)
                speak('Calling' + query)
                print('Calling' + query)
                click(x=1780, y=70)

        #website
        elif 'website' in query:
            if 'open' in query:
                query=query.replace("open","")
                query=query.replace("website","")
                webbrowser.open("{}.com".format(query))
        elif 'internet' in query:
            if 'speed' in query:
                speak('Checking internet speed')
                print('Checking internet speed')
                google()
                time.sleep(1)
                keyboard.type('https://fast.com/')
                time.sleep(1)
                press('enter')


        #offline system
        #clock
        # if 'set' and 'alarm' in query:
        elif 'time'in query:
            now=datetime.datetime.now()
            print('Time is: \n')
            print(now.strftime("%r"))
            speak('Time is')
            speak(now.strftime("%r"))
        elif 'date' in query:
            now=datetime.datetime.now()
            print('Date is: \n')
            print(now.strftime("%d %b %G"))
            speak('Date is')
            speak(now.strftime("%d %b %G"))
        # if 'date and time' in query:
        #     now=datetime.datetime.now()
        #     print(now.strftime("%c"))
        #     speak(now.strftime("%c"))
        # if 'day' or 'de' in query:
        #     now=datetime.datetime.now()
        #     print('Today is: \n')
        #     print(now.strftime("%c"))
        #     speak('Today is')
        #     speak(now.strftime("%c"))

        #opening system 
        # elif 'cut' in query:
        #     if 'call' in query:
        #         if 'voice' in query:
        #             click(x=1864, y=80)
        #         elif 'video' in query:
        #             click(x=1710, y=433)
        elif 'open' in query:
        #vs code
            if 'vs code' in query:
                print("Opening VS code")
                speak('Opening vs code')
                vspath="C:\\Users\\Anand Jha\\OneDrive\\Desktop\\Visual Studio Code - Shortcut.lnk"
                os.startfile(vspath)
        #whatsapp
            elif 'whatsapp' in query:
                print("Opening whatsapp")
                speak('Opening whatsapp')
                whpath="C:\\Users\\Anand Jha\\OneDrive\\Desktop\\WhatsApp - Shortcut.lnk"
                os.startfile(whpath)
                time.sleep(15)
                speak('What you want to do')
                print('What you want to do')
                z=takeCommand().lower()
                if 'message' in z:
                    speak('Okay sir')
                    print('Okay sir')
                    click(x=285, y=141)
                    pyautogui.hotkey('ctrl','a')
                    # speak('To whom should i send the message')
                    # print('To whom should i send the message')
                    time.sleep(2)
                    z=z.replace("message","")
                    keyboard.type(z)
                    time.sleep(2)
                    click(x=265, y=295)
                    time.sleep(1)
                    speak('What message do you want to send')
                    print('What message do you want to send')
                    a=takeCommand().lower()
                    time.sleep(1)
                    keyboard.type(a)
                    time.sleep(2)
                    press('enter')
                elif 'call' in z:
                    if 'voice' in z:
                        speak('Okay sir')
                        print('Okay sir')
                        click(x=285, y=141)
                        pyautogui.hotkey('ctrl','a')
                        time.sleep(2)
                        z=z.replace("call","")
                        z=z.replace("voice","")
                        keyboard.type(z)
                        time.sleep(2)
                        click(x=265, y=295)
                        time.sleep(1)
                        speak('Voice Calling' + z)
                        print('Voice Calling' + z)
                        click(x=1714, y=62)
                    elif 'video' in z:
                        speak('Okay sir')
                        print('Okay sir')
                        click(x=285, y=141)
                        pyautogui.hotkey('ctrl','a')
                        time.sleep(2)
                        z=z.replace("call","")
                        z=z.replace("video","")
                        keyboard.type(z)
                        time.sleep(2)
                        click(x=265, y=295)
                        time.sleep(1)
                        speak('Video Calling' + z)
                        print('Video Calling' + z)
                        click(x=1630, y=61)
                    else:
                        speak('Okay sir')
                        print('Okay sir')
                        click(x=285, y=141)
                        pyautogui.hotkey('ctrl','a')
                        time.sleep(2)
                        z=z.replace("call","")
                        z=z.replace("voice","")
                        keyboard.type(z)
                        time.sleep(2)
                        click(x=265, y=295)
                        time.sleep(1)
                        speak('Voice Calling' + z)
                        print('Voice Calling' + z)
                        click(x=1714, y=62)


                    
        #word
            elif 'word' in query:
                print("Opening word")
                speak('Opening word')
                wopath="C:\\Users\\Anand Jha\\OneDrive\\Desktop\\Word - Shortcut.lnk"
                os.startfile(wopath)
        #excel
            elif 'excel' in query:
                print("Opening excel")
                speak('Opening excel')
                expath="C:\\Users\\Anand Jha\\OneDrive\\Desktop\\Excel - Shortcut.lnk"
                os.startfile(expath)
        #audacity
            # elif 'audacity' in query:
            #     print("Opening audacity")
            #     speak('Opening audacity')
            #     adpath="C:\\Audacity\\Audacity.exe"
            #     os.startfile(adpath)
        # instagram
            elif 'instagram' in query:
                    print("Opening Instagram")
                    speak("Opening Instagram")
                    google()
                    time.sleep(2)
                    keyboard.type('https://www.instagram.com/')
                    press('enter')
        #youtube
            # elif 'youtube' in query:
            #         print("Opening youtube")
            #         speak("Opening youtube")
            #         google()
            #         time.sleep(2)
            #         keyboard.type('https://www.youtube.com/')
            #         press('enter')
            #         time.sleep(2)
            #         press
        #linked in
            elif 'linkedin' in query:
                    print("Opening linked in")
                    speak("Opening linked in")
                    google()
                    time.sleep(2)
                    keyboard.type("https://www.linkedin.com/in/aryan-raj-724ab023a/")
                    press('enter')
        #git hub
            elif 'github' in query:
                    print("Opening git hub")
                    speak("Opening git hub")
                    google()
                    time.sleep(2)
                    keyboard.type("https://github.com/")
                    press('enter')
        #flipkart
            elif 'flipkart' in query:
                    print("Opening flipkart")
                    speak("Opening flipkart")
                    google()
                    time.sleep(2)
                    keyboard.type("https://www.flipkart.com/viewcart?otracker=PP_GoToCart")
                    press('enter')
        #hotstar
            elif 'hotstar' in query:
                    print("Opening hotstar")
                    speak("Opening hotstar") 
                    google()
                    time.sleep(2)
                    keyboard.type("https://www.hotstar.com/in")
                    press('enter')
        #jio cinema
            elif 'jio cinema' in query:
                    print("Opening jio cinema")
                    speak("Opening jio cinema") 
                    google()
                    time.sleep(2)
                    keyboard.type("https://www.jiocinema.com/")
                    press('enter')
        
        #facebook
            elif 'facebook' in query:
                    print("Opening facebook")
                    speak("Opening facebook")
                    google()
                    time.sleep(2)
                    keyboard.type("https://www.facebook.com/")
                    press('enter')
        #gmail
            elif 'gmail' in query:
                    print("Opening gmail")
                    speak("Opening gmail")
                    google()
                    time.sleep(2)
                    keyboard.type("https://mail.google.com/mail/u/0/#inbox")
                    press('enter')
        #google classroom
            elif 'classroom' in query:
                print("Opening google classroom")
                speak("Opening google classroom")
                google()
                time.sleep(2)
                keyboard.type("https://classroom.google.com/u/0/")
                press('enter')
            elif 'search' in query:
                # if 'insta id' in query:
                #     click(x=61, y=287)
                    query=query.replace("open","")
                    query=query.replace("search","")
                    speak('Opening ' + query)
                    print('Opening ' + query)
                    pyautogui.hotkey('win','s')
                    time.sleep(2)
                    keyboard.type(query)
                    time.sleep(1)
                    press('enter')
            elif 'messenger' in query:
                query=query.replace("open","")
                speak('Opening ' + query)
                print('Opening ' + query)
                pyautogui.hotkey('win','s')
                time.sleep(2)
                keyboard.type("instagram")
                time.sleep(1)
                press('enter')
                time.sleep(5)
                click(x=59, y=483)
            elif 'my files' in query:
                speak("Opening your files")
                print("Opening your files")
                pyautogui.hotkey('win','e')
            elif 'notification' in query:
                speak('Here are the notifications')
                print('Here are the notifications')
                pyautogui.hotkey('win','n')
            elif 'setting' in query:
                speak('Okay sir')
                print('Okay sir')
                if 'quick' in query:
                    pyautogui.hotkey('win','a')
                else:
                    pyautogui.hotkey('win','i')
            elif 'microsoft' in query:
                speak('Okay sir')
                print('Okay sir')
                if 'chat' in query:
                    pyautogui.hotkey('win','c')
            elif 'task view' in query:
                speak('Okay sir')
                print('Okay sir')
                pyautogui.hotkey('win','tab')


        #keyboard
        elif 'stop' in query:
            press('k')
        elif 'full' in query:
            press('f')
        # elif 'mute' in query:
        #     press('m')

        # elif 'start' in query:
        #     press('k')
        # elif 'small' in query:
        #     press('f')
        # elif 'unmute' in query:
        #     press('m')

        elif 'mute' in query:
            pyautogui.press('volumemute')
        elif 'unmute' in query:
            pyautogui.press('volumemute')

        elif 'stop' in query:
            pyautogui.press('playpause')
        elif 'start' in query:
            pyautogui.press('playpause')

        elif 'minimise' in query:
            pyautogui.hotkey('win','d')
        elif 'restore' in query:
            pyautogui.hotkey('win','d')
        elif 'screenshot' in query:
            pyautogui.hotkey('win','prtsc')
        
        #youtube skip and recap
        elif 'skip' in query:
            if 'ten' in query:
                pyautogui.press('l')
            elif 'five' in query:
                pyautogui.press('right')
            elif '10' in query:
                pyautogui.press('l')
            elif '5' in query:
                pyautogui.press('right')
            else:
                pyautogui.press('right')
        elif 'recap' in query:
            if 'ten' in query:
                pyautogui.press('j')
            elif 'five' in query:
                pyautogui.press('left')
            elif '10' in query:
                pyautogui.press('j')
            elif '5' in query:
                pyautogui.press('left')
            else:
                pyautogui.press('left')
        # elif 'skip' in query:
        #     query=query.replace("skip","")
        #     query=query.replace("second","")
        #     query=query.replace("seconds","")
        

        #copy paste and other general keyboard settings
        elif 'copy' in query:
            pyautogui.hotkey('ctrl','a')
            time.sleep(1)
            pyautogui.hotkey('ctrl','c')
        elif 'paste' in query:
            click()
            time.sleep(1)
            pyautogui.hotkey('ctrl','v')
        elif 'select all' in query:
            tripleClick()
            pyautogui.hotkey('ctrl','a')
        elif 'undo'in query:
            pyautogui.hotkey('ctrl','z')
        elif 'cut' in query:
            pyautogui.hotkey('ctrl','a')
            time.sleep(1)
            pyautogui.hotkey('ctrl','x')
        elif 'switch' in query:
            pyautogui.hotkey('alt','tab')
        elif 'hidden' in query:
            pyautogui.hotkey('win','b')
        elif 'new file' in query:
            speak('Creating a new file')
            print('Creating a new file')
            pyautogui.hotkey('ctrl','n')
        elif 'save' in query:
            speak("Saving")
            print("Saving")
            pyautogui.hotkey('ctrl','s')

        # elif 'new tab' in query:
        #     press('ctrl+T')
        elif 'new window' in query:
            press('ctrl+N')
        # elif 'new incognito tab' in query:
        #     press('ctrl+shift+N')
        

        #tab control
        elif 'tab' in query:
            if 'new' in query:
                press('ctrl+T')
            elif 'incognito' in query:
                press('ctrl+shift+N')
            elif 'forward' in query:
                pyautogui.hotkey('ctrl','tab')
            elif 'backward' in query:
                pyautogui.hotkey('ctrl','shift','tab')
            elif '1' in query:
                pyautogui.hotkey('tab','1')
            elif '2' in query:
                pyautogui.hotkey('tab','2')
            elif '3' in query:
                pyautogui.hotkey('tab','3')
            elif '4' in query:
                pyautogui.hotkey('tab','4')
            elif '5' in query:
                pyautogui.hotkey('tab','5')
            elif '6' in query:
                pyautogui.hotkey('tab','6')

        elif 'select' in query:
            if 'address bar' in query:
                press('alt+D')
            elif 'search box' in query:
                press('ctrl+E')
        
        #desktop control 
        elif 'desktop' in query:
            if 'new' in query:
                pyautogui.hotkey('win','ctrl','d')
            elif 'next' in query:
                pyautogui.hotkey('win','ctrl','right')
            elif 'previous' in query:
                pyautogui.hotkey('win','ctrl','left')
            elif 'remove' in query:
                pyautogui.hotkey('win','ctrl','f4')
        # elif 'go' in query:
        elif 'back' in query:
                pyautogui.hotkey('alt','left')
        elif 'next' in query:
                pyautogui.hotkey('alt','right')
        elif 'reload' in query:
            press('ctrl+R')

        #basic key control
        elif 'enter' in query:
            pyautogui.press('enter')
        elif 'space' in query:
            pyautogui.press('space')
        elif 'delete' in query:
            pyautogui.press('backspace')
        elif 'caps lock' in query:
            pyautogui.press('capslock')
        elif 'num lock' in query:
            pyautogui.press('numlock')
        elif 'write' in query:
            write()
        elif 'type' in query:
            write()
        elif 'alpha' in query:
            press('?')
            pyautogui.hotkey('ctrl','a')
        
        #arrow control
        elif 'up' in query:
            if 'page' in query:
                pyautogui.press('pageup')
            else:
                pyautogui.press('up')
        elif 'down' in query:
            if 'page' in query:
                pyautogui.press('pagedown')
            elif 'shut' in query:
                speak('Shutting down your PC')
                pwt.shutdown(time=5)
            else:
                pyautogui.press('down')
        elif 'left' in query:
            pyautogui.press('left')
        elif 'right' in query:
            pyautogui.press('right')
        elif 'beta' in query:
            press('m')

        #volume control
        elif 'volume' in query: 
            if 'increase' in query: 
                    pyautogui.press('volumeup')
                    pyautogui.press('volumeup')
                    pyautogui.press('volumeup')
                    pyautogui.press('volumeup')
                    pyautogui.press('volumeup')
            elif 'decrease' in query:
                    pyautogui.press('volumedown')
                    pyautogui.press('volumedown')
                    pyautogui.press('volumedown')
                    pyautogui.press('volumedown')
                    pyautogui.press('volumedown')
    

        
        # elif 'shutdown' in query:
        #      speak('Shutting down your PC')
        #     #  sleep(5)
        #     #  os.system('shutdown /s /t /1')
        #      pwt.shutdown(time=5)
        elif 'restart' in query:
             speak('restarting down your PC')
            #  sleep(5)
             os.system('shutdown /r /t /1')
        elif 'terminate yourself' in query or 'terminate' in query:
            quit()


        #in system settings 
        #instagram 
        # elif 'instagram' 
        elif 'search' in query:
            if 'insta id' in query:
                click(x=61, y=287) 
            else:
                query=query.replace("search","")
                speak('searching the results of ' + query)
                google()
                speak("According to google")
                keyboard.type(query)
                press('enter')


        # elif 'insta id' in query:
        elif 'home' in query:
            click(x=56, y=210)
        elif 'reels' in query:
            click(x=61, y=421)
        elif 'messenger' in query:
            click(x=59, y=483)
        elif 'like' in query:
            if 'likes' in query:
                click(x=60, y=558)
            else:
                click(x=670, y=564)
                doubleClick()
        elif 'profile' in query:
            click(x=60, y=685)


   

        #mouse control
        elif 'click' in query:
            if 'left' in query:
                time.sleep(1)
                leftClick()
            elif 'right' in query:
                time.sleep(1)
                rightClick()
            elif 'double' in query:
                time.sleep(1)
                doubleClick()
            elif 'triple' in query:
                time.sleep(1)
                tripleClick()
            else:
                click()

        elif 'activate' in query and 'jarvis' in query:
            print('Activating jarvis......')
            speak('Activating jarvis......')
            time.sleep(2)
            print('Jarvis is ready to work')
            speak('Jarvis is ready to work')

            while True:
                print("Ask jarvis")
            # prompt=takeCommand().lower()
                model_engine="text-davinci-003"
            # prompt=input('Ask JARVIS...')
            # keyboard.type(prompt)
            # prompt==a
                prompt=takeCommand().lower()
                if 'exit' in prompt or 'quit' in prompt in prompt:
                    print('Okay sir,Terminating Jarvis')
                    speak('Okay sir,Terminating Jarvis')
                    print('Activating Friday')
                    speak('Activating Friday')
                    break
                # elif 'jarvis' in query:
                #     speak('yes sir')
                #     print('yes sir')
                # elif 'friday' in query:
                #     speak('Sir I am jarvis, not firday.')
                #     print('Sir I am jarvis, not friday.')
                completion=openai.Completion.create(
                    engine=model_engine,
                    prompt=prompt,
                    max_tokens=1024,
                    n=1, stop=None,
                    temperature=0.5
                )
                response=completion.choices[0].text
                print(response)
                print('Should I speak the result?')
                speak('Should I speak the result?')
                query=takeCommand().lower()
                if 'speak' in query or 'yes' in query:
                    speak(response)
                elif 'no' in query:
                    break 
                # if 'jarvis' in query:
                #     speak('yes sir')
                #     print('yes sir')
                # if 'friday' in query:
                #     speak('Sir I am jarvis, not firday.')
                #     print('Sir I am jarvis, not friday.')
            


    # else :
    #      speak('Sir. R U there, sir ?') type