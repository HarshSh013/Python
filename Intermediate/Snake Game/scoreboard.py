from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial", 12, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.highscore =int(data.read())
        # self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
        self.goto(0, 270)

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE : {self.score} High Score : {self.highscore}", False, align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score +=1
        self.update_scoreboard()