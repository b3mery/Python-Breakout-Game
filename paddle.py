from turtle import Turtle

class Paddle(Turtle):
    """Class for creating and moving the paddle, Extends Turtle"""

    MOVESIZE = 50
    COLLISION_SIZE = 100

    def __init__(self, screen_width ,screen_height ) -> None:
        super().__init__()
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.shape('square')
        self.color('blue')
        self.shapesize(stretch_len=8,stretch_wid=1)
        self.penup()
        self.goto(0, self.SCREEN_HEIGHT/-2 + 20)
    
    def move_left(self):
        """Move the paddle to the left along the x axis"""
        if self.xcor() > self.SCREEN_WIDTH/-2 + self.COLLISION_SIZE:
            new_x = self.xcor() - self.MOVESIZE
            self.goto(new_x,self.ycor())

    def move_right(self):
        """Move to the right along the x axis """
        if self.xcor() < self.SCREEN_WIDTH/2 - self.COLLISION_SIZE:
            new_x = self.xcor() + self.MOVESIZE
            self.goto(new_x,self.ycor())
    