import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


s = Screen()
s.setup(height=600, width=600)
s.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

s.listen()
s.onkey(key="Up", fun=player.up)

game_on = True
while game_on:
	time.sleep(0.1)
	s.update()
	cars.create_car()
	cars.move_cars()

	#Player collides with car
	for car in cars.cars:
		if car.distance(player) < 20:
			game_on = False
			scoreboard.game_over()

	#Player crossed succesfully
	if player.is_at_finish_line():
		player.go_to_start()
		cars.level_up()
		scoreboard.increase_level()

s.exitonclick()