class Snake:
    """
    Class Snake that holds all the attributes of the snake that the player controls
    while playing the game.
    """

    def __init__(self, window_size: tuple):
        """
        Constructor for the Snake class. Has to initialize the
        following variables.

        __offsets__: dictionary
                    A dictonary that maps 'up', 'down', 'right'
                    and 'left' to the appropriate actions for the
                    snake segment positions.
        shape:      List of lists
                    A list of the segments of the snake.

        new_segments:   List of tutrle object segments

        direction:  str
                    A string holding the current direction in which the
                    snake is moving.

        color:      str
                    A string holding the color of the snake

        window_size: tuple
                    A tuple of integers holding the game window size

        GAME_OVER:  bool
                    A flag to tell if the Game Over condition has been triggered

        :param window_size: The size of the game window given as
                            a tuple containing (window_width, window_height)
        """
        ############## WRITE BELOW ################

        Snake.__offset__ =  {"up":(0,20), "down":(0,-20), "left": (-20,0), "right" : (20,0)}
        Snake.shape = [[0,0]] #Initial Poaition
        Snake.new_segments = []
        Snake.direction = 'left' #Initial Direction
        Snake.color = 'green' #Head Color
        Snake.window_size = window_size
        Snake.GAME_OVER = False


    def go_up(self) -> None:
        """
        Function that implements what happens when
        the up arrow is pressed on the keyboard
        :return: None
        """
        ############## WRITE BELOW ###############

        # Logic is that if snake is moving is down you cant go up.
        if Snake.direction != "down":
            Snake.direction = "up"


        ##########################################
    def go_down(self) -> None:
        """
                Function that implements what happens when
                the down arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############

        # Logic is that if snake is moving is up you cant go down.

        if Snake.direction != "up":
            Snake.direction = "down"

        ##########################################
    def go_left(self) -> None:
        """
                Function that implements what happens when
                the left arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############

        # Logic is that if snake is moving is right you cant go left.

        if Snake.direction != "right":
            Snake.direction = "left"

        ##########################################
    def go_right(self) -> None:
        """
                Function that implements what happens when
                the right arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############

        # Logic is that if snake is moving is left you cant go right.

        if Snake.direction != "left":
            Snake.direction = "right"

        ##########################################

    def check_food_collision(self, current_food_position: tuple) -> bool:
        """
        Function that checks if the snake has collided with the food.
        :param current_food_position: A tuple of integers representing the
                                      current position of the food.
        :return: bool
                 Returns True if the snake has collided with the food, False
                 otherwise
        """

        ############## WRITE BELOW ###############

        # Checks the distance between snake's head (i.e position at snake.shape[0] to food_position at eacb coordinate.

        segment = Snake.shape[0] #Position of head

        if abs((segment[0] - current_food_position[0])) < 25 and abs((segment[1] - current_food_position[1])) < 25: #TODO: SET PROPER NUMBER
            return True

        else:
            return False
        ##########################################

    def keep_snake_onscreen(self) -> None:
        """
        Function that implements the logic that prevents
        the snake from going off the side of the game window.
        The snake is to reappear from the other side of the
        window.

        :return: None
        """

        ############## WRITE BELOW ###############

        # Logic: If snake's head is reaching screen's end, change the coordinates to the other end of the whole snake
        # This can be done by subtracting window_size's appropripate coordinate

        mover = (0,0) # Decides if snake is out of screen
        for cor in Snake.shape:

            if cor[0] > Snake.window_size[0] / 2:
                mover = (-1,0)
            elif cor[0] < 0 - Snake.window_size[0] / 2:
                mover = (1,0)
            elif cor[1] > Snake.window_size[1] / 2:
                mover = (0,-1)
            elif cor[1] < 0 - Snake.window_size[1] / 2:
                mover = (0,1)

            # Now add window_size to required cooredinate
            for index in range(len(Snake.shape)):
                Snake.shape[index] = (Snake.shape[index][0], Snake.shape[index][1])
                moveby = (mover[0]*Snake.window_size[0], mover[1]*Snake.window_size[1])
                Snake.shape[index] = tuple([sum(x) for x in zip(Snake.shape[index], moveby)])
            break



        ##########################################

    def update_snake(self) -> None:
        """
        Function that updates the positions of the
        snake per game loop. Function also checks
        if game over condition has been reached.
        :return: None
        """

        ############## WRITE BELOW ###############

        #Logic: Move the head as per direction. Copy the rest to add to the head
        #Last position is of no use after the move so pop it out

        Snake_shape_copy = Snake.shape.copy()
        Snake_shape_copy = Snake_shape_copy[:-1]
        Snake.shape[0] = tuple([sum(x) for x in zip(Snake.shape[0] ,  Snake.__offset__[Snake.direction])])

        Snake.shape = [Snake.shape[0]] + Snake_shape_copy

        count = 0
        for segment in Snake.shape:
            if len(Snake.shape) >= 3:
                #print(segment[0] - Snake.shape[-1][0], segment[1] - Snake.shape[-1][1], count)
                if abs((segment[0] - Snake.shape[-1][0])) < 10 and abs(
                        (segment[1] - Snake.shape[-1][1])) < 10:  # TODO: SET PROPER NUMBER
                    count += 1
                    if count >= 2:
                        Snake.GAME_OVER = True





        ##########################################









