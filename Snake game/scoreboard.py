from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.hideturtle()
        self.penup()
        self.goto(-15, 270)
        self.pencolor("White")
        self.update_score()

    def read_high_score(self):
        with open("data.txt", mode="r") as file:
            return int(file.read())

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def write_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
