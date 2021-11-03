from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        random_x = random.randint(-240, 240)
        random_y = random.randint(-240, 240)
        self.goto(random_x,random_y)
