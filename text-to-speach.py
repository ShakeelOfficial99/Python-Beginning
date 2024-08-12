from gtts import gTTS
import os

# Text to be converted to speech
text = "Hello! Welcome to the text to speech conversion using gTTS."

# Language in which you want to convert
language = 'en'  # English

# Passing the text and language to the engine
speech = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in an mp3 file
speech.save("output.mp3")

# Playing the converted file (optional)
os.system("start output.mp3")  # On Windows
# os.system("mpg321 output.mp3")  # On Linux
