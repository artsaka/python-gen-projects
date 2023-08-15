from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("My GUI")
root.geometry("500x500")

# create menubar panel
myMenu = Menu()
root.config(menu=myMenu)

def showWindow():
    subwindow = Tk()
    subwindow.title("New window")
    subwindow.geometry('300x300')
    subwindow.mainloop()

def aboutProgram():
    tkinter.messagebox.showinfo("Description", "Developer: MacKD")

def exitProgram():
    # alert dialog box
    confirm = tkinter.messagebox.askquestion("Confirm Exit", "Are you sure you want to exit ?")
    if confirm == "yes":
        root.destroy()

# create nested menu dropdown in the menubar
menuitem = Menu()
# clicks "New Window" label to display a sub new window 
menuitem.add_command(label="New Window", command=showWindow)
menuitem.add_command(label="Open")
menuitem.add_command(label="About", command=aboutProgram)
menuitem.add_command(label="Exit", command=exitProgram)


# adding labels to the menubar panel
myMenu.add_cascade(label="File", menu=menuitem)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="View")

# display the main window cursively
root.mainloop()