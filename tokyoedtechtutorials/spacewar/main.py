# Space war tutorial by @TokyoEdTech
# https://www.youtube.com/watch?v=Ak1IDnP5IrI&list=PLlEgNdBJEO-muprNCDYiKLZ-Kc3-p8thS
# With tweaks by me
# Convert images to .gif files here: https://www.online-image-editor.com/
# Ref: https://trinket.io/docs/colors
# Ref: https://opengameart.org/content/laser-fire
# Ref: https://opengameart.org/content/big-low-frequency-explosion-boom
# Ref: https://opengameart.org/content/muffled-distant-explosion
# Ref: https://opengameart.org/content/space-backgrounds-9

import os
import random
import turtle
import time

# fd (forward) appears to be needed for MacOS to show the window
turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
# hide the default turtle
turtle.bgpic("stars2.gif")
turtle.hideturtle()
# reduce memory usage
turtle.setundobuffer(1)
turtle.tracer(0)
turtle.title("~ Space War! ~")

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        self.fd(self.speed)

        # Boundary detection
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)

    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
        (self.xcor() <= (other.xcor() + 20)) and \
        (self.ycor() >= (other.ycor() - 20)) and \
        (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False

class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 4
        self.lives = 3
        self.shapesize(1, 2, 1)
        self.color("light gray", "light blue")

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1


class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 4
        self.setheading(random.randint(0, 360))

class PlayAudio():
    def __init__(self):
        self.gamestate = 1
        # start the game music
        os.system("afplay scifi-close.mp3&")

    def togglemusic(self):
        if self.gamestate == 0:
            os.system("killall afplay")
            self.gamestate = 1
        else:
            os.system("afplay scifi-close.mp3&")
            self.gamestate = 0

class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 6
        self.setheading(random.randint(0, 360))

    def move(self):
        self.fd(self.speed)

        # Boundary detection
        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)

class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.3, stretch_len=0.4, outline=0)
        self.speed = 20
        self.status = "ready"
        self.goto(-1000, 1000)

    def fire(self):
        if self.status == "ready":
            # Play missile sound
            os.system("afplay laser4.wav&")
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    def move(self):
        if self.status == "ready":
            self.goto(-1000, 1000)

        if self.status == "firing":
            self.fd(self.speed)

        # Border check
        if self.xcor() < -290 or self.xcor() > 290 or self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000, 1000)
            self.status = "ready"

class Particle(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.goto(-1000, -1000)
        self.frame = 0

    def explode(self, startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0, 360))
        self.frame = 1

    def move(self):
        if self.frame > 0:
            self.fd(10)
            self.frame += 1

        if self.frame > 20:
            self.frame = 0
            self.goto(-1000, 10)

class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.highScore = 0
        self.enemyKilled = 0
        self.alliesKilled = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.scorewriter = turtle.Turtle()
        self.highScoreWriter = turtle.Turtle()
        self.statsWriter = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        # Draw a border on the screen
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.ht()
        self.pen.penup()
        self.pen.goto(-350, 360)
        self.pen.color("yellow")
        self.pen.write("Press [h] for help", align="center", font=("Arial", 14, "normal"))

    def show_score(self):
        self.scorewriter.clear()
        self.scorewriter.speed(0)
        self.scorewriter.color("white")
        self.scorewriter.penup()
        self.scorewriter.goto(0, 330)
        msg1 = "Score: %s" % self.score
        self.scorewriter.write(msg1, align="center", font=("Arial", 24, "normal"))
        self.scorewriter.ht()
        self.scorewriter.penup()

    def show_high_score(self):
        self.highScoreWriter.clear()
        self.highScoreWriter.speed(0)
        self.highScoreWriter.color("white")
        self.highScoreWriter.penup()
        self.highScoreWriter.goto(0, -350)
        msg2 = "High Score: %s" % self.highScore
        self.highScoreWriter.write(msg2, align="center", font=("Arial", 24, "normal"))
        self.highScoreWriter.ht()
        self.highScoreWriter.penup()

    def show_stats(self):
        self.statsWriter.clear()
        self.statsWriter.speed(0)
        self.statsWriter.color("white")
        self.statsWriter.penup()
        self.statsWriter.goto(-200, -370)
        stats1 = "Enemy Killed: %s" % self.enemyKilled
        self.statsWriter.write(stats1, align="center", font=("Arial", 16, "normal"))
        self.statsWriter.goto(200, -370)
        stats2 = "Allies Killed: %s" % self.alliesKilled
        self.statsWriter.write(stats2, align="center", font=("Arial", 16, "normal"))
        self.statsWriter.ht()
        self.statsWriter.penup()

    def help_screen(self):
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
        hlp.write("Help", align="center", font=("Courier", 24, "normal"))

        hlp.goto(-180, 20)
        hlp.write("Blue = Allies | Red = Enemy \nDo NOT shoot allies!\nShoot or crash into enemies", align="left", font=("Courier", 15, "normal"))

        hlp.goto(-180, -10)
        hlp.write("[w] accelerate   | [s] decelerate", align="left", font=("Courier", 15, "normal"))

        hlp.goto(-180, -30)
        hlp.write("[a] turn left    | [d] turn right", align="left", font=("Courier", 15, "normal"))

        hlp.goto(-180, -50)
        hlp.write("[space bar] fire | [m] music", align="left", font=("Courier", 15, "normal"))

        hlp.hideturtle()

        timer = turtle.Turtle()
        timer.hideturtle()
        timer.penup()
        timer.goto(0, -90)
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

