# http://www.codeskulptor.org/#user47_brch87tYsQbUnXa.py

# implementation of card game - Memory

import simplegui
import random

#Constants
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 100
CARD_WIDTH = 50
CARD_HEIGHT = 100
TEXT_SIZE = 20

#globals
game_list = [1, 2, 3, 4, 5, 6, 7, 8,
             1, 2, 3, 4, 5, 6, 7, 8]
exposed = []
game_state = 0
move1 = -1
move2 = -2
turn_count = 0

# helper function to initialize globals
def new_game():
    global game_list, exposed
    random.shuffle(game_list)
    exposed = [False] * len(game_list)

    # define event handlers
def mouseclick(pos):
    global game_state, move1, move2, turn_count, exposed, game_list
    
    clicked = pos[0] // CARD_WIDTH
    if exposed[clicked]:
        return #do nothing if we have already clicked here!

    # state logic
    if game_state == 0:
        game_state = 1
        move1 = clicked
    elif game_state == 1:
        game_state = 2
        move2 = clicked
    elif game_state == 2:
        game_state = 1
        turn_count += 1
        label.set_text("Turns = " + str(turn_count)) 
        if not game_list[move1] == game_list[move2]:
            exposed[move1] = False
            exposed[move2] = False
        move1 = clicked
        move2 = -2
    
    exposed[clicked] = True
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global game_list
    x = 0
    width = 0
    height = (CARD_HEIGHT // 2) + TEXT_SIZE / 2
    
    for i in game_list:
        width += CARD_WIDTH / 2
        canvas.draw_text(str(i), (width - 6, height), TEXT_SIZE, 'White')
        width += CARD_WIDTH / 2

    for i in range(len(game_list)):
        width += CARD_WIDTH / 2
        
        if exposed[i]:
            canvas.draw_text(str(game_list[i]), (width - 6, height), TEXT_SIZE, 'White')
        else:
            canvas.draw_polygon([(x, 0),
                                 (x, CARD_HEIGHT), 
                                 (x + CARD_WIDTH, CARD_HEIGHT),
                                 (x + CARD_WIDTH, 0)], 
                                1, 
                                "Grey", 
                                "Green")  
        width += CARD_WIDTH / 2
        x += CARD_WIDTH


   
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric