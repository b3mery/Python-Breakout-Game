from turtle import Turtle
import time

HIGHSCORE_FILE = "high_score.txt"
ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')

class Scoreboard(Turtle):
    """Class for writing, refreshing and tracking game score"""

    high_score:int = 0

    def __init__(self,screen_height:int) -> None:
        super().__init__()
        self.SCREEN_HEIGHT = screen_height
        self.score = 0
        self.lives = 3

        self.penup()
        self.hideturtle()
        self.__read_high_score()
        self.__update_scoreboard()
    
    def __update_scoreboard(self):
        """Update the Scoreboard with current score and highscore"""
        self.color('white')
        self.goto(0,self.SCREEN_HEIGHT/2-35)
        self.clear()
        self.write(f"Lives: {self.lives}\tScore: {self.score}\tHigh Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, points:int):
        """Increase the score by one, then update scoreboard"""
        self.score += points
        self.__update_scoreboard()
    
    def decrease_lives(self):
        """Decrease lives"""
        self.lives-= 1
        self.__update_scoreboard()
    
    def __reset_scoreboard(self):
        """Reset the Scoreboard. 
        If current score greater than highscore, update the highscore"""
        if self.score > self.high_score:
            self.high_score = self.score
            self.__write_high_score()
        self.score = 0
        self.lives = 3
        self.__update_scoreboard()
    
    def __read_high_score(self):
        """Read highscore txt file to self.highscore"""
        try:
            with open(HIGHSCORE_FILE, mode='r', encoding='utf-8') as file:
                try:
                    self.high_score = int(file.read())
                except ValueError:
                    pass         
        except FileNotFoundError:
            pass

    def __write_high_score(self):
        """Write the highscore to txt file, overwriting existing data"""
        with open(HIGHSCORE_FILE, mode='w', encoding='utf-8') as file:
            file.write(f'{self.high_score}')
    
    def game_over_reset(self, game_won:bool =False):
        """Game Over method, reset the game"""
        if game_won:
            text = 'YOU WIN!'
            colour='green' 
        else:
            text = 'GAME OVER'
            colour ='red'

        self.goto(0,0)
        self.color(colour)
        self.write(text, align=ALIGNMENT, font=FONT)
        time.sleep(2)
        self.clear()
        self.__reset_scoreboard()