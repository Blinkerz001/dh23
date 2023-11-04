import pyttsx3
 
# init function to get an engine instance for the speech synthesis 
engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty('volume', 1)
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)

engine.say("Hello. Turn on for me to describe the surroundings") 
#engine.save_to_file(opencv_response ,'audio.mp3' ) - saves opencv response as a file
engine.runAndWait()


#spelling word option, get word definition from internet option - allows using of tool for learning

#tracking code checks detected changes, if there is a change then the variables are read aloud.
A = 'first'  #j   #tracker data
B = 'second' #j  #tracker data

#position left or right if x<0 say left, x>0 say right. 
engine.say(str(A + B))
engine.runAndWait()
