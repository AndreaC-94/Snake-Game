from turtle import Turtle
import random as rd


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_pos = rd.randint(-14, 14) * 20
        y_pos = rd.randint(-14, 14) * 20
        self.goto(x_pos, y_pos)


