from turtle import Turtle


UP = 20
DOWN = 20

class Paddle(Turtle):

	def __init__(self, position):
		super().__init__()
		self.shape("square")
		self.penup()
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.color("white")
		self.speed("fastest")
		self.goto(position)		

	def up(self):
		move_y = self.ycor() + 20
		self.goto(self.xcor(), move_y)

	def down(self):
		move_y = self.ycor() - 20
		self.goto(self.xcor(), move_y)
