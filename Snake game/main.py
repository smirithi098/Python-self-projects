from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreBoard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 270 \
            or snake.head.ycor() < -290:
        scoreBoard.write_high_score()
        snake.reset_snake()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreBoard.write_high_score()
            snake.reset_snake()


screen.exitonclick()
