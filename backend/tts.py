from gtts import gTTS
import os

input = "test text: Hey. Welcome to EchoNotes."
tts = gTTS(text=input, lang='en', slow=False)
tts.save("response.mp3")
os.system("mpg123 response.mp3") # brew install mp123
