import turtle
import pandas as pd


s = turtle.Screen()
s.title("U.S. States Game")

img_us_map = "US_Map.gif"
states_and_coords = pd.read_csv('US_States.csv')
states = states_and_coords.state.to_list()
s.addshape(img_us_map) #Make image available in screen for turtle to use

turtle.shape(img_us_map)

"""
Function to get (x, y) coordinates of clicked position

1. onscreenclick() is a listener
2. mainloop() works like exitonclick() -> keeps screen open till all coords are collected

def get_mouse_click_coor(x, y):
	print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
"""
correct = 0
answered_states = []

while correct != 50:
	enter_state = s.textinput(title=f"{correct}/50 States Correct", prompt="Enter a state name").title()
	state_coord_data = states_and_coords[states_and_coords.state == enter_state]

	if enter_state in states:
		x = int(state_coord_data.x)
		y = int(state_coord_data.y)
		t = turtle.Turtle()
		t.hideturtle()
		# print(f"State is {enter_state}\n\t(x, y) = ({x}, {y})")
		t.penup()
		t.goto(x, y)
		t.write(enter_state)

		answered_states += enter_state,
		correct += 1	

s.exitonclick()