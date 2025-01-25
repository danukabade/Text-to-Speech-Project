from gtts import gTTS
from playsound import playsound

file = open("abc.txt", "r").read()
speech = gTTS(text=file, lang='en', slow=False)
speech.save("voice.mp3")

# Play the audio file
playsound("voice.mp3")
