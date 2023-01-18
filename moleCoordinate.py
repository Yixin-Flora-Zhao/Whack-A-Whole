import random


#function that generates a mole x coordinate
#   and y coordinate randomly
def mole_position():
    #randomly generates a x coordinate from -450 to 450
    x_random = random.randint(-450, 450)
    #randomly generates a y coordinate from -250 to 50
    y_random = random.randint(-250, 50)
    
    #return randomly generated x and y coordinate
    return x_random, y_random 