from turtle import Turtle

TOP_CENTER_COORDS = (0, 250)
CENTER = (0, 0)
ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")

class ScoreBoard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = -1
		self.hideturtle()
		self.goto(TOP_CENTER_COORDS)
		self.color("white")
		self.update_score()

	def update_score(self):
		self.score += 1
		self.clear()
		self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

	def game_over(self):
		self.goto(CENTER)
		self.write("GAME OVER", align=ALIGNMENT, font=FONT)