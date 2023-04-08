import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import getpass


# Initialize the speech recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define a function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to handle voice commands
def handle_command(command):
    if "open destiny item manager" in command or "open manager" in command: 
        path = r"C:\Users\Zach\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Apps\Destiny Item Manager.lnk"
        os.startfile(path)
        speak("Opening Destiny item manager.")
    elif "ai search" in command:
        # Extract the search query from the command
        search_query = command.replace("ai search", "")
        # Use the webbrowser module to perform a Google search
        url = "https://chat.openai.com/chat/" + search_query
        webbrowser.get().open(url)
        speak(f"Here are the search results for {search_query}.")
    elif "search google for" in command:
        # Extract the search query from the command
        search_query = command.replace("search google for", "")
        # Use the webbrowser module to perform a Google search
        url = "https://www.google.com/search?q=" + search_query
        webbrowser.get().open(url)
        speak(f"Here are the search results for {search_query}.")
    elif "open destiny" in command:
        # Runs Destiny 2 on command 
        path = r"C:\Users\Zach\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Steam\Destiny 2.url"
        os.startfile(path)
        speak("Opening Destiny 2.")
    elif "open discord" in command:
        # Runs Discord on command 
        path = r"C:\Users\Zach\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk"
        os.startfile(path)
        speak("Opening Discord.")
        #Runs apex
    elif "open apex" in command:
        path = r"C:\Users\Zach\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Steam\Apex Legends.url"
        os.startfile(path)
        speak("opening apex")
        #Opens spotify 
    elif "open spotify" in command:
        path = r
        
    elif "stop" in command:
        stop()
    else:
        speak("Sorry, I didn't understand that command.")

# Define a function to stop the program
def stop():
    speak("Stopping.")
    exit()

# define the trigger phrase
trigger_phrase = "assistant"
# wait for trigger phrase
while True:
    with sr.Microphone() as source:
        print("Listening for trigger phrase...")
        audio = r.listen(source)
    try:
        # recognize speech using Google Speech Recognition
        trigger = r.recognize_google(audio)
        print(f"Trigger phrase: {trigger}")
        if trigger == trigger_phrase:
            speak("Yes?")
            break
    except sr.UnknownValueError:
        print("Could not understand audio")

# listen for command
while True:
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = r.listen(source)
    try:
        # recognize speech using Google Speech Recognition
        command = r.recognize_google(audio)
        print(f"Command: {command}")
        handle_command(command.lower())
    except sr.UnknownValueError:
        print("Could not understand audio")

# Run on startup
    USER_NAME = getpass.getuser()
    def add_to_startup(file_path=r"C:\Users\Zach\OneDrive\Desktop\Voice_Recognition\Voice_Recognition.py"):
        if file_path == r"C:\Users\Zach\OneDrive\Desktop\Voice_Recognition\Voice_Recognition.py":
            file_path = os.path.dirname(os.path.realpath(__file__))
            bat_path = r'C:\Zach\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
            bat_file.write(r'start "" "%s"' % file_path)