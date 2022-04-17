import time
from turtle import Turtle

import random
import turtle
from paddle import Paddle

from score_board import Scoreboard


class Ball(Turtle):
    """Class for creating and moving the ball. Extends Turtle"""

    __START_SLEEP_TIME:float = 1/60 # 60 FPS
    X_AXIS_RANGE:int = 12
    COLLISION_SIZE = 15
    INCREASE_SPEED_PERCENT = 0.98

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
        self.turtle_screen_sleep_time = self.__START_SLEEP_TIME 

    def goto_starting_position(self):
        """Set ball in the starting position
        """
        self.x_trajectory = random.randrange(-self.X_AXIS_RANGE,self.X_AXIS_RANGE)
        y = self.SCREEN_HEIGHT / -3
        self.goto(0 , y)

    def __move_ball(self):
        """Move the ball forward by x and y trajectories"""
        new_x = self.xcor() + self.x_trajectory
        new_y = self.ycor() + self.y_trajectory
        self.goto(new_x,new_y)

    def __detect_wall_collision(self):
        """Detect a wall colision, reverse y trajectory to "bounce" the ball"""
        # Top 
        if self.ycor() >= self.SCREEN_HEIGHT/2 - self.COLLISION_SIZE:
            self.y_trajectory *= -1
        # Right
        if self.xcor() >= self.SCREEN_WIDTH/2 - self.COLLISION_SIZE and self.x_trajectory > 0:
            self.x_trajectory *= -1
        # Left
        if self.xcor() <= self.SCREEN_WIDTH/-2 + self.COLLISION_SIZE and self.x_trajectory < 0:
            self.x_trajectory *= -1

    def __detect_ball_out_of_bounds(self):
        """Detect ball out of game window. Reset and decrease lives
        """
        if self.ycor() <= self.SCREEN_HEIGHT/-2 + self.COLLISION_SIZE:
            self.scorebord.decrease_lives()
            time.sleep(1)
            self.goto_starting_position()
            self.turtle_screen_sleep_time = self.__START_SLEEP_TIME
            self.y_trajectory *= -1
    
    def __detect_paddle_collision(self, paddle:Paddle):
        """Detect a collision with the paddles
        If collision, reverse x trajectory"""
        if self.distance(paddle) <= paddle.COLLISION_SIZE and self.ycor() <= self.SCREEN_HEIGHT/-2 + 20: # paddle is + 20 off bottom
            self.reverse_trajectory_and_increase_speed(paddle)


    def reverse_trajectory_and_increase_speed(self, game_object:turtle):
        """Reverse balls y trajectory and increase the speed
        """
        # Set x trajectory
        degree = self.distance(game_object) / game_object.COLLISION_SIZE
        if game_object.xcor() < self.xcor():
            self.x_trajectory = self.X_AXIS_RANGE * degree 
        elif game_object.xcor() > self.xcor():
            self.x_trajectory = -self.X_AXIS_RANGE * degree
        else: 
            self.x_trajectory = 0
        # Reverse y and increase speed
        self.y_trajectory *= -1
        self.turtle_screen_sleep_time *= self.INCREASE_SPEED_PERCENT # lower sleep time to increase speed. 


    def update_and_draw(self, paddle):
        """Public update and draw method

        Args:
            paddle (Paddle): Insanitated Paddle Object
        """
        self.__move_ball()
        self.__detect_wall_collision()
        self.__detect_ball_out_of_bounds()
        self.__detect_paddle_collision(paddle)