# Simple Pong tutorial by @TokyoEdTech
# https://www.youtube.com/playlist?list=PLlEgNdBJEO-kXk2PyBxhSmo84hsO3HAz2
# With some tweaks by me

import turtle
import os
import time

wn = turtle.Screen()
wn.title("~ Simple Pong ~")
wn.bgpic("stars.gif")
wn.setup(800, 600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# ai_in_use = False

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball 1
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("circle")
ball1.color("yellow")
ball1.penup()
ball1.goto(0, 0)
ball1.dx = 3
ball1.dy = -3

# Ball 2
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("circle")
ball2.color("yellow")
ball2.penup()
ball2.goto(0, 0)
ball2.dx = -3
ball2.dy = -3

balls = [ball1, ball2]

# Pen
divide = turtle.Turtle()
divide.hideturtle()
divide.color("white")
divide.goto(0, 240)
divide.goto(0, -220)
divide.goto(0, 0)
divide.begin_fill()
divide.fd(10)
divide.rt(90)
divide.fd(10)
divide.rt(90)
divide.fd(20)
divide.rt(90)
divide.fd(10)
divide.rt(90)
divide.fd(10)
divide.end_fill()
divide.penup()

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 220)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

top_score = turtle.Turtle()
top_score.penup()
top_score.hideturtle()
top_score.color("yellow")
top_score.goto(0, 260)
top_score.write("SCORES", align="center", font=("Courier", 18, "bold"))

help_me = turtle.Turtle()
help_me.penup()
help_me.hideturtle()
help_me.color("yellow")
help_me.goto(0, -260)
help_me.write("Press H key for Help", align="center", font=("Courier", 18, "bold"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def ai_player():
    if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_up()
    elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_down()

def help_screen():
    hlp = turtle.Turtle()
    hlp.color("white")
    hlp.begin_fill()
    hlp.penup()
    hlp.goto(0, 100)
    hlp.pendown()
    hlp.fd(200)
    hlp.rt(90)
    hlp.fd(200)
    hlp.rt(90)
    hlp.fd(400)
    hlp.rt(90)
    hlp.fd(200)
    hlp.rt(90)
    hlp.fd(200)
    hlp.end_fill()

    hlp.color("black")

    hlp.penup()
    hlp.goto(0, 70)
    hlp.pendown()
    hlp.write("Help", align="center", font=("Courier", 24, "normal"))

    hlp.penup()
    hlp.goto(-180, 20)
    hlp.pendown()
    hlp.write("1) Press [a] for AI player", align="left", font=("Courier", 15, "normal"))

    hlp.penup()
    hlp.goto(-180, 0)
    hlp.pendown()
    hlp.write("2) Player A: W = Up, S = Down", align="left", font=("Courier", 15, "normal"))

    hlp.penup()
    hlp.goto(-180, -20)
    hlp.pendown()
    hlp.write("3) Player B: O = Up, K = Down", align="left", font=("Courier", 15, "normal"))

    hlp.hideturtle()
    hlp.penup()
    timer = turtle.Turtle()
    timer.hideturtle()
    timer.penup()
    timer.goto(0, -90)
    timer.pendown()
    timer.color("red")
    timer.write("Playing in [ 3 ]", align="center", font=("Courier", 18, "normal"))
    time.sleep(1)
    timer.clear()
    timer.write("Playing in [ 2 ] ", align="center", font=("Courier", 18, "normal"))
    time.sleep(1)
    timer.clear()
    timer.write("Playing in [ 1 ]", align="center", font=("Courier", 18, "normal"))
    time.sleep(1)
    timer.clear()
    hlp.clear()

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "o")
wn.onkeypress(paddle_b_down, "k")
wn.onkeypress(help_screen, "h")

if wn.onkeypress(ai_player, "a"):
    ai_in_use = True
    while ai_in_use:
        ai_player()

# Main Game Loop
while True:
    wn.update()

    for ball in balls:
        # Move the Ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # BOTTOM Border Check
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            os.system("afplay bounce.wav&")

        # TOP Border Check
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            os.system("afplay bounce.wav&")

        # RIGHT Border Check
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            os.system("afplay bounce.wav&")

        # LEFT Border Check
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            os.system("afplay bounce.wav&")

        # Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
            ball.setx(340)
            ball.dx *= -1
            os.system("afplay strong-punch.wav&")

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
            ball.setx(-340)
            ball.dx *= -1
            os.system("afplay strong-punch.wav&")
