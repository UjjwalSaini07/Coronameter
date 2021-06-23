# importing the necessary libraries.
import pyttsx3
import pywhatkit as kit
import datetime
import speech_recognition as sr
import wikipedia
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import webbrowser
import sys
import mysql.connector
py = sys.executable
#init_ing the speech engine here.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice', voices[0].id) #MS david voice.
engine.setProperty('rate', 185)
#creating the text to speech conversion function here.
def speak(audio):
    '''
    this function will perform text to speech conversion.
    it will work offline and it uses the microsoft voices for the tts conversion.
    in the audio perimeter we have to pass the text and it will play as audio in ms david voice.
    '''
    engine.say(audio)
    engine.runAndWait()
def wish_me():
    '''
    this will make the voice assistant to greet me according to the time and hour.
    if the hour is from 0 to less than 12 then it means (morning.)
    '''
    current_datetime = datetime.datetime.now() #getting the current datetime.
    current_hour = int(current_datetime.hour) #extract the hour from the datetime.
    if current_hour == 0 and hour < 12:
        speak("Good Morning!")
    elif current_hour >= 12 and current_hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    #after checking the conditions it will come out here.
    speak("I am Your Chat-Buddy, How May I Help You?")
def get_engaudio():
    '''
    this function will take the command of the user, from the microphone and recognise the user's speech.
    after the speech is processed it can capable of producing the quality output for the command.
    it will return the command output as a string.
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak('i am listening')
        audio = r.listen(source)
        user_voice = ""
        try:
            user_voice = r.recognize_google(audio, language = 'en-in')
            return user_voice
        except Exception as audio_not_recognised:
            speak("Sorry, i Can't get that")
            print(audio_not_recognised)
def call_me():
    # storing the user voice returned value here.
    audioquery = get_engaudio()
    print(audioquery)
    # creating the keywords.
    key_word_1 = 'wikipedia'
    key_word_2 = 'the time'
    key_word_3 = 'the date'
    key_word_4 = 'your developer'
    key_word_5 = 'your name'
    key_word_6 = 'youtube'
    key_word_7 = 'open mail'
    key_word_8 = 'google'
    key9 = "how can you help me"
    key10 = "what is your work"
    key11 = "tell me about yourself"
    # handling the exception that the user is connected to internet or not.
    if audioquery == None:
        speak("Make Sure You Are Connected To The Internet!")
    else:
        # creating the logic for the response based on the user audioquery.
        audioquery = audioquery.lower()  # lowercase for better search results.
        # checking the keywords in the audioquery and make responses.
        if key_word_1 in audioquery:
            try:
                speak('Searching Wikipedia...')
                audioquery = audioquery.replace(key_word_1, '')
                results = wikipedia.summary(audioquery, sentences=2)
                print(results)
                speak(f'According To Wikipedia {results}')
            except Exception as e:  # this will handle the
                speak(
                    'i am confused,please confirm that your audioquery is suitable for wikipedia or otherwise provide me some unique keywords to search.')
        elif key_word_2 in audioquery:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time)
            speak(f'The Current Time Is {current_time}')
        elif key_word_6 in audioquery:
            speak('Your YouTube Video Is Loaded Successfully.')
            kit.playonyt(audioquery)
        elif key_word_7 in audioquery:
            speak('G-Mail Opened Successfully.')
            webbrowser.open('www.gmail.com')
        elif key_word_8 in audioquery:
            qlist = audioquery.split()
            qlist.remove('search')
            qlist.remove('on')
            qlist.remove('google')
            search = ''
            for word in qlist:
                search += word + '+'
            print(search)
            webbrowser.open(f'https://www.google.com/search?q={search}')
            speak('Google Opened Successfully.')
        elif 'bye' in audioquery:
            speak("goodbye, it's very nice to talk with you")
        elif 'thank you' in audioquery:
            speak("welcome, it's my pleasure, to serve you the best.")
        elif key_word_4 in audioquery:
            speak('My Sir, Mr. Abhijit Mandal Developed Me')
        elif key_word_5 in audioquery:
            speak('My Name Is ChatBuddy, Your Personalised Assistant.')
        elif key_word_3 in audioquery:
            current_date = datetime.date.today()
            print(current_date)
            speak(current_date)
        elif key9 in audioquery:
            speak("You can ask me many questions or queries, i will try to answer those question at my best.")
        elif key10 in audioquery:
            speak("My work is to answer your all queries regarding to covid-19 virus and many more.")
        elif key11 in audioquery:
            speak("my name is chatbuddy your personalized assistant, my age doesn't matter actually but my knowledge does, you can ask me anything i will answer you that's for sure.")
        else:
            speak("sorry, i can't get that.")
def asktobot():
    # storing the user typed returned value here.
    typedquery = entryvar.get()
    # showing the asked query to the screen.
    chatbox.insert(END, "You : " + typedquery)
    print(typedquery)
    # creating the keywords.
    key_word_1 = 'wikipedia'
    key_word_2 = 'the time'
    key_word_3 = 'the date'
    key_word_4 = 'your developer'
    key_word_5 = 'your name'
    key_word_6 = 'open youtube'
    key_word_7 = 'open mail'
    key_word_8 = 'on google'
    key_word_9 = 'on youtube'
    # handling the exception that the user is connected to internet or not.
    if typedquery == None:
        speak("Make Sure You Are Connected To The Internet!")
    else:
        # creating the logic for the response based on the user typedquery.
        typedquery = typedquery.lower()  # lowercase for better search results.
        # checking the keywords in the typedquery and make responses.
        if key_word_1 in typedquery:
            try:
                speak('Searching Wikipedia...')
                typedquery = typedquery.replace(key_word_1, '')
                results = wikipedia.summary(typedquery, sentences=2)
                chatbox.insert(END, f'ChatBuddy : {results}')
                speak(f'According To Wikipedia {results}')
            except Exception as e:  # this will handle the
                speak('i am confused,please confirm that your typedquery is suitable for wikipedia or otherwise provide me some unique keywords to search.')
        elif key_word_2 in typedquery:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time)
            speak(f'The Current Time Is {current_time}')
            chatbox.insert(END, f"ChatBuddy : The Current Time Is {current_time}")
        elif key_word_3 in typedquery:
            current_date = datetime.date.today()
            print(current_date)
            speak(current_date)
            chatbox.insert(END, f"ChatBuddy : {current_date}")
        elif key_word_6 in typedquery:
            speak('Youtube Opened Successfully.')
            chatbox.insert(END, "ChatBuddy : Youtube Opened Successfully.")
            webbrowser.open('www.youtube.com')
        elif key_word_7 in typedquery:
            speak('G-Mail Opened Successfully.')
            chatbox.insert(END, "ChatBuddy : G-Mail Opened Successfully.")
            webbrowser.open('www.gmail.com')
        elif key_word_8 in typedquery:
            qlist = typedquery.split()
            qlist.remove('search')
            qlist.remove('on')
            qlist.remove('google')
            search = ''
            for word in qlist:
                search += word + '+'
            print(search)
            webbrowser.open(f'https://www.google.com/search?q={search}')
            speak('Google Opened Successfully.')
            chatbox.insert(END, "ChatBuddy : Google Opened Successfully.")
        elif key_word_9 in typedquery:
            kit.playonyt(typedquery)
            speak('Your Video Is Loaded successfully.')
            chatbox.insert(END, "ChatBuddy : youtube opened successfully.")
        elif 'bye' in typedquery:
            speak("goodbye, it's very nice to talk with you")
            chatbox.insert(END, "ChatBuddy : goodbye, it's very nice to talk with you")
        elif 'thank you' in typedquery:
            chatbox.insert(END, "ChatBuddy : welcome, it's my pleasure, to serve you the best.")
            speak("welcome, it's my pleasure, to serve you the best.")
        elif 'hi' in typedquery:
            chatbox.insert(END, "ChatBuddy : Hello i am your chatbuddy, how may i help you?")
            wish_me()
        elif key_word_5 in typedquery:
            chatbox.insert(END, "ChatBuddy : My Name Is ChatBuddy, Your Personalised Assistant.")
            speak('My Name Is ChatBuddy, Your Personalised Assistant.')
        elif key_word_4 in typedquery:
            chatbox.insert(END, "ChatBuddy : My Sir, Mr. Abhijit Mandal Developed Me")
            speak('My Sir, Mr. Abhijit Mandal Developed Me')
        else:
            speak("sorry, i can't get that.")
            chatbox.insert(END, "ChatBuddy : sorry, i can't get that")
#creating the window here.
window = Tk()
window.geometry('600x650')
window.resizable(0,0)
window.iconbitmap('iconfile.ico')
window.title("CoronaMeter : The ChatBuddy")
window.configure(bg = '#ffeaa7')
#creating the image here.
botimg = PhotoImage(file = 'robot.png')
label = Label(window, text = 'Click To Start Talking', font = "times 15 bold italic", bg = '#ffeaa7', fg = 'black')
botimage = Button(window, image = botimg, border = 0, relief = FLAT, command = call_me, bg = '#ffeaa7', fg = '#ffeaa7')
botimage.pack(side = TOP, padx = 5, pady = 5, anchor = CENTER)
label.pack(side = TOP, pady = 0, anchor = CENTER)
#creating the frame here for the chats here.
botframe = Frame(window, border = 5, relief = SOLID, bg = '#ffeaa7')
#creating the scrollbar for the chat section here.
scrollbar = Scrollbar(botframe)
#placing the chatbox with the scrollbar here.
chatbox = Listbox(botframe, width = 90, height = 20, bg = "#ffeaa7", fg = 'darkblue', font = 'times 9 bold italic')
scrollbar.pack(side = RIGHT, fill = Y)
chatbox.pack(side = LEFT, fill = BOTH)
botframe.pack()
#creating the entry box here.
entryvar = StringVar()
entry = Entry(window, width = 10, font = 'times 20 bold', textvariable = entryvar, border = 3, relief = SOLID)
entry.pack(side = TOP, padx = 15, pady = 10, fill = X)
#creating the tick or submit button.
askbutton = Button(window, text = "Ask To ChatBuddy", border = 0, relief = FLAT, font = "times 20 bold italic", command = asktobot, fg = 'darkblue', bg = "#ffeaa7")
askbutton.pack(side = BOTTOM, padx = 5, pady = 0, anchor = CENTER)
window.mainloop()
