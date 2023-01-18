#function that moves success, fail and score positions
#   this function takes 3 parameters, name of the turtle
#   x coordinate and y coordinate of this turtle
def move_turtle(name, x, y):
    #sets spped for name
    name.speed(0)
    #lift pen for name
    name.penup()
    #let name go to (x, y) coordinate
    name.goto(x, y)
    #put down name
    name.pendown()