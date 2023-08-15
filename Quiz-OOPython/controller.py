class Controller:
    def __init__(self, data):
        self.question_list = data
        self.question_number = 0
        self.score = 0
        # running question text 
        self.current = None

    def nextQuestion(self):
        self.current = self.question_list[self.question_number]
        self.question_number += 1
        # print(self.question_number,")", current.text, "(True/False)")
        # user_answer = input("Your answer (true or false) : ")
        # self.checkAnswer(user_answer, current.answer)
        return f"{self.question_number}) {self.current.text}"
        

    def hasQuestion(self):
        return self.question_number < len(self.question_list)
    
    def checkAnswer(self, user_input):
        # using the global current question text
        correct_answer = self.current.answer
        if(user_input.lower() == correct_answer.lower()):
            # receive score
            self.score += 1
            # print("Score = ", self.score)
            return True
        else:
            return False
            # print("Your answer is incorrect.")
            # print("Answer: ", correct_answer)
