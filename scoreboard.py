from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Aral", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setpos(0, 270)
        self.pencolor("white")
        self.write(f"Score: {self.score}", move=True, align=ALIGNMENT, font=FONT)



    def scoreboard(self):
        self.score += 1
        self.clear()
        self.setpos(0, 270)
        self.write(f"Score: {self.score}", move=True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", move=True, align=ALIGNMENT, font=FONT)
























