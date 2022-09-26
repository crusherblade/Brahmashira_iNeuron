import imp
import datetime
from speak import Say
# FUNCTION

# 2TYPES

# 1 - NON INPUT
def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)

def NonInputExecution(query):

    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()
    
    elif "day" in query:
        Day()
    

# 2 - INPUT

def InputExecution(tag, query):
    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about", "").replace("tell me about","").replace("what is the", "").replace("wikipedia", "").replace("can you explain about", "").replace("explain", "").replace("tell me more", "")
        import wikipedia
        result = wikipedia.summary(name)
        Say(result)

    elif "google" in tag:
        query = str(query).replace("google","")
        query = query.replace("search","")
        import pywhatkit
        pywhatkit.search(query)