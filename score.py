from turtle import Turtle
FONT = ("Courier", 14, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)

    def update(self):
        self.points += 1

    def show(self):
        self.clear()
        self.write(f"Score: {self.points}", move=False, align="center", font=FONT)

    def endgame(self):
        self.color("green")
        self.home()
        self.write(f"Game over\nYour score is: {self.points}", move=False, align="center", font=FONT)
