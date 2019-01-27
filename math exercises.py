##############################################################################
    #  Computer Project #3: Exercises
    #
    #  Algorithm (after importing random)
    #    prompt for difficulty and number of problems
    #    difficulty and number of problems in range:
    #       randomly generate the number of problems within difficulty range
    #       user enters his or her answers and is given a score out of 100%
    #    difficulty and/or number of problems out of range:
    #       displays appropriate error message
##############################################################################

import random #so we can generate random stuff

addend=0 #we will keep track of this as the correct answer
correct=0 #we count the number correct
problems=0 #we keep track of the number of problems

difficulty=int(input("Select your difficulty (2+): "))
number_of_problems=int(input("Number of problems (>=1): "))

if difficulty >=2 and number_of_problems>=1: #difficulty and number of\
#problems in range
    range_max=((10**difficulty)-1) #we calculate the highest addend possible\
    #for example, difficulty 3 implies range_max=10**3-1=999, as expected
    
    for i in range(number_of_problems): #for each problem we do this
        print() #skipping lines to make the output look prettier
        print("Problem",i+1, end= ": ")
        
        for j in range(difficulty-1): #within each problem, we print this stuff
            j=int(random.randint(0,range_max))
            print(j, end= " + ")
            addend+=j
            
        for j in range(difficulty-1,difficulty): #this gives and equal sign on\
        #the end. Notice that the range of j was split into 2 parts for this
            j=int(random.randint(0,range_max))
            print(j, end= " =")
            addend+=j #with this, we have our final correct answer
            print()
            answer=int(input("Your answer: ")) #we ask for an answer from the\
            #user
            
        if answer==addend:
            print("Correct!")
            correct+=1 #if correct, we add one to correct
            problems+=1 #we are counting the number of problems
            print() #skipping lines to make the output look prettier
            
        else: #if incorrect, we do this
            print("Wrong, the sum was:" ,addend)
            problems+=1 #we are counting the number of problems
            print() #skipping lines to make the output look prettier
            
        addend=0 #we set the addend back to 0 to begin the next problem
        
    percentage=round(correct/problems*100,1) #standard percentage calculation\
    #with one decimal place
    print("You answered" ,correct, "out of" ,problems, "problems correctly, \
which is",percentage, "percent.") #we display the user's score

if difficulty<2: #error
    print("Difficulty level is too small.") #appropriate error message
    
if number_of_problems<1: #another error 
    print("Number of problems is not big enough.") #appropriate error message  