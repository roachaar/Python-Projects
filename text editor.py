##############################################################################
    #  Computer Project #4: Text Editor
    #
    #  Algorithm
    #    show commands and ask user to enter one
    #       command is checked with error responses and termination options
    #           program will only stop with commands
    #           invalid commands display appropriate error messages
    #       start by loading in text to work with
    #           you work with the text by using the given commands
##############################################################################

MENU = '''
--------------------------------------
Commands available:
    'n': Move to Next word
    'p': Move to Previous word
    'i': Insert a word
    'e': Erase current word
    'r': Replace current word
    'c': Cut word, move to copy buffer
    'v': Paste word from copy buffer to before current word
    'l': Load a string
--------------------------------------
'''
print(MENU)#instructor gave us this to use

command=input("Enter a command (h for menu; q to quit): ")

first=""
current=""#the rubric says to name these variables at the beginning
rest=""#so it has been done
bound=0

while command != "q":#so, if we pick q, the program halts

    if command=="l":#load string
        first=""
        current=""#we will reset these values each time the load command is \
        #used
        rest=""
        text=input("Enter some text to edit: ")#appropriate message
        text=text.strip()#we strip unnecessary spaces
        bound=text.find(" ")#find the first space in the user's input
        if bound!=-1:#meaning they entered more than one word
            current=text[:bound]#split off from beginning up to the space
            rest=text[bound+1:]#from beyong the space to the end
            rest=rest.strip()#we strip in case any unnecessary spaces were \
            #added
        else:#if the user only entered one word
            current=text#obviously
            rest=""#obviously
        first=first.strip()#you will notice strip commands periodically
        current=current.strip()#these were later added on
        rest=rest.strip()#they ensure extra spaces are gone at all times
        print("[ "+first+" ]", "[",current,"]","[",rest,"]")#printing this \
        # after each edit
        command=input("Enter a command (h for menu; q to quit): ")#new command
        
    elif command=="n":#next
        if first=="":#empty
            first=current#we shift current over
            first=first.strip()#in case current had extra spaces
            bound=rest.find(" ")#find first space in rest
            if bound==-1:#if it only had one word
                current=rest#we just shift rest over
                rest=""#rest is now empty because it had one word
            elif bound!=-1:#more than one word in rest
                current=rest[:bound]#from beginning up to the space
                rest=rest[bound+1:]#from beyond the space to the end
        elif first!="":#if first is not empty
            first=first+" "+current#we must add a space before adding the word
            first=first.strip()#strip off extras
            bound=rest.find(" ")#exactly the same as above with same reasoning
            if bound==-1:
                current=rest
                rest=""
            elif bound!=-1:
                current=rest[:bound]
                rest=rest[bound+1:]
        first=first.strip()
        current=current.strip() #periodic stripping before printing
        rest=rest.strip()
        print("[ "+first+" ]", "[",current,"]","[",rest,"]")#printing
        command=input("Enter a command (h for menu; q to quit): ")#new command
        
    elif command=="p":#previous
        if rest=="":#if rest is empty
            rest=current#what was in current is now in rest
            bound=first.rfind(" ")#find the last space in the first box
            if bound==-1:#if there is only one word
                current=first#current becomes that one word
                first=""#first is now empty
            elif bound!=-1:#if there is more than one word (a space)
                current=first[bound+1:]#current becomes from beyond the space \
                #to the end
                first=first[:bound]#first loses its ending
        elif rest!="":#if rest is not empty
            rest=current+" "+rest#must add this space
            rest=rest.strip()#we strip off extra spaces
            bound=first.rfind(" ")#find the last space
            if bound==-1:#exactly the same as above, same reasoning
                current=first 
                first="" 
            elif bound!=-1: 
                current=first[bound+1:] 
                first=first[:bound] 
        first=first.strip()
        current=current.strip()#periodic stripping
        rest=rest.strip()
        print("[ "+first+" ]", "[",current,"]","[",rest,"]")#printing
        command=input("Enter a command (h for menu; q to quit): ")#new command
    
    elif command=="i":#insert
        insertion=input("Enter a word to insert: ")#find out what user wants
        insertion=insertion.strip()#strip off spaces
        if first=="":#if first is empty
            first=insertion#it just becomes the insertion
        elif first!="":#if first is not empty
            first=first+" "+insertion#we must add this space on first
        first=first.strip()
        current=current.strip() #periodic stripping
        rest=rest.strip()
        print("[ "+first+" ]", "[",current,"]","[",rest,"]")#printing
        command=input("Enter a command (h for menu; q to quit): ")#new command
    
    elif command=="e":#we will erase current here or replace the empty current
        if rest!="":#if rest is not empty
            bound=rest.find(" ")#we find the first space
            if bound!=-1:#if there is a space (more than one word)
                current=rest[:bound]#we cut off the first word of rest
                rest=rest[bound+1:]#we leave beyond the space to the end
            elif bound==-1:#if there is no space (only one word)
                rest=rest.strip()#we strip rest
                first=first.strip()#we strip first
                current=rest #current just inherits rest
                rest=""#rest becomes empty because current took it
        elif rest=="":#if rest is empty
            bound=first.rfind(" ")#we look at the first box instead
            if bound!=-1:#if there is a space
                current=first[bound+1:] #we give current the last word of first
                first=first[:bound]#we chop it off of first
            elif bound==-1:#if there is only one word
                current=first#we just give it from first to current
                current=current.strip()#we strip in case
                first=""#first is now empty if it was not already empty
        first=first.strip()
        current=current.strip()#periodic stripping
        rest=rest.strip()
        print("[ "+first+" ]", "[",current,"]","[",rest,"]")#printing
        command=input("Enter a command (h for menu; q to quit): ")#new command
   
    elif command=="r":#replace
        current=input("Enter a replacement for the current word: ")#we just \
        #ask the user to change the current box
        current=current.strip()#we strip the input
        first=first.strip()
        current=current.strip()#periodic stripping
        rest=rest.strip()
        print("[ "+first+" ]", "[",current,"]","[",rest,"]")#printing
        command=input("Enter a command (h for menu; q to quit): ")#new command
   
    elif command=="c":#cut and copy
        buffer=current#we save the word current as buffer
        rest=rest.strip()#we strip rest
        bound=rest.find(" ")#we find the first space in rest
        if bound!=-1:#if there is a space (more than one word)
            current=rest[:bound]#we take the first word off of rest and give \
            #it to current
            rest=rest[bound:]#rest keeps its remaining words
        else:#if there is no space (only one word)
            current=rest#we just shift rest over to current
            rest=""#leaving rest empty
        first=first.strip()
        current=current.strip()#periodic stripping
        rest=rest.strip()
        print("[ "+first+" ]", "[",current,"]","[",rest,"]")#printing
        print("Current word has been cut and copied.")#we tell the user they \
        #have successfully copied the current word
        command=input("Enter a command (h for menu; q to quit): ")#new command
    
    elif command=="v":#past
        if first=="":#if first is empty
            first=first+buffer#we just tack on buffer with no space necessary
        else: 
            first=first+" "+buffer#if it is not empty we need a space
        first=first.strip()
        current=current.strip()#periodic stripping
        rest=rest.strip()
        print("[ "+first+" ]", "[",current,"]","[",rest,"]")#printing
        command=input("Enter a command (h for menu; q to quit): ")#new command
        buffer=""#reset buffer to an empty string as instructed
    
    elif command=="h":#help menu
        print(MENU)#instructor gave this to the students to use
        command=input("Enter a command (h for menu; q to quit): ")#new command
   
    else:######################
        print("Please enter a valid command (h for menu; q to quit): ")#invalid
        command=input("Enter a command (h for menu; q to quit): ")#new command

print("")#used to skip a line to make output look more pleasant in console
print("Thank you for using Text Editor.")#ending message