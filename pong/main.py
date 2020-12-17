from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard


s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Pong")
s.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

s.listen()
s.onkey(key="Up", fun=r_paddle.up)
s.onkey(key="Down", fun=r_paddle.down)
s.onkey(key="w", fun=l_paddle.up)
s.onkey(key="s", fun=l_paddle.down)

game_on = True
while game_on:
	time.sleep(ball.move_speed)
	s.update()
	ball.move()

	#Collision with wall
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()

	#Ball hits paddles
	if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320) :
		ball.bounce_x()

	#Ball misses right paddle
	if ball.xcor() > 380:
		ball.reset_position()
		scoreboard.l_point()

	#Ball misses left paddle
	if ball.xcor() < -380:
		ball.reset_position()
		scoreboard.r_point()

s.exitonclick()