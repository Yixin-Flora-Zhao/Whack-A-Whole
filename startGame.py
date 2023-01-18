import hideTurtle
import drawGrid
import writeCoordinate
import moleCoordinate
import moveScore
import hammerMove
import welcomePage


#function that implements main game logic takes
#   x_button, y_button, button_list, and score_list
def start_game(x_button, y_button, button_list, score_list,mole, hammer, turtle, welcome, hit, miss, draw, score, screen):   
    #check start button condition
    if (-142 <= x_button <= 147 and 177 <= y_button <= 209 and button_list[0] == True):
        #clear previous welcome page
        welcome.clear()
        #hide all turtles
        hideTurtle.hide_turtle(mole, hammer, turtle, welcome, hit, miss, draw, score)
        
        #show main game image
        turtle.bgpic('game page.gif')
        #show mole 
        mole.showturtle()

        #this part calls draw_grid() and write_coordinate()
        #   without delay
        screen.tracer(False)
        drawGrid.draw_grid(draw)
        writeCoordinate.write_coordinate(draw)
        screen.tracer(True)
        
        #loop the game 5 times
        for i in range (0, 5):
            #randomly generate x and y coordinates
            x_random, y_random = moleCoordinate.mole_position()
            
            #set screen delay to 0
            screen.tracer(False)
            #lift mole picture
            mole.penup()
            #move mole to the designated random position
            mole.goto(x_random, y_random)
            #set screen delay back to normal
            screen.tracer(True)

            #set the delay to False
            screen.tracer(False)
            #clear previous hit writing
            hit.clear()
            #clear previous miss writing
            miss.clear()
            #move hit writing to (-100, 240)
            moveScore.move_turtle(hit, -100, 240)
            #write success score
            hit.write('SUCCESS: ' + str(score_list[0]), font=("Arial", 22, "bold"))
            #move miss writing to (300, 240)
            moveScore.move_turtle(miss, 300, 240)
            #write fail score
            miss.write('FAIL: ' + str(score_list[1]), font=("Arial", 22, "bold"))
            #set the delay to True
            screen.tracer(True)
            
            while True:
                try:
                    x = int(input ('PLEAES ENTER X COORDINATE (-450 < x < 450): '))
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
            
            while True:
                try:
                    y = int(input ('PLEASE ENTER Y COORDINATE (-250 < y < 50): '))
                    break
                except ValueError:
                    print("Oops!  That was no valid number.  Try again...")
                    
            #check if entered x and y is within a mole's x and y
            if x in range ((x_random - 45), (x_random + 45)) and y in range ((y_random - 35), (y_random + 35)):
                #move hammer to (x, y)
                hammerMove.move_hammer(x, y, hammer)
                #update success score
                score_list[0] += 1
            #case for not hitting a mole
            else:
                #move hammer to (x, y)
                hammerMove.move_hammer(x, y, hammer)
                #update fail score
                score_list[1] += 1

            #set delay to False
            screen.tracer(False)
            #clear previous success score
            hit.clear()
            #clear previous fail score
            miss.clear()
            #move hit writing to (-100, 240)
            moveScore.move_turtle(hit, -100, 240)
            #write success score
            hit.write('SUCCESS: ' + str(score_list[0]), font=("Arial", 22, "bold"))
            #move miss writing to (300, 240)
            moveScore.move_turtle(miss, 300, 240)
            #write fail score
            miss.write('FAIL: ' + str(score_list[1]), font=("Arial", 22, "bold"))
            #set the delay to True
            screen.tracer(True)
##############
#game part ends
            

#end page begins
#############
        
        #set start game button to False
        button_list[0] = False
        #set restart game button to True
        button_list[1] = True
        #clear x and y axis
        draw.clear()
        #hide all turtles
        hideTurtle.hide_turtle(mole, hammer, turtle, welcome, hit, miss, draw, score)
        #clear success score
        hit.clear()
        #clear fail score
        miss.clear()

        #show end-of-game page
        turtle.bgpic('end page.gif')
        #move final score to (-170, 180)
        moveScore.move_turtle(score, -170, 180)
        
        ##################
        #calculate final score in 100
        level = score_list[0] / (score_list[0] + score_list[1]) * 100
        #if level is above or equal to 80, show S as score
        if level >= 80:
            score.write('S', font=("Arial", 31, "bold"))
        #if level is between 60 inclusive and 80, show A as score
        elif 60 <= level < 80:
            score.write('A', font=("Arial", 31, "bold"))
        #if level is between 40 inclusive and 60, show B as score
        elif 40 <= level < 60:
            score.write('B', font=("Arial", 31, "bold"))
        #if level is between 20 inclusive and 40, show A as score
        elif 20 <= level < 40:
            score.write('C', font=("Arial", 31, "bold"))
        #if level is below or equal to 20, show D as score
        else:
            score.write('D', font=("Arial", 31, "bold"))

    #check restart button condition
    elif (-365 <= x_button <= -111 and 107 <= y_button <= 145 and button_list[1] == True):
        #turtle.bye()
        #hide all the turtles
        hideTurtle.hide_turtle(mole, hammer, turtle, welcome, hit, miss, draw, score)
        #clear success score
        hit.clear()
        #clear fail score
        miss.clear()
        
        #reload welcome page
        #welcomePage.welcome_page(score_list, button_list, turtle, score, screen)
        welcomePage.welcome_page(button_list, score_list,mole, hammer, turtle, welcome, hit, miss, draw, score, screen)
##############
#end page ends