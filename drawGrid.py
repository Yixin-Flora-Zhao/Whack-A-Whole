#function that draw the x axis and y axis
def draw_grid(draw):
    #set the pen width to 4
    draw.pensize(4)
    #set the axises color to white
    draw.color('white')
    #set up starting grid drawing point for x
    x = -500
    #set up starting grid drawing point for y
    y = 0
    
    #lift up draw turtle
    draw.penup()
    #move draw to (-500, 0)
    draw.goto(x, y)
    #put down draw turtle
    draw.pendown()
    #draw x axis
    draw.goto(500, y)
    
    #lift up draw turtle
    draw.penup()
    #move draw to (0, -300)
    draw.goto(0, -300)
    #put down draw
    draw.pendown()
    #draw y axis
    draw.goto(0, 200)