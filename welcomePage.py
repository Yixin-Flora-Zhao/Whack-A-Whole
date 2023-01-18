import startGame


#function that starts welcome page
#   takes 2 parameters a score list (scccess and fail)
#   and a button list
def welcome_page(button_list, score_list,mole, hammer, turtle, welcome, hit, miss, draw, score, screen):
    
    #initialize score list and player score
    for i in range (0, 2):
        if i == 0 or i == 1:
            #set success and fail to 0
            score_list[i] = 0
        #set start game button to True
        if i == 0:
            button_list[i] = True
        #set restart game button to False
        else:
            button_list[i] = False

    #import starting game image
    turtle.bgpic('start page.gif')
    #clear previous score if any
    score.clear()

    #function that takes to start_game(x_button, y_button, button_list, score_list) function
    screen.onclick(lambda x_button, y_button:startGame.start_game(x_button, y_button, button_list, score_list, mole, hammer, turtle, welcome, hit, miss, draw, score, screen))