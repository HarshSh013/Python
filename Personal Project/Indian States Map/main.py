
import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "India.gif"
screen.addshape(image)
turtle.shape(image)




# Set the screen size to match the image dimensions
image_width = 700  # Update this with the actual width of your image
image_height = 828  # Update this with the actual height of your image
screen.setup(width=image_width, height=image_height)


data = pandas.read_csv("states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 36:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/36 States Correct",
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
