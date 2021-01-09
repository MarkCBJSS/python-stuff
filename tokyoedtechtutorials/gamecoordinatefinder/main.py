# ---------------------------  ABOUT  -------------------------------------
# Turtle Game Grid Co-ordinate Calculator
# Inspired for use in placing items related to @TokyoEdTech tutorials
# https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg
# Written by @MarkCTest - free to use in any way without attribution

# --------------------------  WHY THIS  -----------------------------------
# Co-ordinates are calculated from the top left, which is the 'system' 0-0
# Turtle games have their 0-0 in the middle of the screen. It therefore
# uses a +/- X and +/- Y co-ordinate system. This makes it harder to work
# out the co-ordinates for placing game items.
#
# --------------------------- HOW TO USE ----------------------------------
# Run this script and hover your mouse over the grid. Look in the console
# of your IDE and it will be printing the game co-ordinates for you.
# In your game, place items you want to have at the given co-ordinates.
# e.g. in the @TokyoEdTech Pong, we had: paddle_b.goto(350, 0)

import turtle

# Set up the window in which everything will be displayed
wn = turtle.Screen()
wn.bgcolor("Black")
wn.title("~ Position Checker ~")
wn.tracer(0)

# Draw a border around the game space
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.pensize(3)
border_pen.penup()
border_pen.setposition(-300, 300)
border_pen.pendown()
for side in range(4):
    border_pen.fd(600)
    border_pen.rt(90)
border_pen.penup()
border_pen.hideturtle()

# Add axis labels to each side for reference
axis_pen = turtle.Turtle()
axis_pen.speed(0)
axis_pen.penup()
axis_pen.hideturtle()
# -x (Left)
axis_pen.color("red")
axis_pen.setposition(-350, -10)
axis_pen.write("-x", align="center", font=("Courier", 24, "normal"))
# +x (Right)
axis_pen.setposition(350, -10)
axis_pen.write("+x", align="center", font=("Courier", 24, "normal"))
# +y (Top)
axis_pen.color("yellow")
axis_pen.setposition(0, 340)
axis_pen.write("+y", align="center", font=("Courier", 24, "normal"))
# -y (Bottom)
axis_pen.setposition(0, -350)
axis_pen.write("-y", align="center", font=("Courier", 24, "normal"))

# Start drawing the grid at 100 pixel divisions
grid_pen = turtle.Turtle()
grid_pen.speed(0)
grid_pen.penup()

def draw_grid():
    count = 0
    horX = -300
    horY = 200
    verX = -200
    verY = 300
    length = 600

    while count != 5:
        grid_pen.color("yellow")
        grid_pen.setposition(horX, horY)
        grid_pen.pendown()
        grid_pen.fd(length)
        grid_pen.penup()
        temphorX = horX - 30
        temphorY = horY - 5
        grid_pen.setposition(temphorX, temphorY)
        grid_pen.write(horY, font=("Courier", 10, "normal"))
        horY += -100
        count += 1

    grid_pen.rt(90)
    count = 0

    while count != 5:
        grid_pen.color("red")
        grid_pen.setposition(verX, verY)
        grid_pen.pendown()
        grid_pen.fd(length)
        grid_pen.penup()
        tempverY = verY + 5
        tempverX = verX - 5
        grid_pen.setposition(tempverX, tempverY)
        grid_pen.write(verX, font=("Courier", 10, "normal"))
        verX += 100
        count += 1

# Print key position labels
    grid_pen.color("white")
    # 0, 0 (middle)
    grid_pen.setposition(2, -8)
    grid_pen.write("0-0", align="center", font=("Courier", 15, "normal"))
    # -300, 300 (top left)
    grid_pen.setposition(-320, 300)
    grid_pen.write("-300, 300", align="center", font=("Courier", 15, "normal"))
    # 300, 300 (top right)
    grid_pen.setposition(300, 300)
    grid_pen.write("300, 300", align="center", font=("Courier", 15, "normal"))
    # -300, -300 (bottom right)
    grid_pen.setposition(-300, -320)
    grid_pen.write("-300, -300", align="center", font=("Courier", 15, "normal"))
    # 300, -300 (bottom right)
    grid_pen.setposition(300, -320)
    grid_pen.write("300, -300", align="center", font=("Courier", 15, "normal"))

    grid_pen.hideturtle()

draw_grid()

# Print the mouse position to the console
# We need to a) get the system X and Y
# Then b) convert to game X and Y
def motion(event):
    x = event.x
    y = event.y
    if x <= 424 and y <= 398:
        x = 424 - x
        y = 398 - y
        print('X -{}, Y {}'.format(x, y))
    elif x > 424 and y < 398:
        x = x - 424
        y = 398 - y
        print('X +{}, Y {}'.format(x, y))
    elif x <= 424 and y >= 398:
        x = 424 - x
        y = y - 398
        print('X -{}, Y -{}'.format(x, y))
    else:
        x = x - 424
        y = y - 398
        print('X +{}, Y -{}'.format(x, y))

canvas = turtle.getcanvas()
canvas.bind('<Motion>', motion)

wn.mainloop()
