import pyjokes
import pyttsx3
jokes = pyjokes.get_joke()
speaker = pyttsx3.init()
speaker.say(jokes)
speaker.runAndWait()