import turtle # Tess becomes a traffic light.
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

#Next functions to change the collor of tess 
# Tess red
def  set_red (): 
   tess.color("red")

# Tess green
def  set_green (): 
   tess.color("green")

# Tess blue
def  set_blue (): 
   tess.color("blue") 

#Next functions to change the size of tess  
#Tess smaller.
def smaller():
    aux = tess.shapesize()
    tess.shapesize(aux[0] * .7, aux[1] * .7, aux[2] * .7)

#Tess larger.
def larger():
    aux = tess.shapesize()
    tess.shapesize(aux[0] / .7, aux[1] / .7, aux[2] / .7)

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()
    
tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")


# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.


# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0: # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1: # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else: # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")

# "link" the pressed keys to the handles  
# PRESS those keys in Caps Lock.
# R to Tess get color red
wn.onkey(set_red, "R") 
# G to Tess get color green
wn.onkey(set_green, "G") 
# B to Tess get color blue
wn.onkey(set_blue, "B") 
#Press s to Tess get smaller 
wn.onkey(smaller, "minus")
#Press l to Tess get larger 
wn.onkey(larger, "plus")

wn.listen() # Listen for events
wn.mainloop()

#Try to implement that for width but when
#call function draw_housing(), I can not use
##################################
#decrease the width of tess pen
'''def decrease_pen():
    pen = tess.pensize() - 1
    if pen >= 0:
        tess.pensize(pen)
#increase the width of tess pen
def increase_pen():
    pen = tess.pensize() + 1
    if pen <= 20:
        tess.pensize(pen)

wn.onkey(decrease_pen, "minus")
wn.onkey(increase_pen, "plus")'''        
##################################
