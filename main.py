"""
Imports:
Snake.py which contains the Snake class
Food.py which contains the Food class
Turtle module to implement game graphics
"""

import Snake
import Food
import turtle
import time

""""
The main file for the program that implements the Python game using 
the turtle module. 

Global variables:

DELAY: The value after which the main game loop reruns. This sets how 
fast the snake moves. This value is to be slowly decremented as the 
game progresses.

COUNTER: Variable to keep count of the number of elapsed frames since
the last decrement of the DELAY variable.
"""
DELAY = 100
COUNTER = 0


def game_loop() -> None:

    """
    Function that implements the main game loop. All updations are to be
    done in this function. Function should also implement GAME OVER logic
    and do the decrement in DELAY appropriately.
    :return: None
    """

    ############ DO NOT CHANGE ###########
    global DELAY
    global COUNTER
    ######################################
    ########## WRITE BELOW ###############


    snake_turtle.goto(0,0) #Send turtle to (0,0)
    snake_turtle.direction = "left" #set shead direction as left
    food_turtle.goto(food_obj.position) #send food to the object position
    snake_obj.update_snake() #update snakes position after each frame
    snake_obj.keep_snake_onscreen() #check if the snake is out of screen and do stuffs!!!

    # Test Game over condition
    if snake_obj.GAME_OVER == True:
        print("\n\n\n\nGAMEOVER\n\n\n")
        turtle.write('GAME OVER!', font=("Verdana",15, "normal"))
        return

    # Update snakes position
    for index in range(len(snake_obj.shape)):
        x = snake_obj.shape[index][0]
        y = snake_obj.shape[index][1]
        if index == 0 :
            snake_turtle.goto(x,y)
        else:
            #print(index, len(snake_obj.new_segments))
            snake_obj.new_segments[index-1].goto(x,y)

    # Test for food collision
    food_collision = snake_obj.check_food_collision(current_food_position = food_obj.position)
    if food_collision == True:

        # Create new food position
        food_obj.update_random_food_position()
        food_turtle.goto(food_obj.position)

        # Add new segment to snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        snake_obj.new_segments.append(new_segment)

        # Where to add the new segment to snake?
        if  snake_obj.direction == "left" or snake_obj.direction == "right":
            snake_obj.shape.append([snake_obj.shape[-1][0] - 20, snake_obj.shape[-1][1]])
        else:
            snake_obj.shape.append([snake_obj.shape[-1][0], snake_obj.shape[-1][1] - 20])

        # Send the new segment to its position
        new_segment.goto([snake_turtle.xcor(), snake_turtle.ycor()])

    ######################################
    ########### DO NOT CHANGE ############
    screen.update()

    if DELAY > 10 and COUNTER == 15:
        DELAY -= 1
        COUNTER = 0

    COUNTER += 1

    turtle.ontimer(game_loop, DELAY)
    #######################################



if __name__ == "__main__":
    """
    The main for the program.
    DO NOT CHANGE    
    """

    ############ DO NOT CHANGE ############
    screen_height = 500
    screen_width = 500
    start_time = time.time()

    screen = turtle.Screen()
    screen.setup(screen_width, screen_height)
    screen.title("Python in Python")
    screen.bgcolor("blue")
    screen.tracer(0)

    snake_obj = Snake.Snake(window_size=(screen_width, screen_height))
    food_obj = Food.Food(window_size=(screen_width, screen_height))
    food_obj.update_random_food_position()

    snake_turtle = turtle.Turtle("square") #head = snake_tuetle
    snake_turtle.color(snake_obj.color)
    snake_turtle.penup()

    food_turtle = turtle.Turtle()
    food_turtle.shape(food_obj.shape)
    food_turtle.color(food_obj.color)
    food_turtle.pensize(food_obj.size)
    food_turtle.penup()

    screen.listen()
    screen.onkey(snake_obj.go_up, "Up")
    screen.onkey(snake_obj.go_down, "Down")
    screen.onkey(snake_obj.go_right, "Right")
    screen.onkey(snake_obj.go_left, "Left")

    game_loop()
    turtle.done()
    #########################################