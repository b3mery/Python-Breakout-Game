import time

from turtle import Screen

from ball import Ball
from paddle import Paddle
from block_manager import BlockManager
from score_board import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
GAME_HEIGHT = 600

# Screen:
screen = Screen()
screen.colormode(255)
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

# Game objects
scoreboard = Scoreboard(SCREEN_HEIGHT)
ball = Ball(SCREEN_WIDTH, GAME_HEIGHT, scoreboard)
paddle = Paddle(SCREEN_WIDTH, GAME_HEIGHT)
block_manager = BlockManager(SCREEN_WIDTH, GAME_HEIGHT, ball, scoreboard)

# Screen listener functions
screen.listen()
screen.onkeypress(paddle.move_left, 'Left')
screen.onkeypress(paddle.move_right, 'Right')

# Basic game loop
while True:
    screen.update()
    if scoreboard.lives == 0 or block_manager.has_game_been_won:
        scoreboard.game_over_reset(block_manager.has_game_been_won)
        block_manager.game_over_reset()
        ball.goto_starting_position()

    time.sleep(ball.turtle_screen_sleep_time)
    ball.update_and_draw(paddle)
    block_manager.update_and_draw()
    
