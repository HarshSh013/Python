from turtle import Turtle,Screen
import random
# tim=Turtle()
is_race_on = False
screen=Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# print(usr_bet)
colors=["violet","blue","green","yellow","orange","red"]
all_turtles = []
y_cor=[-150,-90,-30,30,90,150]
for q in range(0,6):
    # player=Turtle(shape="turtle")
    # player.color(colors[players.index(player)])
    # player.penup()
    # player.goto(x=230,y=y_cor[players.index(player)])
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[q])
    new_turtle.goto(x=-220, y=y_cor[q])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()




