# Simple die roller

import turtle
import random
import time

turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
turtle.tracer(0)

class Dice(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.fd(0)
        self.speed(0)
        self.penup()
        self.numberRolled = 0
        self.dicePen = turtle.Turtle()
        self.hideturtle()

    def dodiceroll(self, faces):
        previousNumber = self.numberRolled
        print("Previous number = " + str(previousNumber))
        print("Faces:  %s" % faces)
        self.numberRolled = random.randint(1, faces)
        print("Number Rolled = " + str(self.numberRolled))
        if self.numberRolled == previousNumber:
            self.numberRolled = random.randint(1, faces)

    def drawDiceRoll(self):
        self.dicePen.clear()
        self.dicePen.color("white")
        self.dicePen.penup()
        self.dicePen.hideturtle()
        self.dicePen.goto(-0, 20)
        self.dicePen.write(self.numberRolled, align="center", font=("Courier", 150, "normal"))

class Game:
    def __init__(self):
        self.pen = turtle.Turtle()

    def draw_border(self):
        # Draw a border on the screen
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(-100, 200)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(200)
            self.pen.rt(90)
        self.pen.penup()
        # Write Helper Text to the screen
        self.pen.goto(0, -50)
        self.pen.write("Press [r] to roll again", align="center", font=("Courier", 15, "normal"))

def runTheGame():
    numberOfDieFaces = 6

# We could ask the player how many die faces they want to have, instead of the normal 6 as above
# It would be something like:
    # getNumberOfDiceSides = 0
    # while getNumberOfDiceSides == 0:
    #     getNumberOfDiceSides = int(turtle.textinput("Dice Sides", "How many sides?"))
    #     print(getNumberOfDiceSides)
    #
    # numberOfDieFaces = getNumberOfDieSides

    a = 0
    while a < 10:
        dice.dodiceroll(numberOfDieFaces)
        dice.drawDiceRoll()
        time.sleep(0.1)
        a += 1

# Create a new Game object and draw the game border
game = Game()
game.draw_border()

# Create a new Dice object and draw the
dice = Dice()

runTheGame()

# Keyboard Bindings
turtle.onkeypress(runTheGame, "r")
turtle.listen()

print("------------------------------------")

while True:
    turtle.update()
