import pyttsx3
 
# init function to get an engine instance for the speech synthesis 
engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 0.9)
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)

engine.say("Hello. Turn on for me to describe the surroundings") 
#engine.save_to_file(opencv_response ,'audio.mp3' ) - saves opencv response as a file
engine.runAndWait()


#spelling word option, get word definition from internet option - allows using of tool for learning

#tracking code checks detected changes, if there is a change then the variables are read aloud.
A = j#tracker data
B = j#tracker data

engine.say(str(A + B))
engine.runAndWait()
