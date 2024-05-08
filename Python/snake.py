import turtle

gn = turtle.Screen()
gn.title("Pong")
gn.bgcolor("black")
gn.setup(width=800, height=600)
gn.tracer(0)


#Snake
Snake = turtle.Turtle()
Snake.speed(0)
Snake.shape("square")
Snake.color("white")
Snake.shapesize(stretch_wid=2, stretch_len=10)
Snake.penup()
Snake.goto(0, -100)

#Function
def snake_forward():
    Snake.forward(90)

def snake_left():
    Snake.left(90)

def snake_right():
    Snake.right(90)

def snake_back():
    Snake.back(90)
    
#Movement
gn.listen()
gn.onkeypress(snake_forward,"w")
gn.onkeypress(snake_back,"s")
gn.onkeypress(snake_right,"d")
gn.onkeypress(snake_left,"a")

while True:
    gn.update()
    
    





