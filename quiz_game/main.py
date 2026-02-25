from data import question_data
from question_model import Question
from quizbrain import QuizBrain
import random
choice = random.choice(question_data)


question_bank = []
for question in question_data:
    questiontext = question["text"]
    questionanswer = question["answer"]
    new_question = Question(questiontext,questionanswer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("you have finished the quiz")
print(f"your final score is {quiz.score}/{quiz.question_number}")