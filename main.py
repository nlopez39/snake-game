from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0) #allows us to uodate a drawing by setting a delay between the drawings
screen.title("My Snake Game")

# #draw 3 squares
# position = [(0,0), (-20, 0), (-40, 0)]

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)
# #make the snake move
near_wall = True
while near_wall:
    screen.update()#updates drawing when tracer is turned off
    time.sleep(0.1)  # after all three segments have moved there is a delay before all move again
    #this code will link all three squares and help turn the snake
    #we will start from the end of the snake so at (-40,0)/otherwise moving from right to left
    snake.move()
#detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        #increase size of snake
        snake.increase_size()
#detect collison with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        near_wall = False
        scoreboard.game_over()
#detect tail
    for segment in snake.segments:
        if snake.segments[0] == segment:
            pass
        elif snake.segments[0].distance(segment) < 10:
            near_wall = False ##or in this case the game ends becuse we touched our own tail
            scoreboard.game_over()








screen.exitonclick()