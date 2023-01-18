import turtle
import hideTurtle
import welcomePage

    
#main function starts from here
#define a turtle called screen
screen = turtle.Screen()
#set the delay to False
screen.tracer(False)

#define mole turtle
mole = turtle.Turtle()
#define hammer turtle
hammer = turtle.Turtle()


#define welcome turtle
welcome = turtle.Turtle()
#define success turtle
hit = turtle.Turtle()
#define fail turtle
miss = turtle.Turtle()
#define draw turtle
draw = turtle.Turtle()
#define score turtle
score = turtle.Turtle()

#register image for mole
turtle.register_shape('mole.gif')
#register image for hammer
turtle.register_shape('hammer.gif')

#assign image to mole
mole.shape('mole.gif')
#assign image to hammer
hammer.shape('hammer.gif')

#hide all turtles
hideTurtle.hide_turtle(mole, hammer, turtle, welcome, hit, miss, draw, score)

#set up initial value for start game button to True
#   and restart game button to False
button_list = [True, False]

#score list that stores success and fail scores
score_list = [0, 0]
#set delay to True
screen.tracer(True)


#load welcome page
welcomePage.welcome_page(button_list, score_list,mole, hammer, turtle, welcome, hit, miss, draw, score, screen)

#finish turtle
turtle.done ()
