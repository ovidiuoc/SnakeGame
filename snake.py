from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 0
DOWN = 1
LEFT = 2
RIGHT= 3

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.orientation = RIGHT

    def create_snake(self):
        for position in STARTING_POSITIONS:
           self.add_segment(position)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            self.segments[seg].goto(self.segments[seg - 1].xcor(), self.segments[seg - 1].ycor())
        self.segments[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.orientation == RIGHT:
            self.segments[0].left(90)
            self.orientation = UP
        elif self.orientation == LEFT:
            self.segments[0].right(90)
            self.orientation = UP

    def move_down(self):
        if self.orientation == RIGHT:
            self.segments[0].right(90)
            self.orientation = DOWN
        elif self.orientation == LEFT:
            self.segments[0].left(90)
            self.orientation = DOWN

    def move_left(self):
        if self.orientation == UP:
            self.segments[0].left(90)
            self.orientation = LEFT
        elif self.orientation == DOWN:
            self.segments[0].right(90)
            self.orientation = LEFT


    def move_right(self):
        if self.orientation == UP:
            self.segments[0].right(90)
            self.orientation = RIGHT
        elif self.orientation == DOWN:
            self.segments[0].left(90)
            self.orientation = RIGHT

    def add_segment(self,position):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)
    def extend(self):
        self.add_segment(self.segments[-1].position())