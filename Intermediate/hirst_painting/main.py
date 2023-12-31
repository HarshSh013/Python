# import colorgram as col
# rgb_colors=[]
# colors = col.extract('image.jpg', 30)
# for i in colors:
#     r=i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     rgb=(r,g,b)
#     rgb_colors.append(rgb)
# print(rgb_colors)
from turtle import Screen
import random
import turtle as tur
tur.colormode(255)
color_list=[(200, 166, 110), (238, 241, 246), (143, 75, 52), (168, 153, 45), (58, 92, 120), (224, 203, 130), (136, 161, 179), (132, 34, 25), (50, 115, 88), (199, 95, 73), (144, 25, 31), (18, 96, 74), (70, 47, 39), (173, 145, 153), (130, 69, 74), (150, 177, 152), (56, 42, 46), (186, 86, 92), (236, 175, 164), (40, 58, 70), (88, 144, 125), (180, 204, 180), (26, 83, 90), (240, 159, 165), (20, 68, 59), (39, 65, 93), (113, 126, 148)]
tim=tur.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen= Screen()
screen.exitonclick()