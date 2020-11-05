import turtle

left_turtle = turtle.Turtle()
right_turtle = turtle.Turtle()

right_turtle.speed(20)
left_turtle.speed(20)

left_turtle.left(180)
right_turtle.right(0)
left_turtle.left(45)
right_turtle.right(45)

while left_turtle.distance(right_turtle) < 150:
    left_turtle.forward(100)
    # Linke Kugel zeichnen
    left_turtle.left(45)
    left_turtle.forward(10)
    left_turtle.right(90)
    left_turtle.circle(10)
    left_turtle.right(90)
    left_turtle.forward(10)
    # Kugel gezeichnet
    left_turtle.right(90)
    left_turtle.forward(50)
    left_turtle.right(135)
    right_turtle.forward(100)
    # Rechte Kugel zeichnen
    right_turtle.right(45)
    right_turtle.forward(10)
    right_turtle.right(90)
    right_turtle.circle(10)
    right_turtle.right(90)
    right_turtle.forward(10)
    # Kugel gezeichnet
    right_turtle.left(90)
    right_turtle.forward(50)
    right_turtle.left(135)

left_turtle.left(135)
right_turtle.right(135)
left_turtle.forward(60)
right_turtle.forward(60)

left_turtle.right(90)
right_turtle.left(90)
left_turtle.forward(50)
right_turtle.forward(50)

left_turtle.left(90)
right_turtle.right(90)
half_distance = left_turtle.distance(right_turtle) / 2
left_turtle.forward(half_distance)
right_turtle.forward(half_distance)

turtle.Screen().mainloop()