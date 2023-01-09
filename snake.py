from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(self.segments[-1].pos())
        self.segments.append(new_segment)

    # def tail_collision(self):
    #     for i in range(1, len(self.segments) - 1):
    #         if self.segments[0].distance(self.segments[i]) < 10:
    #             return True
    #     return False

    def tail_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False
