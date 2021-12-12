import turtle as t
from time import sleep

from bird import Bird
from column import Column

screen = t.Screen()
screen.setup(1000, 600)
screen.bgcolor('black')
screen.title('Flappy bird')
screen.tracer(0)
screen.listen()

bird = Bird()
column = Column()

screen.onkey(bird.up, 'w')
screen.onkey(bird.down, 's')

isGame = True
while isGame:
    screen.update()
    sleep(0.01)


screen.exitonclick()
