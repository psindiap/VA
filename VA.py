import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener=sr.Recognizer()
engine=pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
  engine.say(text)
  engine.runAndWait()
def take_command():
   try:
     with sr.Microphone() as source:

        print("Listening....\n")

        voice=listener.listen(source)
        command = listener.recognize_google(voice)
        command=command.lower()

   except:
      pass
   return command

def run():
    command=take_command()

    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk("Playing "+song)
        print("Playing " + song+"\n")
        pywhatkit.playonyt(song)

    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,2)
        print(info+"\n")
        talk(info)

    elif 'hello' in command:
        print("Hello\n ")
        talk("Hello")

    elif 'joke' in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'ok' in command:
        talk("Great!")
        print("Great!")

    elif 'Haha' in command:
        talk("Why, Thank You!")
        print("Why, Thank You!")

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I %M %p')
        talk('The time is '+time)
        print(time+"\n")
    elif 'date' in command:
        date=datetime.datetime.now().strftime('%d %B %Y')
        talk('The date today is '+date)
        print(date+"\n")
    elif 'day' in command:
            day = datetime.datetime.now().strftime('%A')
            talk('Today is ' + day)
            print(day + "\n")
    elif "what is" in command:
        thing=command.replace('what is','')
        info=wikipedia.summary(thing,2)
        print(info+"\n")
        talk(info)
    elif "where is" in command:
        thing=command.replace('where is','')
        info=wikipedia.summary(thing,2)
        print(info+"\n")
        talk(info)
    elif "cancel" in command:
        print("Sure, Cancelled that.")
        talk("Sure, Cancelled that.")



    else:
        print("Please rephrase your command\n")
        talk("Please rephrase your command")



while (1):
 run()




























