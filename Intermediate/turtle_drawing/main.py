from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()
def move_fwd():
    tim.forward(10)
def move_rt():
    tim.right(10)
def move_lt():
    tim.left(10)
def move_bac():
    tim.back(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_fwd,"w")
screen.onkey(move_lt,"a")
screen.onkey(move_bac,"s")
screen.onkey(move_rt,"d")
screen.onkey(clear,"c")
screen.exitonclick()




