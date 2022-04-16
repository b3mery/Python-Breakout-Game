import random
from ball import Ball
from block import Block
from score_board import Scoreboard

class BlockManager:
    """Managers the break out block objects
    """
    rows = 4
    
    def __init__(self,screen_width ,screen_height, ball:Ball, scoreboard:Scoreboard) -> None:
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.ball:Ball = ball
        self.scoreboard:Scoreboard = scoreboard
        self.LEFT_SIDE = self.SCREEN_WIDTH /- 2 + 40
        self.RIGHT_SIDE = self.SCREEN_WIDTH /2 - 40
        self.TOP_SIDE = self.SCREEN_HEIGHT / 2 - 20
        self.active_blocks:list[Block] = []
        self.inactive_blocks:list[Block] = []
        self.__draw_all_blocks()

    def __draw_row_of_blocks(self, y, value):
        """Draw a row of blocks on the screen

        Args:
            y (int): Y Axis Position
        """
        x = self.LEFT_SIDE
        while x <= self.RIGHT_SIDE:
            self.active_blocks.append(Block((x, y), value))
            x += 80

    def __draw_all_blocks(self):
        """Draw all blocks to screen
        """
        y = self.TOP_SIDE
        for i in range(0,self.rows):
            self.__draw_row_of_blocks(y, 4-i)
            y -= 40
    
    def __detect_ball_collisions(self):
        """Detect ball collisions.
        if collision:
            * Inactive the block
            * Remove block for active list.
        """
        for block in self.active_blocks[:]:
            if block.distance(self.ball) <= 60:
                # hide turtle and remove 
                block.hideturtle()
                self.active_blocks.remove(block)
                self.inactive_blocks.append(block)

                # Update scoreboard
                self.scoreboard.increase_score(block.value)
                
                # Reverse Trajectory
                self.ball.reverse_trajectory_and_increase_speed(block)
    
    @property                
    def has_game_been_won(self):
        """Check is the game has been won

        Returns:
            bool: True if game has been won. Else False
        """
        if len(self.active_blocks) == 0:
            return True
        return False

    def game_over_reset(self):
        """Reset all the blocks to active and displayed
        """
        for block in self.inactive_blocks[:]:
            block.showturtle()
            self.inactive_blocks.remove(block)
            self.active_blocks.append(block)

    def update_and_draw(self):
        """Update public method
        """
        self.__detect_ball_collisions()