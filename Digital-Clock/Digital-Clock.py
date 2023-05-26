import turtle
import time
import datetime as dt

# Turtle object to display time
t = turtle.Turtle()

# Turtle object to display the clock frame
t1 = turtle.Turtle()

# Screen for the display
s = turtle.Screen()

# Set the background color of the screen
s.bgcolor("#7cc49a")

# Retrieve the current second, minute and hour from the local system
sec = dt.datetime.now().second
minn = dt.datetime.now().minute
hr = dt.datetime.now().hour

# Setting the properties of the turtle pen that displays the clock frame
t1.pensize(5)
t1.color("#ff1a8c")
t1.penup()

# Setting the starting position of the turtle
t1.goto(-200, -20)
t1.pendown()

# Creating the clock frame
for i in range(2):
    t1.forward(400)
    t1.left(90)
    t1.forward(200)
    t1.left(90)

t1.hideturtle()

while True:
    t.hideturtle()
    t.clear()
    t.penup()
    t.goto(-122, 32)
    t.color("#ff1a8c")
    # display the time
    t.write(str(hr).zfill(2)  # adds '0's for the hour, min, sec values till it becomes 2 digits
            + ":" + str(minn).zfill(2)
            + ":" + str(sec).zfill(2),
            font=("Arial Narrow", 75, "bold")
            )
    time.sleep(1)
    sec += 1

    # Algorithm for the clock work
    if sec == 60:  # The clock has completed a minute
        sec = 0  # Reset the sec value
        minn += 1

    if minn == 60:  # The clock has completed an hour
        minn = 0  # Reset the minute value
        hr += 1

    if hr == 13:  # The clock has completed one half cycle in a day
        hr = 1  # Reset the hour value


