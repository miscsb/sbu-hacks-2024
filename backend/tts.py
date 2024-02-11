from gtts import gTTS
import os

input = "test text: I am a blue kangaroo and I have homosexual tendencies and I love rice pudding. I would like sam to glaze me with peanut butter and push his commit into my git's gyat."
tts = gTTS(text=input, lang='en', slow=False)
tts.save("response.mp3")
os.system("mpg123 response.mp3") # brew install mp123