##############################################################################
    #  Computer Project #10: Solitaire-Alaska
    #
    #  Algorithm
    #    Randomly generate a game of Solitare-Alaska
    #        Imports the 'cards' class, will not work without
    #        Prompt for a command to play a move
    #        If the command/move is valid, the computer executes
    #            One can continue on playing until he or she wins
    #                Alternatively, press q to quit
    #            Prints results neatly and provides appropriate error messages
##############################################################################


import cards   # This line is required

RULES = '''
Alaska Card Game:
     Foundation: Columns are numbered 1, 2, 3, 4
                 Built up by rank and by suit from Ace to King.
                 The top card may be moved.
     Tableau: Columns are numbered 1,2,3,4,5,6,7
              Built up or down by rank and by suit.
              The top card may be moved.
              Complete or partial face-up piles may be moved.
              An empty spot may be filled with a King or a pile starting with a King.
     To win, all cards must be in the Foundation.'''

MENU = '''
Input options:
    F x y : Move card from Tableau column x to Foundation y.
    T x y c: Move pile of length c >= 1 from Tableau column x to Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game
'''                              #menu and rules by Enbody
def valid_move(c1,c2):
    '''return True if suits are the same and ranks differ by 1; c1 & c2 are cards.'''
    if c1.suit()==c2.suit(): #checks for matching suits
        if abs(c1.rank()-c2.rank())==1: #checks for rank difference of 1
            return True
        else:
            return False
    else:
        return False        
        
def tableau_move(tableau,x,y,c):
    '''Move pile of length c >= 1 from Tableau column x to Tableau column y.
       Return True if successful'''
    if tableau[int(y)-1]==[] and tableau[int(x)-1][-1*int(c)].rank()==13:
        print("\nValid Move\n") #we can fill empty spaces with Kings
        tableau[int(y)-1].extend(tableau[int(x)-1][-1*int(c):])
        for i in range(1,int(c)+1):
            tableau[int(x)-1].pop()
    elif tableau[int(y)-1]==[] and tableau[int(x)-1][-1*int(c)].rank()!=13:
        print("\nInvalid Move\n") #ONLY Kings
    elif valid_move(tableau[int(x)-1][-1*int(c)],tableau[int(y)-1][-1])==True:
        print("\nValid Move\n") #if the selected move is valid
        tableau[int(y)-1].extend(tableau[int(x)-1][-1*int(c):]) #extend column
        for i in range(1,int(c)+1): 
            tableau[int(x)-1].pop() #pop initial column
    else:
        print("\nInvalid move\n")

def foundation_move(tableau,foundation,x,y):
    '''Move card from Tableau x to Foundation y.
       Return True if successful'''
    if tableau[x][-1].rank()==1 and foundation[y]==[]:
        foundation[y].append(tableau[x][-1]) 
        tableau[x].pop() #allows us to move Aces to the foundation initially
    elif tableau[x][-1].rank!=1 and foundation[y]==[]:
        print("\nInvalid move\n") #check for validity of command
    else:
        if tableau[x][-1].rank()-foundation[y][-1].rank()==1\
        and tableau[x][-1].suit()==foundation[y][-1].suit():
            foundation[y].append(tableau[x][-1]) #we can stack in order of rank
            tableau[x].pop()
        else:
            print("\nInvalid move\n")

def win(tableau,foundation):
    '''Return True if the game is won.
       Note that you may use the tableau or foundation or both -- your choice.'''
    if tableau==[[],[],[],[],[],[],[]]: #this means all cards are
        return True                     #in the foundation
    else:
        return False
    
def init_game():
    '''Initialize and return the tableau, and foundation.
       - foundation is a list of 4 empty lists
       - tableau is a list of 7 lists
       - deck is shuffled and then all cards dealt to the tableau'''
    foundation = [[],[],[],[]]   
    my_deck = cards.Deck()    #initialize deck
    my_deck.shuffle()         #shuffle
    c_one=[my_deck.deal()] 
    c_two=[my_deck.deal() for i in range(6)]
    c_two[0].flip_card()
    c_three=[my_deck.deal() for i in range(7)]
    c_three[0].flip_card()
    c_three[1].flip_card()
    c_four=[my_deck.deal() for i in range(8)]
    for i in range(3):
        c_four[i].flip_card()
    c_five=[my_deck.deal() for i in range(9)]
    for i in range(4):
        c_five[i].flip_card()
    c_six=[my_deck.deal() for i in range(10)]
    for i in range(5):
        c_six[i].flip_card()
    c_seven=[my_deck.deal() for i in range(11)]
    for i in range(6):
        c_seven[i].flip_card()

#==============================================================================
#       above we deal the deck into columns (lists at the moment)
#       flipping cards as appropriate
#       then we fill the tableau with these soon to be columns
#==============================================================================
        
    tableau = [c_one,c_two,c_three,c_four,c_five,c_six,c_seven]
    return tableau, foundation
    
def display_game(tableau, foundation):
    '''Display foundation with tableau below.
       Format as described in specifications.'''
    print('='*27)
    for i in range(len(foundation)):
        if foundation[i]!=[]:
            print(foundation[i][-1],end="  ")
        else:
            print("_",end="  ")
    print('\n'+'-'*27)
    max_l=max([len(tableau[i]) for i in range(7)])
    for i in range(max_l):
        for j in range(7):
            try:
                card_str=str(tableau[j][i]) #format requires a string
                print("{:>3}".format(card_str),end=" ") 
            except IndexError: #if error, which is bound to happen, print blank
                print("",end="    ")
        print("")
        
def card_flipper(tableau):
    '''Runs through the tableau and flips all top cards that are face down'''
    for i in range(len(tableau)):
        if tableau[i]!=[] and tableau[i][-1].is_face_up()==False:
            tableau[i][-1].flip_card() #we flip unnecessarily face down cards


   

print(RULES)      
tableau,foundation = init_game()
display_game(tableau, foundation)
print(MENU) #beginning provided by Enbody
choice = 'asdf' #some default choice
while choice[0].lower() != 'q': #q will end the loop

    if win(tableau,foundation)==True:
        print("You win!")
        break #winning ends the loop as well
    choice = input("\nEnter a choice: ")
    if choice=="": #handles empty choice
        print("\nPlease enter a valid command")
        choice='asdf'
        continue
    
    elif choice[0].lower()=='f':
        choice=choice.strip().split() #turn choice to list
        if len(choice)==3 and choice[1].isdigit() and choice[2].isdigit():
            foundation_move(tableau,foundation,int(choice[1])-1,\
            int(choice[2])-1)
            card_flipper(tableau) #call card_flipper()
            display_game(tableau,foundation) #display game every move
            print('\nMove card from Tableau to Foundation')
        else:
            print("\nError: Incorrect arguments")
    
    elif choice[0].lower()=='t':
        choice=choice.strip().split() #turn choice to list
        if len(choice)==4 and choice[1].isdigit() and choice[2].isdigit()\
        and choice[3].isdigit():
            tableau_move(tableau,choice[1],choice[2],choice[3])
            card_flipper(tableau) #call card_flipper()
            display_game(tableau,foundation) #display every move
            print('\nMove pile from one column to another')
        else:
            print("\nError: Incorrect arguments")
        
    elif choice.lower()=='r':
        print('\nShuffle and restart')
        tableau,foundation = init_game() #calls function to generate new game
        card_flipper(tableau)
        display_game(tableau, foundation)
        
    elif choice.lower()=='h':
        print(MENU) #in case user forgets directions
            
    else:
        print('\nPlease enter a valid command') 
        
print('\nGame Ended successfully\n') #successful end message