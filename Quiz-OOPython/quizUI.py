from tkinter import *
from controller import Controller
THEME_APP = '#375362'

class UserInterface:
    def __init__(self, controller: Controller):
        self.controller = controller

        # create instance of the Tk class
        self.window = Tk()
        self.window.title("Quiz program")
        self.window.config(padx=20, pady=20, bg=THEME_APP)

        # display a score at the top-right
        self.scoreLabel = Label(text="Score : 0", fg="white", bg=THEME_APP)
        self.scoreLabel.grid(row=0, column=2)

        # display a question using canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Question is here",
            font=('Arial', 18, 'bold'),
            fill=THEME_APP
        )
        self.canvas.grid(row=1, column=1, columnspan=2, pady=50)

        # Setting two buttons for answer selection 
        true_image = PhotoImage(file="./images/check.png")
        self.true_button = Button(image=true_image, command=self.true_button)
        self.true_button.grid(row=2, column=1)

        false_image = PhotoImage(file="./images/remove.png")
        self.false_button = Button(image=false_image, command=self.false_button)
        self.false_button.grid(row=2, column=2)

        # update the question text using get_next_question() method
        self.get_next_question()

        self.window.mainloop()

    # Displays the actual question text from database via controller module
    def get_next_question(self):
        if self.controller.hasQuestion():
            q_text = self.controller.nextQuestion()
            # update the score
            self.scoreLabel.config(text=f"Score : {self.controller.score}")
            # update the question_text on Canvas
            self.canvas.itemconfig(self.question_text ,text=q_text)
        else:
            # update the last score after end the test
            self.scoreLabel.config(text=f"Score : {self.controller.score}")
            self.canvas.itemconfig(self.question_text, text='End the test')
            
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    # choose answer then hop to the next question    
    def true_button(self):
        self.controller.checkAnswer('True')
        self.waitNextQuestion()
    
    def false_button(self):
        self.controller.checkAnswer('False')
        self.waitNextQuestion()

    def waitNextQuestion(self):
        # wait one second before showing a new question
        self.window.after(1000, self.get_next_question)