from tkinter import *
from pytube import YouTube
from moviepy.editor import *

def downloadBtn():
    #URL's path
    video_path = link.get()
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)
    video_clip.close()

# create an instance of Tkinter's tk class
root =  Tk()
root.title("YouTube Downloader")
canvas = Canvas(root, width=400, height=200)
canvas.pack() # add widget to a window

# Widget Label of the program's name
app_title = Label(root, text="Download Video", font=('Arial', 20, 'bold'))
# put the title into the root window
canvas.create_window(200, 30, window=app_title)


# input link and download buttons
label_link = Label(root, text="Input a url from YouTube:")
canvas.create_window(200, 80, window=label_link)
link = Entry(root, width=60)
canvas.create_window(200, 100, window=link)

# using command to handle download's event
download_btn = Button(text="download", command=downloadBtn)
canvas.create_window(200, 150, window=download_btn)


root.mainloop()