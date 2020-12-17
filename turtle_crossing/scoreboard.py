from turtle import Turtle


ALIGNMENT = "left"
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
	
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.penup()
		self.goto(-280, 250)
		self.level = 1
		self.update_scoreboard()

	def increase_level(self):
		self.level += 1
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()
		self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

	def game_over(self):
		self.goto(0, 0)
		self.write(f"Game Over", align="center", font=FONT)