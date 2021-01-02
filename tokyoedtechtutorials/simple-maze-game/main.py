# Simple Maze Game tutorial by @TokyoEdTech
# https://www.youtube.com/watch?v=-0q_miviUDs&list=PLlEgNdBJEO-lNDJgg90fmfAq9RzORkQWP
# With tweaks by me
# Ref: https://trinket.io/docs/colors
# Ref: https://www.online-image-editor.com/
# Ref: https://opengameart.org/content/the-treasure-nes-version
# Ref: https://www.twinibird.co.za/resources/
# Ref: https://opengameart.org/content/simple-tiles
# Ref: https://opengameart.org/content/lpc-tile-atlas

import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Simple Maze Game")
wn.setup(700, 700)
# Comment the trace out to get a cool screen-building effect
wn.tracer(0)

# Register Shapes
images = ["img/treasure.gif", "img/wizard-left.gif", "img/wizard-right.gif",
          "img/gray-tile.gif", "img/water-tile.gif", "img/moss-tile.gif",
          "img/lava-tile.gif", "img/mob.gif"]
for eachImage in images:
    turtle.register_shape(eachImage)

# Create pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("dim gray")
        self.penup()
        self.speed(0)

class Water(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("img/water-tile.gif")
        self.penup()
        self.speed(0)

class Moss(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("img/moss-tile.gif")
        self.color("dark green")
        self.penup()
        self.speed(0)

class Lava(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("img/lava-tile.gif")
        self.penup()
        self.speed(0)

# Player class
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("img/wizard-right.gif")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        # Calculate the spot we're going to move TO
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        # Calculate the spot we're going to move TO
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() -24
        move_to_y = player.ycor()

        self.shape("img/wizard-left.gif")

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() +24
        move_to_y = player.ycor()

        self.shape("img/wizard-right.gif")

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("img/treasure.gif")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("img/mob.gif")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        dx = 0
        dy = 0

        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            self.goto(0, 0)

        # Calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.xcor() + dy

        # Check if the space has a wall
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            # Choose a different direction
            self.direction = random.choice(["up", "down", "left", "right"])

        # Set time to move next time
        wn.ontimer(self.move, t=random.randint(100, 300))

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

# Create levels lists
levels = [""]

# Define first level
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X   XXX  XXXXXXXXX  XXXXX",
    "X P MXM XXXX         XXXX",
    "XM   M  XXX   XXXXXXXXXXX",
    "XXM    WWWW    XXX    WXX",
    "XXXX    WW      XXX  XWWX",
    "XXXXX      E   XXXX XXWMX",
    "XXXXX         XXXX   XMMX",
    "XXXXX    XXXXXXXXX   XXTX",
    "XXXXM   XXXXLLXXX    XXXX",
    "XXXM     XXLLLXXM    XXXX",
    "XXXM      XLLXM       XXX",
    "XXXXM     XXXM    X   XXX",
    "XXXLXX    XXX    XXX   XX",
    "XLLLLXX    X    XXXX   XX",
    "XXLXXX     E      XXX XXX",
    "XXX      XX   XX    XXXXX",
    "XX   XXXXXXXXXXX       XX",
    "XX  XX  XX    XXXM    XXX",
    "XX XX          XXXM  XXXX",
    "XX XX  W  XX   XXXM  XXXX",
    "X  X  W   XX   XXM    XXX",
    "X XXX  E   XX   X  X  XXX",
    "X XXXX   TXXX     XXX  XX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

# Add a treasures list
treasures = []

# Track list of enemies
enemies = []

# Add maze to mazes list
levels.append(level_1)

# Create level set-up function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # Get character at each x, y coordinate
            # NOTE the order of y and x in the next line
            character = level[y][x]
            # Calculate the screen x,y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # Check if the character is an X (wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("img/gray-tile.gif")
                pen.stamp()

                # Add coordinates to wall list
                walls.append((screen_x, screen_y))

            # Check if the character is a P (player)
            if character == "P":
                player.goto(screen_x, screen_y)

            # Check if the character is T (Treasure)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

            # Check if the character is E (Enemies)
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))

            # Check if the character is W (Water)
            if character == "W":
                water.goto(screen_x, screen_y)
                water.stamp()

            # Check if the character is M (Moss)
            if character == "M":
                moss.goto(screen_x, screen_y)
                moss.stamp()

            # Check if the character is L (Lava)
            if character == "L":
                lava.goto(screen_x, screen_y)
                lava.stamp()

# Create class instances
pen = Pen()
player = Player()
water = Water()
moss = Moss()
lava = Lava()

# Create walls coordinate list
walls = []

# Set up the level
setup_maze(levels[1])

# Keyboard binding
turtle.listen()
turtle.onkey(player.go_left, "a")
turtle.onkey(player.go_right, "d")
turtle.onkey(player.go_up, "w")
turtle.onkey(player.go_down, "s")

# Turn off screen updates
wn.tracer(0)

# Start moving enemies
for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

# Main game loop
while True:
    # Check for player collision with treasure
    # Iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):
        # Add the Treasure gold to the Player gold
            player.gold += treasure.gold
            print("Player gold: {}".format(player.gold))
        # Destroy the treasure
            treasure.destroy()
        # Remove the treasure from the treasures list
            treasures.remove(treasure)

    for enemy in enemies:
        if player.is_collision(enemy):
            print("Player dies!")

    # Update screen
    wn.update()
