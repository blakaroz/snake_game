from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 250)
        self.penup()
        self.score = 0
        self.color("white")
        self.write(f"Score: {self.score}", False, "center", ("Arial", 24,"normal"))
        self.hideturtle()

    def point(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", False, "center", ("Arial", 24, "normal"))