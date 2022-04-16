from turtle import Turtle

import random
import turtle
from paddle import Paddle

from score_board import Scoreboard


class Ball(Turtle):
    """Class for creating and moving the ball. Extends Turtle"""

    __start_sleep_time:float = 1/60
    rand_x_range:int = 10

    def __init__(self, screen_width, screen_height, scoreboard:Scoreboard) -> None:
        super().__init__()
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.scorebord:Scoreboard = scoreboard
        self.y_trajectory = 10
        self.x_trajectory = 0
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color('white')
        self.goto_starting_position()
        self.turtle_screen_sleep_time = self.__start_sleep_time # 60 FPS

    def goto_starting_position(self):
        """Set ball in the starting position
        """
        self.x_trajectory = random.randrange(-self.rand_x_range,self.rand_x_range)
        y = self.SCREEN_HEIGHT / -3
        self.goto(0 , y)

    def __move_ball(self):
        """Move the ball forward by x and y trajectories"""
        new_x = self.xcor() + self.x_trajectory
        new_y = self.ycor() + self.y_trajectory
        self.goto(new_x,new_y)

    def __detect_wall_collision(self):
        """Detect a wall colision, reverse y trajectory to "bounce" the ball"""
        # Top and Bottom
        if self.ycor() >= self.SCREEN_HEIGHT/2 - 15:
            self.y_trajectory *= -1
        # Left and Right
        if self.xcor() >= self.SCREEN_WIDTH/2 - 15 or self.xcor() <= self.SCREEN_WIDTH/-2 + 15:
            self.x_trajectory *= -1

    def __detect_ball_out_of_bounds(self):
        """Detect ball out of game window. Reset and decrease lives
        """
        if self.ycor() <= self.SCREEN_HEIGHT/-2 + 15:
            self.scorebord.decrease_lives()
            self.goto_starting_position()
            self.turtle_screen_sleep_time = self.__start_sleep_time
            self.y_trajectory *= -1
    
    def __detect_paddle_collision(self, paddle:Paddle):
        """Detect a collision with the paddles
        If collision, reverse x trajectory"""
        if self.distance(paddle) <= 80 and self.ycor() <= self.SCREEN_HEIGHT/-2 + 20:
            self.reverse_trajectory_and_increase_speed(paddle)


    def reverse_trajectory_and_increase_speed(self, game_object:turtle):
        """Reverse balls y trajectory and increase the speed
        """
        # Set x trajectory
        if game_object.xcor() < self.xcor():
                self.x_trajectory = 5
        else:
            self.x_trajectory = -5
        # Reverse y and increase speed
        self.y_trajectory *= -1
        self.turtle_screen_sleep_time *= 0.95 # lower sleep time to increase speed. 



    def update_and_draw(self, paddle):
        """Public update and draw method

        Args:
            paddle (Paddle): Insanitated Paddle Object
        """
        self.__move_ball()
        self.__detect_wall_collision()
        self.__detect_ball_out_of_bounds()
        self.__detect_paddle_collision(paddle)