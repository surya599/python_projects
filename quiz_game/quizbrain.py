class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    def still_has_questions(self):
       if self.question_number < len(self.question_list):
           return True
       else:
           return False
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        useranswer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.checkanswer(useranswer,current_question.answer)
    def checkanswer(self,useranswer,correctanswer):
        if str(useranswer).lower() == str(correctanswer).lower():
            print("you are right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correctanswer}")
        print(f"your current score is {self.score}/{self.question_number}")
          