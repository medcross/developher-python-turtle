import turtle
import maze as mz, blueprints


def setup_maze(block_size, selected_maze):
    maze_array = blueprints.maze_arrays[selected_maze]
    screen = Canvas(maze_array.__len__(), maze_array[0].__len__(), block_size)
    screen.set_tracer(0)
    maze = mz.Maze(maze_array, block_size)
    player = Player(maze, block_size)
    screen.set_tracer(1)
    return player, screen


class Player:
    NORTH = 270
    EAST = 0
    SOUTH = 90
    WEST = 180

    def __init__(self, maze, block_size):
        self.start_coordinates = (maze.start[0] * block_size + block_size / 2,
                                  -(maze.array.__len__() - maze.start[1]) * block_size + block_size / 2)
        self.array_position = maze.start
        self.maze_array = maze.array
        self.is_finished = False
        self.step = block_size
        self.turtle = turtle.Turtle()
        self.init_turtle()

    def init_turtle(self):
        self.turtle.shape("turtle")
        self.turtle.color("green")
        self.turtle.width(2)
        self.turtle.speed(1)
        self.turtle.penup()
        self.turtle.goto(self.start_coordinates)
        self.turtle.setheading(Player.NORTH)
        self.turtle.pendown()

    def move_forward(self, steps=1):
        if self.is_wall_ahead():
            return False
        elif self.is_finish_ahead():
            if not self.is_finished:
                self.turtle.forward(self.step)
                self.turtle.hideturtle()
                self.turtle.penup()
                self.turtle.forward(self.step / 2)
                self.turtle.write("Ziel erreicht!", move=False, align="center", font=("Arial", 24, "normal"))
                self.is_finished = True
            return False
        s = 0
        while s < steps:
            self.turtle.forward(self.step)
            s += 1
        add_x, add_y = self.get_xy_addition_based_on_heading()
        self.array_position = self.array_position[0] + add_x, self.array_position[1] + add_y

    def turn_right(self):
        self.turtle.left(90)

    def turn_left(self):
        self.turtle.right(90)

    def is_wall_ahead(self):
        return self.get_position_ahead() == 0

    def is_finish_ahead(self):
        return self.get_position_ahead() == 3

    def get_position_ahead(self):
        add_x, add_y = self.get_xy_addition_based_on_heading()
        return self.maze_array[self.array_position[1] + add_y][self.array_position[0] + add_x]

    def get_xy_addition_based_on_heading(self):
        heading = self.turtle.heading()
        if heading == Player.NORTH:
            return 0, -1
        elif heading == Player.EAST:
            return 1, 0
        elif heading == Player.SOUTH:
            return 0, 1
        elif heading == Player.WEST:
            return -1, 0
        return 0, 0


class Canvas:
    def __init__(self, x, y, block_size):
        self.screen = turtle.Screen()
        long_side = x if x >= y else y
        screen_length = (long_side + 2) * block_size
        self.screen.setup(screen_length, screen_length)
        self.screen.bgcolor("white")
        margin = 35
        self.screen.setworldcoordinates(-margin, margin, long_side * block_size + margin,
                                        -long_side * block_size - margin)

    def set_tracer(self, t):
        if t == 0:
            self.screen.tracer(0)
        else:
            self.screen.tracer(1)

    def main_loop(self):
        self.screen.mainloop()

    def onkey(self, fun, key):
        self.screen.onkey(fun, key)

    def listen(self):
        self.screen.listen()
