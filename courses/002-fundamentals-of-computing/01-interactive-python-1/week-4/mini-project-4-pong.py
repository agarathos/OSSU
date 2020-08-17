# http://www.codeskulptor.org/#user47_OVERpmRQILM232Z.py

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
PAD_VEL = 5
hit_paddle = False

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists

    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    x_vel = random.randrange(120, 240) / 60
    y_vel = random.randrange(60, 180) / 60

    if direction == LEFT:
        x_vel = -x_vel
        y_vel = -y_vel
        
    ball_vel = [x_vel, y_vel]
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    spawn_ball(LEFT)
    
    paddle1_pos = HEIGHT / 2 - (PAD_HEIGHT / 2)
    paddle2_pos = HEIGHT / 2 - (PAD_HEIGHT / 2)
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, hit_paddle
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # collision with floor and ceiling
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        
    #colision with gutters
    if hit_paddle:
        ball_vel[0] = -ball_vel[0]
        hit_paddle = False
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        score2 += 1
        spawn_ball(RIGHT)
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        score1 += 1
        spawn_ball(LEFT)
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
   

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel >= 0 and paddle1_pos + paddle1_vel <= HEIGHT - PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    
    if paddle2_pos + paddle2_vel >= 0 and paddle2_pos + paddle2_vel <= HEIGHT - PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos), 
                         (0, paddle1_pos + PAD_HEIGHT), 
                         (PAD_WIDTH, paddle1_pos + PAD_HEIGHT), 
                         (PAD_WIDTH, paddle1_pos)
                        ], 1, "White", "White")
    a = WIDTH - PAD_WIDTH
    canvas.draw_polygon([(a, paddle2_pos), 
                         (a, paddle2_pos + PAD_HEIGHT), 
                         (a + PAD_WIDTH, paddle2_pos + PAD_HEIGHT), 
                         (a + PAD_WIDTH, paddle2_pos)
                        ], 1, "White", "White")
    
    # determine whether paddle and ball collide
    #left paddle
    
    if ((ball_pos[0] <= PAD_WIDTH + BALL_RADIUS
    and ball_pos[1] >= paddle1_pos + PAD_WIDTH and ball_pos[1] <= paddle1_pos + PAD_WIDTH + PAD_HEIGHT)
    or (ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH
    and ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + PAD_HEIGHT)):
        hit_paddle = True
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1

    # draw scores
    canvas.draw_text(str(score1), (WIDTH / 2 - 20, 20), 20, "White")
    canvas.draw_text(str(score2), (WIDTH / 2 + 10, 20), 20, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    #player 1
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= PAD_VEL
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += PAD_VEL
   
    #player 2
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= PAD_VEL
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += PAD_VEL
        

def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game)


# start frame
new_game()
frame.start()
