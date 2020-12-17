from turtle import Turtle
import random


class Food(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("circle") #TODO: Change to pick a set of images/emoticons in shape of fruits
		self.penup()
		self.shapesize(stretch_len=0.5, stretch_wid=0.5)
		self.color("red")
		self.speed("fastest")
		random_x = random.randint(-280, 280)
		random_y = random.randint(-280, 280)
		self.place_food()

	def place_food(self):
		random_x = random.randint(-280, 280)
		random_y = random.randint(-280, 280)
		self.goto(random_x, random_y)