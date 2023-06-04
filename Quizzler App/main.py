from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
from ui import QuizInterface

question_bank = []

for item in question_data:
    new_q = Question(item['question'], item['correct_answer'])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
