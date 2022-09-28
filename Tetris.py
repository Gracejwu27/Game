# Tetris game!
import turtle
import time
import random

delay = 0.05
scr = turtle.Screen()
scr.title("Tetris by Grace Wu")
scr.bgcolor("black")
scr.setup(width=500, height=800)
scr.tracer(0)


class Shape:
    def __init__(self):
        self.x = 4
        self.y = 0
        self.color = random.randint(1, 7)
        # All the shapes
        o = [[1, 1],
             [1, 1]]

        i1 = [[1, 1, 1, 1]]

        i2 =[[1],
             [1],
             [1],
             [1]]

        j = [[1, 0, 0, ],
             [1, 1, 1]]

        l = [[0, 0, 1],
             [1, 1, 1]]

        s = [[1, 1, 0],
             [0, 1, 1]]

        z = [[0, 1, 1],
             [1, 1, 0]]

        t = [[0, 1, 0],
             [1, 1, 1]]

        shapes = [o, i1, i2, l, s, z, j, t]

        #choose a random shape
        self.shape = random.choice(shapes)

        self.height = len(self.shape)
        self.width = len(self.shape[0])

    def move_left(self, grid):
        if self.x > 0:
            if grid[self.y][self.x-1] == 0:
                self.erase_shape(grid)
                self.x -= 1

    def move_right(self, grid):
        if self.x < 11-self.width:
            if grid[self.y][self.x + self.width] == 0:
                self.erase_shape(grid)
                self.x += 1

    def draw_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if(self.shape[y][x]) == 1:
                    grid[self.y + y][self.x + x] = self.color

    def erase_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if (self.shape[y][x]) == 1:
                    grid[self.y + y][self.x + x] = 0

    def can_move(self,grid):
        result = True
        for x in range(self.width):
            if self.shape[self.height-1][x] == 1:
                if grid[self.y + self.height][self.x + x] != 0:
                    result = False
        return result



grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 4, 5, 3, 2, 0, 1, 2, 0, 0],
]

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(1)


def draw_grid(pen, grid):
    pen.clear()
    top = 230
    left = -110
    colors = ["black", "red", "orange", "light blue", "yellow", "purple", "blue", "green"]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x = left + (x * 20)
            screen_y = top - (y * 20)
            color_number = grid[y][x]
            color = colors[color_number]
            pen.color(color)
            pen.goto(screen_x, screen_y)
            pen.stamp()


def check_grid(grid):
    # Check if each row is full
    y = 19
    while y > 0:
        is_full = True
        for x in range(0, 10):
            if grid[y][x] == 0:
                is_full = False
                y -= 1
                break
        if is_full:
            global score
            score += 10
            for copy_y in range(y, 0, -1):
                for copy_x in range(0, 10):
                    grid[copy_y][copy_x] = grid[copy_y - 1][copy_x]


def draw_score(pen, score):
    pen.hideturtle()
    pen.goto(100, 250)
    pen.write('Score: {}'.format(score), move=False, align="left", font=("Arial", 30, "normal"))
    pen.showturtle()


# create the basic shape
shape = Shape()

# Put the shape in the grid
grid[shape.y][shape.x] = shape.color

# Draw the initial grid
scr.listen()
scr.onkeypress(lambda: shape.move_left(grid), "Left")
scr.onkeypress(lambda: shape.move_right(grid), "Right")

# score
score = 0
draw_score(pen, score)
# Main game loop
while True:
    scr.update()
    # Move the Shape
    # Open Row
    # Check for bottom
    if shape.y == 19 - shape.height + 1:
        shape = Shape()
        check_grid(grid)
    # Check for collision
    elif shape.can_move(grid):
        # Erase the current shape
        shape.erase_shape(grid)
        # Move the Shape by 1
        shape.y += 1
        # Draw the shape again
        shape.draw_shape(grid)

    else:
        shape = Shape()
        check_grid(grid)

    # Draw the game
    draw_grid(pen, grid)
    draw_score(pen, score)

    time.sleep(delay)

# scr.mainloop()
