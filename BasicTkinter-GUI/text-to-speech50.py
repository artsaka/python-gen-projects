from tkinter import *
from cgitb import text
from gtts import gTTS

def convertTextToMP3():
    # Get the message
    message =  text_entry.get()
    language = 'th'
    # converts text to speech
    output_speech = gTTS(text=message, lang=language, slow=False)
    output_speech.save("sound.mp3")

panel = Tk()
panel.title("Trans Text to Speech - Thai")
canvas = Canvas(panel, width=400, height=300)
canvas.pack()

app_label = Label(text="Text to Speech", font=('Arial', 25, 'bold'))
canvas.create_window(200,100, window=app_label)

text_entry = Entry(panel)
canvas.create_window(200, 180, window=text_entry)

button = Button(text="Press here (text to speech)", command=convertTextToMP3)
canvas.create_window(200, 230, window=button)


panel.mainloop()