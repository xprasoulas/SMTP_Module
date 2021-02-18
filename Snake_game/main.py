import time
from turtle import Screen
from snake import Snake

# Set the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Disable animation of screen - not seeing the gup of movement must be combined with screen.update()
# and time.sleep(0.1)
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
# Movement of square
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # # Segment Movement has a bug while the snake moves- squares don't follow its other
    # for segment in segments:
    #     segment.forward(10)
    #     screen.update()

    # Each segment takes the position of the before segment
    snake.move()


screen.exitonclick()
