from turtle import Turtle
import random

COLORS = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
STARTING_SPEED = 5
SPEED_INCREMENT = 5
Y = 250

class CarManager(Turtle):
	
	def __init__(self):
		self.cars = []
		self.car_speed = STARTING_SPEED

	def create_car(self):
		create = random.randint(1, 6)
		if create == 1:
			car = Turtle("square")
			car.shapesize(stretch_wid=1, stretch_len=2)
			car.penup()
			car.color(random.choice(COLORS))
			car.goto((300, random.randint(-250, 250)))
			self.cars += car,

	def move_cars(self):
		for car in self.cars:
			car.backward(self.car_speed)

	def level_up(self):
		self.car_speed += SPEED_INCREMENT