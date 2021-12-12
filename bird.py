from turtle import Turtle


class Bird(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.goto(-350, 0)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 30)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 30)

