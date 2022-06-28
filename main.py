from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800,800)
screen.bgcolor("black")
screen.tracer(0)

def up_player_two():
    paddleOne.sety(paddleOne.ycor()+20)

def down_player_two():
    paddleOne.sety(paddleOne.ycor()-20)

def up_player_one():
    paddleTwo.sety(paddleTwo.ycor()+20)

def down_player_one():
    paddleTwo.sety(paddleTwo.ycor()-20)

paddleOne = Paddle(350,0)

paddleTwo = Paddle(-350,0)

ball= Ball()


screen.listen()
screen.onkey(up_player_two, "Up")
screen.onkey(down_player_two, "Down")
screen.onkey(up_player_one, "w")
screen.onkey(down_player_one, "s")

game_on = True

def gameover(game_on):
    if (ball.xcor() > 400):
        game_on = False
        screen.bye()
        print("game over. Player One wins!")
    elif (ball.xcor() < -400):
        game_on = False
        screen.bye()
        print("game over. Player One wins!")

while game_on:
    time.sleep(0.05)
    screen.update()
    ball.run()

    if (ball.ycor() > 400 or ball.ycor()< -400):
        ball.reflect_border()

    if (ball.distance(paddleOne) <50 or ball.distance(paddleTwo) <50):
        ball.reflect_paddle()

    gameover(game_on)


screen.exitonclick()