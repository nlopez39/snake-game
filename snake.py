from turtle import Turtle
class Snake:
    START_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
    def __init__(self):
        self.segments = []
        self.create_snake()
    def create_snake(self):
        for i in self.START_POSITIONS:
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(i)  # move tp the positions given
            self.segments.append(tim)
    def move_up(self):
        self.segments[0].setheading(90)

    def move_down(self):
        # self.segments[0].forward(20)
        self.segments[0].setheading(270)
    def move_left(self):
        # self.segments[0].forward(20)
        self.segments[0].setheading(180)
    def move_right(self):
        # self.segments[0].forward(20)
        self.segments[0].setheading(0)
    #move function
    def move(self):
        #start at the end of the snake, make the 3rd snake  = 2nd snake and 2nd snake  =1st snake
        #right to left
        for i in range(len(self.segments)-1,0, -1):
            #start by looking at x and y coordinates at the second snake
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            #now the new position of the 3rd snake is the 2nd snakes position
            #for the first iteration this is saying snake[2].goto(-20,0)
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(20)
    def increase_size(self):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        self.segments.append(new_square)
