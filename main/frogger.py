
import pygame
from pygame.locals import *
import turtle 
import math
import time
import random
import os


wn =turtle.Screen()
wn.title("Jumpy Frog")
wn. setup(600, 800)
wn.cv._rootwindow.resizable(False, False)
os.chdir('main\static\images/frogger')
wn.bgpic('background.gif')

shapes = ["frogger1.gif", "car_left.gif", "car_right.gif", "log_full.gif", "turtle_left.gif", "turtle_right.gif", "turtle_left_half.gif", "turtle_right_half.gif", "turtle_submerged.gif", "home.gif", "frog_home.gif","frogger1small.gif"]
for shape in shapes:
    wn.register_shape(shape)


wn.tracer(0)
pen = turtle.Turtle("frogger1.gif")
pen.speed(0)
pen.hideturtle()
pen.penup()

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
    
    def update(self):
        pass

class Player1(Frog):
    def __init__(self, x, y, width, height, image):
        Frog.__init__(self, x, y, width, height, image)
        self.dx = 0
        self.collision= False
        self.frogs_home = 0
        self.max_time = 60
        self.time_remaining = 60
        self.start_time= time.time()
        self.lives= 4



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
        
        self.time_remaining = self.max_time - round(time.time()- self.start_time)

        if self.time_remaining <=0:
            player.lives -=1
            self.go_back()
    
    def go_back(self):
        self.dx = 0
        self.x= 0
        self.y =-300
        self.max_time = 60
        self.time_remaining = 60
        self.start_time = time.time()
        

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
        self.full_time = random.randint(8,12)
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
class Home(Frog):
    def __init__(self, x, y, width, height, image):
        Frog.__init__(self, x, y, width, height, image)
        self.dx = 0
class Timer():
    def __init__(self, max_time):
        self.x = 200
        self.y = -350
        self.max_time= max_time
        self.width= 200
    
    def render(self,time, pen):
        pen.color("green")
        pen.pensize(5)
        pen.penup()
        pen.goto(self.x, self.y)
        pen.pendown()
        percent = time/self.max_time
        dx = percent * self.width 
        pen.goto(self.x-dx, self.y)
        pen.penup()

#KeyBindings
player= Player1(0, -300, 40, 40, "frogger1.gif")
timer= Timer(60)
level_1= [ 
Car(0,-250, 121, 40, "car_left.gif", -0.6 ),
Car(221,-250, 121, 40, "car_left.gif", -0.6 ),

Car(-221,-200, 121, 40, "car_right.gif", 0.6 ),
Car(0,-200, 121, 40, "car_right.gif", 0.6 ),

Car(0,-150, 121, 40, "car_left.gif", -0.6 ),
Car(221,-150, 121, 40, "car_left.gif", -0.6 ),

Car(221,-50, 121, 40, "car_left.gif", -0.6 ),
Car(221,-150, 121, 40, "car_left.gif", -0.6 ),


Log(0,100, 121, 40, "log_full.gif", -0.2 ),
Log(200,50, 121, 40, "log_full.gif", 0.2 ),

Log(0,100, 121, 40, "log_full.gif", -0.2 ),
Log(200,100, 121, 40, "log_full.gif", -0.2 ),

Turtle(0, 200, 155, 40, "turtle_left.gif", -0.15 ),
Turtle(255, 200, 155, 40, "turtle_left.gif", -0.15 ),


Turtle(0,150, 155, 40, "turtle_right.gif", 0.15 ),
Turtle(255,150, 155, 40, "turtle_right.gif", 0.15 ),

Log(0,250, 121, 40, "log_full.gif", 0.2 ),
Log(200,100, 121, 40, "log_full.gif", -0.2 ),
]

player.render(pen)

homes=[
Home(0,300,50,50,"home.gif"),
Home(-100,300,50,50,"home.gif"),
Home(-200,300,50,50,"home.gif"),
Home(100,300,50,50,"home.gif"),
Home(200,300,50,50,"home.gif"),
]


frogs = level_1 + homes
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

    timer.render(player.time_remaining, pen)
    
    pen.goto(-290, -350)
    pen.shape("frogger1small.gif")
    for life in range(player.lives):
        pen.goto(-280 +(life * 30), -350)
        pen.stamp()
    
    player.dx=0
    player.collision = False
    
    for frog in frogs:
        if player.is_collision(frog):
            if isinstance(frog, Car):
                player.lives -= 1
                player.go_back()
                break
            
            elif isinstance(frog, Log):
                player.dx = frog.dx
                player.collision=True
                break

            elif isinstance(frog, Turtle) and frog.state != "submerged":
                player.dx = frog.dx
                player.collision=True
                break
            
            elif isinstance(frog, Home):
                player.go_back()
                frog.image="frog_home.gif"
                player.frogs_home +=1
                break
    
    if player.y > 0 and player.collision !=True:
        player.lives -= 1
        player.go_back()
    
    if player.frogs_home ==5:
        player.go_back()
        player.frogs_home =0
        for home in homes:
            home.image = "home.gif"
    
    if player.lives==0:
        player.go_back()
        player.frogs_home =0
        for home in homes:
            home.image = "home.gif"
        player.lives= 4
    
    wn.update()
    
    pen.clear()

wn.mainloop()