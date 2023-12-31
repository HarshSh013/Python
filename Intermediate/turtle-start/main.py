from turtle import Turtle,Screen
import turtle as t
import random
tim = t.Turtle()
screen = t.Screen()
screen.bgcolor("black")
# tim.color("red")
# for i in range(4):
#     tim.forward(100)
#     tim.left(90)
# for i in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# tim.forward(100)
# tim.right(120)
#
# tim.forward(100)
# tim.right(120)
#
# tim.forward(100)
# i=3
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# while i<11:
#     angle=360/i
#     tim.color(random.choice(colours))
#     for j in range(i):
#         tim.forward(100)
#         tim.right(angle)
#     i+=1
tim.width(0.5)
t.colormode(255)

tim.shape("circle")
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color
tim.speed("fastest")
current_heading=tim.heading()
tim.circle(100)
for i in range(144):
    current_heading = tim.heading()
    tim.color(random_color())
    tim.setheading(current_heading+2.5)
    tim.circle(100)

tim.color("white")








# direction=["right","left","forward","backward"]
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# for i in range(100):
#     random_direction=random.choice(direction)
#     tim.color(random_color())
#     if random_direction=="right":
#         tim.right(90)
#         tim.forward(30)
#     if random_direction=="left":
#         tim.left(90)
#         tim.forward(30)
#     if random_direction=="forward":
#         tim.forward(30)
#     else:
#         tim.backward(30)








screen= Screen()
screen.exitonclick()