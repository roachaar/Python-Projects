##############################################################################
    #  Computer Project #11: APID shapes
    #
    #  Algorithm
    #    Draws shapes on a 4 quadrant plane based on a given PID and size
    #        Imports turtle,time,math,random
    #        Prompt for an appropriate PID and side length
    #        If valid input is given, a picture is drawn
    #            Shapes are chosen by getHash function
    #                draws 4 shapes in 4 quadrants in TurtleGraphics
##############################################################################

import turtle
import time
import math
import random

def drawShape(shape,side):
    '''
    Draws a shape given a number and side length
    Each integer on [0,9] corresponds to a different shape
    '''
    #Setting turtle up
    (r,g,b) = (random.random(), random.random(), random.random())
    turtle.pencolor(r,g,b)
    turtle.fillcolor(r,g,b)
    turtle.begin_fill()

    #Start drawing    
    turtle.down()
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)

    if shape == 1: #straight line
        turtle.left(135)
        turtle.forward(math.sqrt(2*side*side))
        
    elif shape == 2: #steps
        turtle.left(90)
        for i in range(1,3):
            #Alternate between vertical and horizontal lines
            turtle.forward(side/2) #horizontal
            turtle.left(90)
            turtle.forward(side/2) #vertical
            turtle.right(90)
        
    elif shape == 3: #unbroken step
        turtle.left(90)
        turtle.forward(side/4)
        turtle.left(45)
        #Calculate length of hypotenuse
        turtle.forward(math.sqrt(9*side*side/8))
        turtle.left(45)
        turtle.forward(side/4)
        
    elif shape == 4: #convex quartercircle
        turtle.left(90)
        turtle.circle(side,90)
    
    elif shape == 5: #concave quartercircle
        turtle.left(180)
        #Negative radius changes turtle direction
        turtle.circle(-side,90)
    
    elif shape == 6: #periodic wave
        turtle.left(180)
        turtle.circle(-side/5,90) #down circle
        turtle.circle(side/5,90) #up circle
        turtle.circle(-side/5,90) #down circle
        turtle.circle(side/5,90) #up
        turtle.circle(-side/5,90) #down
    
    elif shape == 7: #pentagon on a plane 
        turtle.left(90)
        turtle.forward(side/(3+(2/5))) #preserves symmetricity
        turtle.left(45)
        turtle.forward(side/(3+(2/5)))
        turtle.right(90)
        turtle.forward(side/(3+(2/5)))
        turtle.left(45)                
        turtle.forward(side/(3+(2/5))) #this draws a pentagon
        turtle.left(90)
        turtle.forward(side/(3+(2/5)))
        turtle.left(45)
        turtle.forward(side/(3+(2/5)))
        turtle.right(90)
        turtle.forward(side/(3+(2/5))) #symmetricity
        
    elif shape == 8: #Marlena's Snowflake
        turtle.left(135)
        turtle.forward(side/(4+(8/9))) #symmetricity
        turtle.left(45)
        turtle.forward(side/(4+(8/9))) #follows from geometry
        turtle.right(45)
        turtle.forward(side/(4+(8/9)))
        turtle.right(45)
        turtle.forward(side/(4+(8/9)))
        turtle.left(90)
        turtle.forward(side/(4+(8/9)))
        turtle.right(45)
        turtle.forward(side/(4+(8/9)))
        turtle.right(45)
        turtle.forward(side/(4+(8/9)))
        
    elif shape == 9: #half-pipe
        turtle.left(90)
        turtle.forward(side/3)
        turtle.left(90)
        turtle.forward(side/3)
        turtle.circle(-side/3,90) #one fourth of a circle
        turtle.forward(side/3)
        turtle.left(90)
        turtle.forward(side/3)
    
    else: # shape == 0: #puzzle piece
        turtle.left(135)
        turtle.forward(side/4)
        turtle.right(90)        #begins drawing stump
        turtle.forward(side/10) #height
        turtle.left(90)
        turtle.forward(side/10)
        turtle.left(90)
        turtle.forward(side/10) #height
        turtle.right(90)
        turtle.forward(side/10) #finishes drawing a stump
        turtle.right(90)
        turtle.forward(side/8) #a taller stump
        turtle.left(90)
        turtle.forward(side/10)
        turtle.left(90)
        turtle.forward(side/8) #gets taller
        turtle.right(90)
        turtle.forward(side/10)
        turtle.right(90)
        turtle.forward(side/6) #tallest stump
        turtle.left(90)
        turtle.forward(side/10)
        turtle.left(90)
        turtle.forward(side/6) #tallest
        turtle.right(90)
        turtle.forward(side/10)
        turtle.right(90)
        turtle.forward(side/8) #medium sized stump again
        turtle.left(90)
        turtle.forward(side/10)
        turtle.left(90)
        turtle.forward(side/8) #medium, part 2
        turtle.right(90)
        turtle.forward(side/10)
        turtle.right(90)
        turtle.forward(side/10) #back to original height
        turtle.left(90)
        turtle.forward(side/10)
        turtle.left(90)
        turtle.forward(side/10) #original height
        turtle.right(90)
        turtle.forward(side/10)
    
    turtle.end_fill()
    turtle.up()
    turtle.setpos(0,0)
    turtle.seth(0)
    
