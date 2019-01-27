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

#Display the rules of the game
print("\nWelcome to the game of Nim! I'm probably going to win...")
print('''Nim is a simple two-player game based on removing stones.
         The game begins with two piles of stones, numbered 1 and 2. 
         Players alternate turns. Each turn, a player chooses to remove one, 
         two, or three stones from some single pile. The player who removes the
         last stone wins the game.''')

play_str=input("Would you like to play? (0=no, 1=yes) ")
player_turn=1
wins=0
losses=0
while int(play_str) != 0:
    player_turn=1
    pile_1=5
    pile_2=5
    print("There are now 5 stones in each of pile 1 and pile 2, Good luck!")
    while pile_1>0 or pile_2>0:
        while player_turn==1:
            print("Your turn")
            #if pile_1>0 and pile_2>0:
            pile_choice=int(input("Which pile would you like to\
 remove stones from? (Enter '1' for pile 1 or enter '2' for pile 2) "))
            if pile_choice == 1 and pile_1>0:
                valid_pile=1
                while valid_pile==1:
                    how_many = int(input("How many stones would you like to remove from\
 pile 1? "))
                    if pile_1-how_many>=0 and how_many <=3:
                        pile_1=pile_1-how_many
                        print("There are" ,pile_1, "stones remaining in pile 1 and there\
 are" ,pile_2, "stones remaining in pile 2")
                        valid_pile=0
                        player_turn=0
                    else: 
                        print("You can't do that")
                        continue
            elif pile_choice == 2 and pile_2>0:
                valid_pile=1
                while valid_pile==1:
                    how_many = int(input("How many stones would you like to remove from\
 pile 2? "))
                    if pile_2 - how_many >=0 and how_many <=3:
                        pile_2=pile_2-how_many
                        print("There are" ,pile_1, "stones remaining in pile 1 and there\
 are" ,pile_2, "stones remaining in pile 2")
                        valid_pile=0
                        player_turn=0
                    else: 
                        print("You can't do that")
                        continue
            else:
                print("That is not a valid pile number")
                continue
        while player_turn==0:
            if (pile_choice==1 and pile_2>0) or (pile_1==0 and pile_2!=0):
                print("I will take one stone out of pile 2")
                pile_2=pile_2-1
                print("There are" ,pile_1, "stones remaining in pile 1 and there\
 are" ,pile_2, "stones remaining in pile 2")
                player_turn=1
            elif (pile_choice==2 and pile_1>0) or (pile_1!=0 and pile_2==0):
                print("I will take one stone out of pile 1")
                pile_1=pile_1-1
                print("There are" ,pile_1, "stones remaining in pile 1 and there\
 are" ,pile_2, "stones remaining in pile 2")
                player_turn=1
            else:
                break
    if player_turn==0:
        wins+=1
        print("You won this game! Congratulations")
    else:
        losses+=1 
        print("You lost this game, better luck next time!")           
    print("Your current record (W-L) is", wins ,"-", losses)       
        
    play_str = input("\nWould you like to play again? (0=no, 1=yes): ")


print("\nThanks for playing! See you again soon!")
print("\nYour final record is", wins, "-", losses)