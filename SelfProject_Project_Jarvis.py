import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pyjokes
import os
import time

def sptext():#it will take input from us but will not return anything
  while True:
    recognizer = sr.Recognizer() #sr is module name and Recognizer is class name, it is used to store voice in recognizer variable

    with sr.Microphone() as source: #inut through microphone as source

      print("You can talk now, I am Listening...") #It will print while you are talking/commanding/requesting

      recognizer.adjust_for_ambient_noise(source)#noise cancellation i.e. the syntax to remove noise from source

      audio = recognizer.listen(source) #listen from source, it will be stored in audio variable

      try:  #to avoid error displaying we are going to use try catch as if voice is not recognized then it will avoid error and throw exception
        print("Recognizing...")   #display during recognition process

        data = recognizer.recognize_google(audio)   #recognizer function of google sourced from audio
        print(data)
        return data                 #it will print what it recognized using speech recognizer module which we imported

      except sr.UnknownValueError:
        print("Sorry! I did not understand what you said.")

def speechtx(x):
  engine = pyttsx3.init()
  voices = engine.getProperty('voices') #voice is taken #voices indicates two different voices # Voice indicate only one variable
  engine.setProperty('voice', voices[0].id) #Male = 0 or female=1 voice is set
  rate = engine.getProperty('rate')  # To control speed rate is used
  engine.setProperty('rate', 130) #150 is speed, you can use default speed too
  engine.say(x) 			#variable creation for saying
  engine.runAndWait()		#It will say what it say


if __name__ == '__main__':
  if "jarvis" in sptext().lower():
      while True:
        data1 = sptext().lower()

        if "your name" in data1:
          name = "My name is Jarvis."
          speechtx(name)
          speechtx("It's good to hear your voice again Ajinkya sir, How may I help you today")

        elif "old are you" in data1:
          age = "As an AI I am not born. Hence, I can't state my age. However, I was created on 19 April 2023."
          speechtx(age)

        elif "created you" in data1:
          creator = "Ajinkya Pawar created me on 19 April 2023."
          speechtx(creator)

        elif 'time' in data1: #str object has no attribute sleep
          time = datetime.datetime.now().strftime("%I%M%p")
          speechtx(time)

        elif 'youtube' in data1:
          webbrowser.open("https://www.youtube.com/")

        elif 'lowes' in data1:
          webbrowser.open("https://lowes.co.in/")

        elif 'my github profile' in data1:
          webbrowser.open(("https://www.github.com/ajinkyamspawar21"))

        elif 'joke' in data1:
          joke_1 = pyjokes.get_joke(language= "en", category="neutral")
          print(joke_1)
          speechtx(joke_1)

        elif 'song' in data1:
          add = r"D:\1_AJINKYA_PAWAR\8_SONGS"
          listofsongs = os.listdir(add)
          print(listofsongs)
          os.startfile(os.path.join(add, listofsongs[1]))


        elif 'exit' in data1:
          speechtx("Thank You, Sir! See you soon...")
          break

        time.sleep(4)


  else:
    print("I only take orders from Ajinkya Sir")



