import pygame
import turtle 
import math
import time
import random
import os

wn=turtle.Screen()
wn.title("Jumpy Frog")
wn. setup(600, 800)
wn.cv._rootwindow.resizable(False, False)
wn. bgcolor("black")
os.chdir('main\static\images/frogger')

shapes = ["frogger1.gif", "car_left.gif", "car_right.gif", "log_full.gif", "turtle_left.gif", "turtle_right.gif", "turtle_left_half.gif", "turtle_right_half.gif", "turtle_submerged.gif"]
for shape in shapes:
    wn.register_shape(shape)


wn.tracer(0)
pen = turtle.Turtle("frogger1.gif")
pen.speed(0)
pen.hideturtle()

class Frog():
    def __init__(self, x, y, width, height, image):
        self.x =x
        self.y= y
        self.width= width
        self.height= height
        self.image= image

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()

    def is_collision(self, other):
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)

class Player1(Frog):
    def __init__(self, x, y, width, height, image):
        Frog.__init__(self, x, y, width, height, image)
        self.dx = 0
    def up(self):
        self.y += 50 
    def down(self):
        self.y -= 50 
    def right(self):
        self.x += 50 
    def left(self):
        self.x -= 50 
    def update(self):
        self.x += self.dx
        
    #Border Checking(Player Death)
        if self.x < -300 or self.x > 300:
            self.x = 0
            self.y= -300

class Car(Frog):
    def __init__(self, x, y, width, height, image,dx):
        Frog.__init__(self, x, y, width, height, image,)
        self.dx= dx
    
    def update(self):
        self.x += self.dx

        # Border checking
        if self.x < -400:
            self.x = 400
        
        if self.x > 400:
            self.x = -400

class Log(Frog):
    def __init__(self, x, y, width, height, image,dx):
        Frog.__init__(self, x, y, width, height, image,)
        self.dx= dx
    def update(self):
        self.x += self.dx

        if self.x < -400:
            self.x = 400
        
        if self.x > 400:
            self.x = -400

class Turtle(Frog):
    def __init__(self, x, y, width, height, image,dx):
        Frog.__init__(self, x, y, width, height, image,)
        self.dx= dx
        self.state = "full"
        self.full_time = random.randit(8,12)
        self.half_time = random.randint(4,6)
        self.submerged_time = random.randint(4,6)
        self.start_time= time.time()

    def update(self):
        self.x += self.dx

        if self.x < -400:
            self.x = 400
        
        if self.x > 400:
            self.x = -400
        
        #Image State 
        if self.state == "full":
            if self.dx > 0:
                self.image = "turtle_right.gif"
            else:
                self.image = "turtle_left.gif"
        elif self.state =="half_up" or self.state == "half_down":
            if self.dx > 0:
                self.image = "turtle_right_half.gif"
            else:
                self.image = "turtle_left_half.gif"
        elif self.state =="submerged":
            self.image = "turtle_submerged.gif"
            

        if self.state =="full" and time.time() - self.start_time > self.full_time:
            self.state ="half_down"
            self.start_time = time.time()
        elif self.state =="half_down" and time.time() - self.start_time > self.half_time:
            self.state ="submerged"
            self.start_time = time.time()
        elif self.state =="submerged" and time.time() - self.start_time > self.submerged_time:
            self.state ="half_up"
            self.start_time = time.time()
        elif self.state =="half_up" and time.time() - self.start_time > self.half_time:
            self.state ="full"
            self.start_time = time.time()


#KeyBindings
player= Player1(0, -300, 40, 40, "frogger1.gif")
player.render(pen)

car_left = Car(0,-250, 121, 40, "car_left.gif", -0.1 )
car_right = Car(0,-200, 121, 40, "car_right.gif", 0.1 )

log_left = Log(0,-100, 121, 40, "log_full.gif", -0.2 )
log_right = Log(0,-150, 121, 40, "log_full.gif", 0.2 )

turtle_left = Turtle(0, 0, 155, 40, "turtle_left.gif", -0.15 )
turtle_right = Turtle(0,-50, 155, 40, "turtle_right.gif", 0.15 )

frogs = [car_left, car_right, log_left, log_right, turtle_left, turtle_right]
frogs.append(player)

wn.listen()
wn.onkeypress(player.up, "w")
wn.onkeypress(player.down, "s")
wn.onkeypress(player.right, "d")
wn.onkeypress(player.left, "a")

while True:
    for frog in frogs:
        frog.render(pen)
        frog.update()

    player.dx=0
    for frog in frogs:
        if player.is_collision(frog):
            if isinstance(frog, Car):
                player.x = 0
                player.y = -300
                break
            elif isinstance(frog, Log):
                player.dx = frog.dx
                break
            elif isinstance(frog, Turtle) and frog.state != "submerged":
                player.dx = frog.dx
                break
    
    wn.update()
    
    pen.clear()

wn.mainloop()