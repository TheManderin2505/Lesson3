import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500
TITLE = "Shoot The Alien"

alien=Actor('alien_2')
alien.pos = 50,50

message = "Game starts..."

score = 0 

def move_Alien():
    alien.x=randint(50,450)
    alien.y=randint(50,450)

def on_mouse_down(pos):
    global message
    global score
    if alien.collidepoint(pos):
        move_Alien()
        message = "good shot"
        score = score + 1
    else:
        message = "you missed"
        score = score - 1
        



def draw():
    screen.clear()
    screen.fill("light blue")
    alien.draw()
    screen.draw.text(message,center=(200,20),fontsize=30,color="black")
    screen.draw.text("Score : "+str(score),topleft=(20,20),fontsize=30,color="black")


                     

move_Alien()

pgzrun.go()