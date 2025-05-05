import turtle


# Function to draw an equilateral triangle
def draw_triangle(turtle, side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

# Function to draw the Star of David
def draw_star_of_david(turtle, side_length):
    # Draw the first triangle
    draw_triangle(turtle, side_length)

    # Position for the second triangle
    turtle.penup()
    turtle.forward(side_length)
    turtle.left(180)
    turtle.pendown()

    # Draw the second triangle
    draw_triangle(turtle, side_length)

    turtle.hideturtle()

# Set up the turtle and screen
screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)  # Set drawing speed to fastest

# Draw the Star of David
draw_star_of_david(pen, 100)

# Keep the window open until it is closed manually
turtle.done()