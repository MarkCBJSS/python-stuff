# Simple Snake game by @TokyoEdTech
# https://www.youtube.com/watch?v=BP7KMlbvtOo&list=PLlEgNdBJEO-n8k9SR49AshB9j7b5Iw7hZ
# With tweaks by me

import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Snack timer
seconds = 1

# Set-up the screen
wn = turtle.Screen()
wn.title("~ Snake ~")
wn.bgcolor("green")
wn.setup(600, 600)
wn.tracer(0)

# Snake Head
head = turtle.Turtle()
head.speed(5)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))
pen.goto(0, -280)
pen.write("High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def score_writer():
    pen.clear()
    pen.goto(0, 260)
    pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
    pen.goto(0, -280)
    pen.write("High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal"))

# Box for the timer to be drawn on
def draw_timer_box():
    tb = turtle.Turtle()
    tb.hideturtle()
    tb.color("white")
    tb.penup()
    tb.goto(-20, 20)
    tb.pendown()
    tb.begin_fill()
    for side in range(4):
        tb.fd(40)
        tb.rt(90)
    tb.end_fill()

# Countdown for player not eating a snack
def run_snack_timer():
    rst = turtle.Turtle()
    rst.hideturtle()
    rst.penup()
    rst.goto(0, -15)
    rst.pendown()
    rst.color("red")

    global seconds
    if seconds < 5:
        rst.write(str(seconds), align="center", font=("Courier", 25, "normal"))
        print(seconds)
        seconds += 1

    turtle.ontimer(rst.clear, 1000)
    turtle.ontimer(run_snack_timer, 1000)

def add_new_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("orange")
    new_segment.penup()
    segments.append(new_segment)

def move_end_segment_first():
    # move the end segment first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    draw_timer_box()

    run_snack_timer()

    # else: # if the timer expires, reset the game
    #     for eachSegment in segments:
    #         eachSegment.goto(1000, 1000)
    #
    #     # Clear the segments list
    #     segments.clear()
    #
    #     # Reset the score
    #     score = 0
    #     score_writer()

    # Check for collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide the segments
        # Doesn't seem to be a way to wipe segments within Turtle
        for eachSegment in segments:
            eachSegment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0
        score_writer()

    # Check for snake head colliding with food
    if head.distance(food) < 20:
        # move food to random location on the screen
        x = random.randrange(-280, 280, 20) # because the screen is 300 x 300
        y = random.randrange(-280, 280, 20)
        food.goto(x, y)
        # or just
        # food.goto(random.randint(-290, 290), random.randint(-290, 290))

        # Add a new segment
        add_new_segment()

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        score_writer()

    move_end_segment_first()


    # move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision on body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide the segments
            # Doesn't seem to be a way to wipe segments within Turtle
            for eachSegment in segments:
                eachSegment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # reset the score
            score = 0

            # reset the delay
            delay = 0.1

            # Update the score display
            score_writer()

    time.sleep(delay)

wn.mainloop()