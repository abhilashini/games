from turtle import Turtle


START_COORDS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_UNITS = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:

	def __init__(self):
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]

	def create_snake(self):
		for coords in START_COORDS:
			self.add_segment(coords)

	def add_segment(self, position):
		seg = Turtle("square")
		seg.color("green")
		seg.penup()
		seg.goto(position)
		self.segments += seg,

	def extend(self):
		self.add_segment(self.segments[-1].position())

	def move(self):
		for idx in range(len(self.segments)-1, 0, -1):
			x = self.segments[idx-1].xcor()
			y = self.segments[idx-1].ycor()
			self.segments[idx].goto(x, y)
		self.head.forward(MOVE_UNITS)

	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)