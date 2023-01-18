#function that writes out coordinate numbers
def write_coordinate(draw):
    #set up initial x value for writing x coordinates
    x = -500
    #set up initial y value for writing x coordinates 
    y = 0
    #loop that writes out x coordinates 
    for i in range(0, 21):
        draw.penup()
        draw.goto(x + 2, y)
        draw.pendown()
        if x != 0:
            draw.write(str(x), font=("Arial", 12, "bold"))
        x = x + 50
    
    #set up initial x value for writing y coordinates
    x = 5
    #set up initial y value for writing y coordinates 
    y = -300
    #loop that writes out x coordinates 
    for i in range (0, 11):
        draw.penup()
        draw.goto(x, y)
        draw.pendown()
        draw.write(str(y), font=("Arial", 12, "bold"))
        y = y + 50