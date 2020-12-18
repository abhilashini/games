import turtle
import pandas as pd
import re


s = turtle.Screen()
s.title("India States Game")
s.setup(width=800, height=943)
img_india_map = "India_Map.gif"
s.addshape(img_india_map)

turtle.shape(img_india_map)
correct = 0
answered_states = []

states_and_coords = pd.read_csv('India_States.csv')
states = states_and_coords.state.to_list()

while correct != 36:
	enter_state = s.textinput(title=f"{correct}/36 Correct", prompt="Enter a State or UT name").title()
	if "And" in enter_state:
		state = re.sub(r"\bAnd\b", "and", enter_state)
	else:
		state = enter_state
	state_coord_data = states_and_coords[states_and_coords.state == state]

	if state in states:
		x = int(state_coord_data.x)
		y = int(state_coord_data.y)
		t = turtle.Turtle()
		t.hideturtle()
		# print(f"State is {state}\n\t(x, y) = ({x}, {y})")
		t.penup()
		t.goto(x, y)
		t.write(state)

		answered_states += state,
		correct += 1	

s.exitonclick()