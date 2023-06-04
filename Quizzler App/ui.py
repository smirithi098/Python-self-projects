from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 15, "normal"),
                                 pady=20)
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Question", fill="black",
                                                     font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2)
        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.click_true)
        self.true_btn.grid(column=0, row=2, pady=20)
        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.click_false)
        self.false_btn.grid(column=1, row=2, pady=20)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def click_true(self):
        is_answer_correct = self.quiz.check_answer("True")
        self.update_result(is_answer_correct)

    def click_false(self):
        is_answer_correct = self.quiz.check_answer("False")
        self.update_result(is_answer_correct)

    def update_result(self, is_correct_answer):
        if is_correct_answer:
            self.score_label["text"] = f"Score: {self.quiz.score}"
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
