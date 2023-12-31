# import turtle
# import pandas
# screen=turtle.Screen()
# screen.title("U.S.State Game")
# image="blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
#
# import turtle
# def draw_text(x, y, text):
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#     turtle.write(text, align="center", font=("Arial", 12, "normal"))
# # def get_coor(x, y):
# #     print(x, y)
# #
# # screen = turtle.Screen()
# #
# # turtle.onscreenclick(get_coor)
# # screen.mainloop()
#
# guessed_states = []
# while len(guessed_states) < 50:
#     answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
#                                     prompt="What's another state's name?").title()
#     # print(answer_state)
#     df=pandas.read_csv("50_states.csv")
#     # print(df.state)
#     all_states=df.state.to_list()
#     if answer_state in all_states:
#         guessed_states.append(answer_state)
#         t=turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data=df[df.state== answer_state]
#         t.goto(int(state_data.x),int(state_data.y))
#         t.write(state_data.state.item())
#
#
#
# screen.exitonclick()

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        #missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
