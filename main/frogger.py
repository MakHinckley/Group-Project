import pygame
import turtle 
import os

wn=turtle.Screen()
wn.title("Jumpy Frog")
wn. setup(900, 900)
wn. bgcolor("black")
os.chdir('main\static\images/frogger')
wn.register_shape("frogger1.gif")
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

class Player1(Frog):
    def __init__(self, x, y, width, height, image):
        Frog.__init__(self, x, y, width, height, image)
    
    def up(self):
        self.y += 45 
    def down(self):
        self.y -= 45 
    def right(self):
        self.x += 45 
    def left(self):
        self.x -= 45 
class Car(Frog):
    def __init__(self, x, y, width, height, image):
        Frog.__init__(self, x, y, width, height, image)



#KeyBindings
player= Player1(0, -300, 40, 40, "frogger1.gif")
player.render(pen)


wn.listen()
wn.onkeypress(player.up, "w")
wn.onkeypress(player.down, "s")
wn.onkeypress(player.right, "d")
wn.onkeypress(player.left, "a")

while True:
    player.render(pen)
    wn.update()
    pen.clear()

wn.mainloop()