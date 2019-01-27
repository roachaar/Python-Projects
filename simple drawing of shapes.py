##############################################################################
    #  Computer Project #2: Drawing Randomly Colored Figures
    #
    #  Algorithm (after importing turtle, random, and time)
    #    prompt for circles or squares
    #    squares:
    #       1: enter a side length to start with
    #       2: program draws until side length is less than 10
    #    circles:
    #       1: user enters a radius to start with
    #       2: program draws until radius is less than 10
    #    After 5 seconds of displaying the drawing, turtle closes
##############################################################################

import turtle,random,time #we will need these

circles_or_squares = input("Enter 1 to draw squares,\
or enter 2 to draw circles:") #user enters a string value
circles_or_squares=int(circles_or_squares) 
#we identify it specifically as an integer so we can work with it

if circles_or_squares == 1: #selecting 1 leads us to squares
    side_length_of_square = input("Enter the starting side length to draw\
    squares with:") #user enters a string value
    side_length_of_square = int(side_length_of_square) #converted to integer
    if side_length_of_square < 10: #length is checked
        print("Squares with side lengths under 10 units will NOT be drawn.")
        #appropriate error message
    else: #this means >=10, so inputting 10 or more will draw at least 1 square
        while side_length_of_square >= 10: #so less than 10 will signal a stop
            (r,g,b) = (random.random(), random.random(), random.random())
            turtle.pencolor(r,g,b)
            turtle.fillcolor(r,g,b)
            turtle.begin_fill() #we turn on the color before drawing
            for j in range(4): 
                turtle.forward(side_length_of_square)
                turtle.right(90) #this sequence makes a square
            side_length_of_square-=10 
            #subtract 10 units from the length each repitition
            turtle.end_fill() #shut the color off now
    time.sleep(5) #display for 5 seconds
    turtle.bye() #close the drawing
    
elif circles_or_squares == 2: #selecting 2 leads us to circles
    radius_of_circle = input("Enter the starting radius to draw circles with:")
    #user enters a string value
    radius_of_circle = int(radius_of_circle)
    #we identify it specifically as an integer so we can work with it
    if radius_of_circle < 10: #length is checked
        print("Circles with radii under 10 units are not worth drawing.") 
        #appropriate error message
    else: #this means >=10, so inputting 10 or mor will draw at least 1 circle
        while radius_of_circle >= 10: #so less than 10 will signal a stop 
            (r,g,b) = (random.random(), random.random(), random.random())
            turtle.pencolor(r,g,b)
            turtle.fillcolor(r,g,b) 
            turtle.begin_fill() #turn the color on before drawing
            turtle.circle(radius_of_circle) #drawing circles is a lot easier
            radius_of_circle-=10 #subtract 10 units from radius each repitition
            turtle.end_fill() #turn the color off now
    time.sleep(5) #display for 5 seconds
    turtle.bye() #close the drawing

else: #it is possible for a user to enter a number that is not 1 or 2
    print("ERROR: You must select 1 or 2 to draw circles or squares,\
 respectively") #results in an appropriate error message
    
    