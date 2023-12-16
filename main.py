import turtle as my_turtle
import random

my_turtle.colormode(255)
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.speed("fastest")
my_turtle.goto(-225, -200)

rgb_colors = [(28, 21, 50), (250, 240, 212), (64, 37, 122), (27, 16, 28), (81, 79, 136), (20, 14, 12), (215, 220, 244),
              (146, 155, 185), (135, 65, 124), (118, 88, 201), (127, 86, 62), (177, 147, 174), (193, 156, 122),
              (182, 164, 246), (237, 223, 239), (168, 78, 174), (110, 32, 90), (240, 225, 73), (232, 251, 250),
              (146, 30, 22), (182, 148, 50), (213, 164, 231), (211, 88, 73), (67, 106, 87), (25, 45, 33),
              (135, 166, 158), (240, 216, 5), (64, 156, 174), (83, 69, 34), (119, 220, 232)]

num_dots = 90


def draw_dots():
    my_turtle.setheading(90)
    my_turtle.fd(50)
    my_turtle.setheading(180)
    my_turtle.fd(500)
    my_turtle.setheading(0)


def start_draw():
    for i in range(10):
        my_turtle.dot(20, random.choice(rgb_colors))
        my_turtle.fd(50)


while num_dots > 0:
    num_dots -= 10
    start_draw()
    draw_dots()

my_turtle.exitonclick()
