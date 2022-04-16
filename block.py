from turtle import Turtle
import random

class Block(Turtle):
    """Class for creating blocks, Extends Turtle"""

    def __init__(self, pos:tuple, value:int) -> None:
        super().__init__()
        self.value = value
        self.pencolor('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=4,stretch_wid=2)
        self.__random_colour()
        self.goto(pos)
    
    def __random_colour(self):
        """Generate a random RGB colour"""
        r = random.randint(0,255)
        g =  random.randint(0,255)
        b =  random.randint(0,255)
        self.fillcolor((r, g, b))
    
