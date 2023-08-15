from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *

root = Tk()
root.title("My GUI")
root.geometry("500x500")

def selectColor():
    color = askcolor()
    # print(color[0], color[1])
    clr_label = Label(text="Color selected!", bg=color[1]).pack()

def selectFile():    
    file = askopenfilename()
    content = open(file, encoding="utf8")
    file_path_label = Label(text=file).pack()
    file_content_label = Label(text=content.read()).pack()

btn1 = Button(text="Choose color", command=selectColor).pack()
btn2 = Button(text="Choose file", command=selectFile).pack()
root.mainloop()