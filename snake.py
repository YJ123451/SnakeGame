from turtle import Turtle
dist = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
    #creates snake
    def create_snake(self):
        for i in range(3):
            tim = Turtle("square")
            tim.penup()
            tim.color("white")
            tim.goto((-20*i),0)
            self.turtles.append(tim)
    def grow(self):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(self.turtles[-1].xcor(),self.turtles[-1].ycor())
        self.turtles.append(new_snake)
    #move snake
    def move(self):
        for turtle in range(len(self.turtles) - 1, 0, -1):
            x = (self.turtles[turtle - 1]).xcor()
            y = (self.turtles[turtle - 1]).ycor()
            self.turtles[turtle].setpos(x, y)
        self.turtles[0].forward(dist)
    #change directions of snake
    def up(self):
        if self.head.heading() != DOWN:
            self.turtles[0].setheading(UP)
        #by changing the direction of the head, the other "parts" of the snake will take the position of the part after it due to line 22
    def right(self):
        if self.head.heading != LEFT:
            self.turtles[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.turtles[0].setheading(LEFT)
    def down(self):
        if self.head.heading() != UP:
            self.turtles[0].setheading(DOWN)





