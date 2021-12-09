## Run this command in terminal  before executing this program
## rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
## and also run this in seperate terminal
## rasa run actions

import requests
import speech_recognition as sr
import pyttsx3 
#from gtts import gTTS
#from translate import Translator
#from playsound import playsound 

#translator = Translator(to_lang='hi')

converter = pyttsx3.init() 
converter.setProperty('rate', 120) 
converter.setProperty('volume', 0.8) 
voices = converter.getProperty('voices')
converter.setProperty('voice', voices[1].id)
  
rec = sr.Recognizer()

print("Hello, I am Miwo - your work assistant")
converter.say("Hello, I am Miwo - your work assistant")
converter.runAndWait()

"""
converter.say("Hello, Please choose one language - Hindi or English?")
myobj = gTTS(text=translator.translate("Hello, Please choose one language - Hindi or English?"), lang="hi")
myobj.save("welcome.mp3")
playsound("welcome.mp3")
converter.runAndWait() 
with sr.Microphone(device_index=0) as source:
    print("Hello, Please choose one language - Hindi or English? MiWo is Listening...")
    la = rec.listen(source)
    inlang = rec.recognize_google(la, language="en-in")
"""


bot_message = ""
message = ""

while(bot_message != "Thank you for using my services, have a great day!" or message != "Bye" or message!="thanks" or message!="thank you"  or message != "bye" or message!="thankyou"  or message!="Thankyou"):
    with sr.Microphone(device_index=0) as source:
        print("MiWo is Listening...")
        message = rec.listen(source)
        
    try:
        query = rec.recognize_google(message, language="en-in")
        print("You Said : {}".format(query))
        r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message":query})
            
        for i in r.json():
            print("MiWo Said : {}".format(i['text']))
            bot_message = i['text']
            converter.say(bot_message)
            converter.runAndWait() 

    except Exception as e:
        print("Sorry, I could not recognize your voice")    # In case of  voice not recognized  clearly
        converter.say("Sorry, I could not recognize your voice")
        converter.runAndWait()




"""
if(inlang=="English" or inlang=="english"):
    while(bot_message != "Bye" or bot_message!='thanks'):
        with sr.Microphone(device_index=0) as source:
            print("MiWo is Listening...")
            message = rec.listen(source)

        try:
            query = rec.recognize_google(message, language="en-in")
            print("You Said : {}".format(query))
            r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message":query})
            
            for i in r.json():
                print("MiWo Said : {}".format(i['text']))
                bot_message = i['text']
                converter.say(bot_message)
                converter.runAndWait() 

        except Exception as e:
            converter.say(e)
            converter.runAndWait()

else:
    while(bot_message != "Bye" or bot_message!='thanks'):
        with sr.Microphone(device_index=0) as source:
            print("MiWo is Listening...")
            message = rec.listen(source)

        try:
            query = rec.recognize_google(message, language="hi-in")
            print("You Said : {}".format(query))
            r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message":query})
            
            for i in r.json():
                print("MiWo Said : {}".format(i['text']))
                bot_message = i['text']
                myobj = gTTS(text=bot_message, lang="hi")
                myobj.save("welcome.mp3")
                playsound("welcome.mp3")
                converter.runAndWait() 

        except Exception as e:
            converter.say(e)
            converter.runAndWait()

"""             
"""

import requests
import speech_recognition as sr     # import the library
import subprocess
from gtts import gTTS
from translate import Translator
from playsound import playsound 

bot_message = ""
message=""

translator = Translator(to_lang='hi')

def start: 
	myobj = gTTS(text="Hello, Please choose one language - Hindi or English?")
	myobj.save("welcome.mp3")
	print('saved')
	playsound("welcome.mp3")

	myobj = gTTS(text=translator.translate("Hello, Please choose one language - Hindi or English?"), lang="hi")
	myobj.save("welcome.mp3")
	print('saved')
	playsound("welcome.mp3")

start()

r = sr.Recognizer()  # initialize recognizer
with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
    audio = r.listen(source)  # listen to the source
    try:
        message = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
    except:
        print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
if len(message)==0:
   start()

if(message=="English")



r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})

print("Bot says, ",end=' ')
for i in r.json():
    bot_message = i['text']
    print(f"{bot_message}")

myobj = gTTS(text=translator.translate("bot_message"), lang="hi")
myobj.save("welcome.mp3")
print('saved')
# Playing the converted file
playsound("welcome.mp3")

#subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])

while bot_message != "Bye" or bot_message!='thanks':

    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        try:
            message = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
            translator = Translator(to_lang='en')
            print("You said : {}".format(translator.translate(message)))

        except:
            print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
    if len(message)==0:
        continue
    print("Sending message now...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

    print("Bot says, ",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    myobj = gTTS(text=translator.translate("hello, how are you?"), lang="hi")
    myobj.save("welcome.mp3")
    print('saved')
    # Playing the converted file
    playsound("welcome.mp3")
    #subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])
"""