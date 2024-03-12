from gtts import gTTS
import os
abc=open('G:\Python-Journey\Text_2_voice\sample.text')

text=abc.read()

#text = 'hello maddy how are you?'

language = 'en'

obj=gTTS(text=text ,lang=language , slow=False)

obj.save('sample.mp3')

os.system("sample.mp3")