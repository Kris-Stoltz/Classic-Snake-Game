from turtle import Turtle

FONT = ("Press Start 2p", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score:{self.score}', False, 'center', FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, 'center', FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


