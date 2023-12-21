from turtle import Screen, Turtle
import time

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("white")

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment_1 = Turtle("square")
        segment_1.color("white")
        segment_1.penup()
        segment_1.goto(position)
        segment_1.color("orange")
        self.segments.append(segment_1)


    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # segments = []

        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
