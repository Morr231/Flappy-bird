import random
from turtle import Turtle


class Column(Turtle):

    def __init__(self):
        super().__init__()
        self.body = []
        self.create_body()
        self.goto_random()

    def add_part(self):
        self.shape('square')
        self.penup()
        self.color('white')
        self.goto(-20, 0)

    def create_body(self):
        for i in range(random.randint(1, 5)):
            self.body.append(self.add_part())

    def goto_random(self):
        self.goto(0, 250)
