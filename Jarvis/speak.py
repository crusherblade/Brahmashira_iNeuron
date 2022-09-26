import pyttsx3

# speak function
def Say(Text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)      #to change the voice 
    engine.setProperty('rate', 170)
    print("     ")      #blank line
    print(f"Brahmashira: {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("     ")      #blank line

Say("Hello sir")