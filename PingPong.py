
# Simple Pong in Python3
# Part 1: Getting Started

import turtle
import os
from playsound import playsound

wn = turtle.Screen()
wn.title("Pong by KateP")
wn.bgcolor("black")
wn.setup(width=800, height = 600) #size of the window
wn.tracer(0) #stops the window from updating - speed up a game

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0) #speed of animation - sets to max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0) #coordinates of 1st paddle

# Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0) #speed of animation - sets to max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0) #coordinates of 2st paddle

# Ball
ball=turtle.Turtle()
ball.speed(0) #speed of animation - sets to max
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0) #coordinates of the ball - middle
ball.dx = 0.1 #moves by 2 pixels
ball.dy = -0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align = "center", font= ("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


# Main game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        playsound('bounce.mp3', block=False)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        playsound('bounce.mp3', block=False)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        playsound('bounce.mp3', block=False)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        playsound('bounce.mp3', block=False)
