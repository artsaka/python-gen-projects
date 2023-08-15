# run the program
from question import Question
from data import question_data
from controller import Controller
from quizUI import UserInterface

all_questions = []

for item in question_data:
    text = item["text"]
    answer = item["answer"]
    quest = Question(text, answer)
    all_questions.append(quest)


#Using controller
controller = Controller(all_questions)
# while controller.hasQuestion():
#     controller.nextQuestion()

user_interface = UserInterface(controller)