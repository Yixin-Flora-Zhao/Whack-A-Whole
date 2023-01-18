#function that moves the hammer to (x, y)
#   this function takes 2 parameters x
#   coordinate and y coordinate
def move_hammer(x, y, hammer):
    #show hammer picture
    hammer.showturtle()
    #lift up hammer
    hammer.penup()
    #set hammer speed as slow
    hammer.speed('slow')
    #move hammer to the designated (x, y)
    hammer.goto(x, y)
    #move hammer back to the origin
    hammer.goto(0, 0)
    #hide the hammer
    hammer.hideturtle()