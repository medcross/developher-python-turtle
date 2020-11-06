import turtle


class Maze:
    def __init__(self, maze_array, block_size):
        self.array = maze_array
        self.start, self.end = self.get_start_and_end()
        self.block_size = block_size
        self.pen = turtle.Turtle()
        self.init_pen()
        self.draw_maze()

    def get_start_and_end(self):
        start, end = 0, 0
        y = 0
        for row in self.array:
            x = 0
            for state in row:
                if state == 2:
                    start = (x, y)
                if state == 3:
                    end = (x, y)
                x += 1
            y += 1
        return start, end

    def init_pen(self):
        self.pen.speed(0)
        self.pen.color("red")
        self.pen.fillcolor("tomato")
        self.pen.shape("square")
        self.pen.width(3)
        self.pen.hideturtle()
        self.pen.setheading(270)

    def draw_maze(self):
        y = self.array.__len__() - 1
        for row in self.array:
            x = 0
            for state in row:
                if state == 0:
                    self.draw_block((x, -y))
                x += 1
            y -= 1

    def draw_block(self, start):
        self.pen.penup()
        self.pen.goto((start[0] * self.block_size, start[1] * self.block_size))
        self.pen.pendown()
        self.pen.begin_fill()
        for i in range(4):
            self.pen.forward(self.block_size)
            self.pen.left(90)
        self.pen.end_fill()
