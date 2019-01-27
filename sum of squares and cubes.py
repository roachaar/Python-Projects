sum_of_squares=0
sum_of_cubes=0

squares_or_cubes=input("Enter 2 to add squares or 3 to add cubes: ")
squares_or_cubes=int(squares_or_cubes)

if squares_or_cubes==2:
    number=input("Enter an integer to square and add, or enter exit to stop: ")
    while number!="exit":
        number=int(number)
        sum_of_squares+=(number*number)
        sum_of_squares=int(sum_of_squares)
        print("Your current sum is:" ,sum_of_squares)
        number=input("Enter an integer to square and add, or enter exit to stop\
: ")
        if number=="exit":
            print("Your final sum of squares is:" ,sum_of_squares)
            print("Program halted appropriately.")
            break
    
elif squares_or_cubes==3:
    number=input("Enter a number you would like to cube and add, or enter\
exit to stop adding cubes: ")
    while number!="exit":
        number=int(number)
        sum_of_cubes+=(number*number*number)
        sum_of_cubes=int(sum_of_cubes)
        print("Your current sum is:" ,sum_of_cubes)
        number=input("Enter an integer to cube and add, or enter exit to stop\
: ")
        if number=="exit":
            print("Your final sum of squares is:" ,sum_of_cubes)
            print("Program halted appropriately.")
            break
        
else:
    print("Please try again and enter 2 or 3 to add squares or cubes.")