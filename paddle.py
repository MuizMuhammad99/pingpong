from turtle import Turtle, Screen

class Paddle(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(6, 0.6, 1)
        self.penup()
        self.goto(x, y)