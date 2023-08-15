from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("My GUI")
root.geometry("500x500")

def showChoice():
    choice=language.get()
    match choice:        
        case 1:
            tkinter.messagebox.showinfo("info", "You choose Python. You can become a Data Scientist!")
                        
        case 2:
            tkinter.messagebox.showinfo("info", "You choose Java. You can become a mobile app developer!")
            
        case 3:
            tkinter.messagebox.showinfo("info", "You choose PHP. You can become a Blockchain developer!")
            
        case 4:
            tkinter.messagebox.showinfo("info", "You choose C#. You can become a game developer!")
             
        case 5:
            tkinter.messagebox.showinfo("info", "You choose JavaScript. You can become a web developer!")
            
        case 6:
            tkinter.messagebox.showinfo("info", "You choose PHP. You can become a backend developer!")
                
        case _:
            print("The language doesn't matter, what matters is solving problems.")

# control selected value 
language = IntVar()
# set default selected language
language.set(1)
Radiobutton(text="Python", variable=language, value=1, command=showChoice).grid(row=0, column=0)
Radiobutton(text="Java", variable=language, value=2, command=showChoice).grid(row=0, column=1)
Radiobutton(text="Solidity", variable=language, value=3, command=showChoice).grid(row=0, column=2)
Radiobutton(text="C#", variable=language, value=4, command=showChoice).grid(row=0, column=3)
Radiobutton(text="JavaScript", variable=language, value=5, command=showChoice).grid(row=0, column=4)
Radiobutton(text="PHP", variable=language, value=6, command=showChoice).grid(row=0, column=5)

root.mainloop()