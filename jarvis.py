from ssl import ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION
import pyttsx3      #speech processing module
import datetime     #module for date and time
import speech_recognition as sr     #module for speech_recognition
import wikipedia #wikipedia module to access wikipedia
import webbrowser # module used to open websites in browser through python
import os #module used to task in the system

engine=pyttsx3.init('sapi5') #sapi5 is used for speech processing by windows
voices=engine.getProperty('voices') #getting voice property
engine.setProperty('voices',voices[1].id)#used to set specific voice



def speech(audio): #function used to input and output audio
    engine.say(audio)
    engine.runAndWait()

def wishme():   #used to wish the user
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speech('Good Morning,I am Jarvis,your support assistant, how may I help You')
        


    elif hour>12 and hour<18:
        speech('Good Afternoon,I am Jarvis,your support assistant, how may I help You')


    elif hour>18 and hour<21:
        speech('Good Evening,I am Jarvis,your support assistant, how may I help You')
   
    else:
        speech('Hey,How are you,I am Jarvis,your support assistant, how may I help You')

    

def audio_command(): #used to get audio command from the user and gives as string output
    voice_recog=sr.Recognizer() #speech recognizer module
    
    with sr.Microphone() as in_voice:     #takes input from microphone
        print('I am listening......')
        voice_recog.pause_threshold=1   #max time python listen once i stop input
        audio_in=voice_recog.listen(in_voice)   #audio_input
    
    try:    #this is used if the python fails to recognize
        print('I am searching......')
        query=voice_recog.recognize_google(audio_in, language="en-in")
        print(f'You said:{query}\n') #gives back the string of given input
    
    except Exception as e:
        print('Can You say it Again....')   #if it don't recognize this msg is given
        return 'None'
    return query


if __name__=="__main__":
    wishme()
    task=audio_command().lower()

    if 'wikipedia' in task: #search something in wikipedia
        speech('According to Wikipedia')
        task=task.replace('wikipedia','')
        results= wikipedia.summary(task,sentences=3)
        speech('Wikipedia Says.....')
        print(results)#first prints the text and speaks  
        speech(results)

    elif 'open youtube' in task: # open youtube
        webbrowser.open_new_tab('https://www.youtube.com')

    elif 'open gmail' in task: # open youtube
        webbrowser.open_new_tab('https://www.gmail.com')

    elif 'open hackerrank' in task: # open youtube
        webbrowser.open_new_tab('https://www.hackerrank.com/')

    elif 'time' in task:#jarvis tell me the time
        pr_time=datetime.datetime.now().strftime('%H:%M:%S')
        speech(f'Sir the clock is showing me{pr_time}')

    elif 'vs code' in task:#opens vscode
        vscode="D:\Microsoft VS Code\Code.exe"
        os.startfile(vscode)
    
  


'''
its not a limit for Jarvis to stop , you can add still more functionalities like sending a mail,opening a audio file or vedio file,make payments for now this enough'''
