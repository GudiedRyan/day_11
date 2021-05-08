import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

tracker = turtle.Turtle()
tracker.ht()
tracker.penup()

map_data = pandas.read_csv("50_states.csv")
state_list = map_data["state"].to_list()

guessed_states =[]


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct", prompt="Name a state.").title()
    if answer_state == "Exit":
        break
    if answer_state in state_list and answer_state not in guessed_states:
        correct_state = map_data[map_data.state == answer_state]
        tracker.goto((correct_state.x.item(), correct_state.y.item()))
        tracker.write(f"{correct_state.state.item()}", align="center", font=("Arial", 10, "normal"))
        guessed_states.append(correct_state.state.item())

states_to_learn = []
for state in state_list:
    if state not in guessed_states:
        states_to_learn.append(state)

data_dict = {
    "states to learn": states_to_learn
}

data = pandas.DataFrame(data_dict)
data.to_csv("states_to_learn.csv")