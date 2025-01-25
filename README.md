# Text-to-Speech 
A simple project to convert text to speech using gTTS.

## Description
This project converts text from a file into speech using the gTTS (Google Text-to-Speech) library. The speech is saved as an MP3 file and played automatically.

### Features
- Reads text from a file (`abc.txt`).
- Converts the text to speech using gTTS.
- Saves the output as an audio file (`voice.mp3`).
- Plays the audio automatically.
### Prerequisites
- Python installed on your system.
- Required libraries:
  - gTTS
  - playsound
- To install the required libraries, run:
   pip install gtts playsound
### How to Use
1. Place the text you want to convert to speech in a file named `abc.txt`.
2. Ensure `abc.txt` is in the same directory as the Python script.
3. Run the script using the following command:
   ```bash
   python texttospeech_name.py
### Code
```python
from gtts import gTTS
from playsound import playsound

file = open("abc.txt", "r").read()
speech = gTTS(text=file, lang='en', slow=False)
speech.save("voice.mp3")

# Play the audio file
playsound("voice.mp3")




