from turtle import Turtle, Screen


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(1, 1, 1)
        self.penup()
        self.x = 10
        self.y = 5

    def run(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def reflect_border(self):
        self.y = self.y * (-1)

    def reflect_paddle(self):
        self.x = self.x * (-1)