# Create game object
game = Game()

# Draw the game border
game.draw_border()

# Show the game status
game.show_score()
game.show_high_score()
game.show_stats()

# Create the sprites
player = Player("triangle", "white", 0, 0)
missile = Missile("triangle", "yellow", 0, 0)

music = PlayAudio()

enemies = []
for i in range(6):
    enemies.append(Enemy("circle", "red", -100, 0))

allies = []
for i in range(6):
    allies.append(Ally("square", "blue", 100, 0))

# Create particles for explosions
# TODO: Assign these different colours to Player, Enemy and Ally and remove the random choice
particles = []
particlecolour = ["red", "orange", "yellow"]
particlechoice = random.randint(0, 2)
for i in range(20):
    particles.append(Particle("circle", str(particlecolour[particlechoice]), 0, 0))

# Keyboard bindings
turtle.onkey(player.turn_left, "a")
turtle.onkey(player.turn_right, "d")
turtle.onkey(player.accelerate, "w")
turtle.onkey(player.decelerate, "s")
turtle.onkey(missile.fire, "space")
turtle.onkeypress(game.help_screen, "h")
turtle.onkeypress(music.togglemusic, "m")
turtle.listen()

# main game loop
while True:
    turtle.update()
    time.sleep(0.02)

    player.move()
    missile.move()

    for enemy in enemies:
        enemy.move()

        # Collision detection between the Player and the Enemy
        if player.is_collision(enemy):
            os.system("afplay big-explosion.wav&")
            # Added particle effects here
            for particle in particles:
                particle.explode(enemy.xcor(), enemy.ycor())
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            game.score += 25
            game.enemyKilled += 1
            if game.score > game.highScore:
                game.highScore = game.score
                game.show_high_score()
            game.show_score()
            game.show_stats()

        # Collision detection between the Missile and the Enemy
        if missile.is_collision(enemy):
            os.system("afplay muffled-explosion.wav&")
            # Do the explosion
            for particle in particles:
                particle.explode(missile.xcor(), missile.ycor())
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            missile.status = "ready"
            # Increase the score
            game.score += 100
            game.enemyKilled += 1
            if game.score > game.highScore:
                game.highScore = game.score
            game.show_high_score()
            game.show_score()
            game.show_stats()

    for ally in allies:
        ally.move()

        # Collision detection between the Missile and Ally
        if missile.is_collision(ally):
            os.system("afplay big-explosion.wav&")
            for particle in particles:
                particle.explode(missile.xcor(), missile.ycor())
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            ally.goto(x, y)
            missile.status = "ready"
            # Decrease the score
            game.score -= 50
            game.alliesKilled += 1
            game.show_score()
            game.show_stats()

    for particle in particles:
        particle.move()

# delay = input("Press enter to finish. >")