def getHash(value):
    '''
    Given a string of 2 numbers, adds the numbers together and
    divides by 10, returns this value as the hash_value
    '''
    a=int(value[0])+int(value[1])
    hash_value=a%10
    return hash_value
    #return hash corresponding to value
    #e.g. the digits of the number 93 sum upto 12
    #the units digit of 12 is 2
    #thus 93 gets hashed to 2

def drawQ1(identifier,side):
    '''
    Draws in the top-left quadrant by positioning turtle
    '''
    #1. position turtle
    turtle.goto(-side, 0)
    #2. calculate hash for the digits corresponding to Q1
    shape=getHash(identifier[1]+identifier[2])
    #3. call drawShape with appropriate arguments(Q1's shape
    #   will be the hash from step 2) to draw the shape 
    #   in the 1st quadrant
    drawShape(shape,side)    

def drawQ2(identifier,side):
    '''
    Draws in the bottom-right quadrant by positioning turtle
    '''
    #1. position turtle
    turtle.goto(0,-side)
    turtle.left(90)
    #2. calculate hash for the digits corresponding to Q2
    shape=getHash(identifier[3]+identifier[4])
    #3. call drawShape with appropriate arguments(Q2's shape
    #   will be the hash from step 2) to draw the shape 
    #   in the 2nd quadrant
    drawShape(shape,side)
    
def drawQ3(identifier,side):
    '''
    Draws in the bottom-right quadrant by positioning turtle
    '''
    #1. position turtle 
    turtle.goto(side,0)
    turtle.right(180)
    #2. calculate hash for the digits corresponding to Q3
    shape=getHash(identifier[5]+identifier[6])
    #3. call drawShape with appropriate arguments(Q3's shape 
    #   will be the hash from step 2) to draw the shape 
    #   in the 3rd quadrant
    drawShape(shape,side)

def drawQ4(identifier,side):
    '''
    Draws in the top-right quadrant by positioning turtle
    '''
    #1. position turtle 
    turtle.goto(0,side)
    turtle.right(90)
    #2. calculate hash for the digits corresponding to Q4
    shape=getHash(identifier[7]+identifier[8])
    #3. call drawShape with appropriate arguments(Q4's shape 
    #   will be the hash from step 2) to draw the shape 
    #   in the 4th quadrant
    drawShape(shape,side)
            
#**** Need to error check both inputs
while True:
    side=input("\nPlease enter the total length of the figure: ")
    try:
        side=int(side) #this checks if side was a number
        if side<=800: #800 is larger than the turtle window
            break #given a valid side, we end this loop
        else:
            print("\nSide too large, please enter a side length <= 800")
    except ValueError: #this checks if the side length is a real number
        print("\nPlease enter a side length less than or equal to 800")

while True:
    identifier=input("\nPlease enter MSU ID (including the starting letter): ")
    if identifier[0].isalpha(): #if the first digit is a letter
        if identifier[1:].isdigit(): #if the rest is a number
            if len(identifier[1:])==8: #with length 8
                break #then we end the loop
            else:
                print("\nA valid PID has one letter followed by 8 numbers")
        else:
            print("\nPlease enter a valid PID (one letter \
followed by 8 numbers)")
    else:
        print("\nPlease enter a valid PID if including the first letter")

turtle.colormode(1.0)
turtle.speed(0)

drawQ1(identifier,side/2) #calls to draw in each of 4 quadrants
drawQ2(identifier,side/2)
drawQ3(identifier,side/2)
drawQ4(identifier,side/2)

time.sleep(10) #shows picture for 20 seconds
turtle.bye()
