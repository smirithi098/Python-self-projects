import html


class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0
        self.question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.question.question)
        return f"{q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
