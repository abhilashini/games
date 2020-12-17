from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

import time


s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

s.listen()
s.onkey(key="Up", fun=snake.up)
s.onkey(key="Right", fun=snake.right)
s.onkey(key="Down", fun=snake.down)
s.onkey(key="Left", fun=snake.left)

game_on = True
while game_on:
	s.update()
	time.sleep(0.1)	
	snake.move()

	#Detect snake in vicinity of food
	if snake.head.distance(food) < 15:
		food.place_food()
		snake.extend()
		scoreboard.update_score()

	#Detect collision with walls
	if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
		game_on = False
		scoreboard.game_over()

	#Detect collision with tail
	for segment in snake.segments[1:]:
		if snake.head.distance(segment) < 10:
			game_on = False
			scoreboard.game_over()

s.exitonclick()