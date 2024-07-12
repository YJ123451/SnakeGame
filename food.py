#Food the snake will "eat\
from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        # Random cord values, screen is 600 x 600, so we do -280 to 280 to make sure "food" doesn't appear at the very edge of each 300 x 300 axis
        random_x = random.randint(-270,270)
        random_y = random.randint(-270,270)
        self.goto(random_x,random_y)







