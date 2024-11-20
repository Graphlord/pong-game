from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=6)
        self.penup()
        self.goto(position)
        self.color("white")

    def move_up(self):
        new_y = self.ycor() + 50
        self.goto(self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 50
        self.goto(self.xcor(), y=new_y)
