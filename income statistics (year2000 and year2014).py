##############################################################################
    #  Computer Project #7: Income Statistics
    #
    #  Algorithm
    #    7 functions in total are defined
    #        Including basic open_file function and read_file function
    #        The rest interact with the output of the read_file function
    #            1)Program asks for a year and opens that year's file
    #            2)Displays general information for the user
    #            3)Prompts user to ask for more detailed stats
    #                Uses a while loop that calls functions on command
##############################################################################

#national_M2014_dl.txt

import pylab

def open_file():
    """
    Prompts the user to enter a year number for the data file. The program \
    will check whether the year is between 1990 and 2014 (both inclusive).
    """
    year=input("Enter a year where 1990 <= year <= 2014: ") #ask for a year
    while True:
        try:
            year=int(year) #check for a valid year
            if 1990<=year<=2014: #check if within range
                while True: #if it is, we try to open it
                    year=str(year)
                    fp="year"+year+".txt"
                    print(fp)
                    try:
                        file=open(fp) #trying to open the file
                        print("Opened successfully") #success message
                        return file #returning the file for future use
                        break #ending loop
                    except FileNotFoundError:
                        print("File not found, try again.")
                        year=input("Enter a year where 1990 <= year <= 2014: ")
                        break  #go back to original loop to check new year
            else:
                year=input("Please enter a year where 1990 <= year <= 2014: ")
                continue
        except ValueError:
            print("You did not enter a valid year, please do so: ")
            year=input("Enter a year where 1990 <= year <= 2014: ")

def read_file():
    """
    Calls the open_file() function and uses the returned file pointer to read
    the data file. This function returns a list of lists
    """
    file_name=open_file() #call open_file()
    full_list=[]
    for line in file_name:
        if line[0].isdigit(): #ignores first 2 lines without data
            sub_list=line.strip().split() #creating a list
            del sub_list[1] #get rid of the unnecessary column
            for i in range(7): #only need 7
                sub_list[i]=sub_list[i].replace(",","") #get rid of commas
            full_list.append(sub_list) #creating a list of lists
    file_name=str(file_name) #the only way to keep track of the year, sadly
    full_list.append(file_name[29:33]) #the year will always show up here
    full_list[-2][1]=1000000000000 #this number is sufficient
    return full_list #returning full list

def get_range(data_list, percent):
    """
    Takes a list of data and a percent and returns the salary range found from
    said list along with the percent at that salary or below and the average
    """
    i=0
    percent=int(percent)
    range_list=[]
    whole_list_gr=[]
    while i!=-1:
        data_list[i][4]=float(data_list[i][4])
        if data_list[i][4]>percent:
            range_list.append(data_list[i][0]) #making a sub_list of the ranges 
            range_list.append(data_list[i][1]) #min and max seen here
            whole_list_gr.append(range_list)
            whole_list_gr.append(data_list[i][4]) #adding things onto the list
            whole_list_gr.append(data_list[i][6]) #this list will be returned
            whole_list_gr=tuple(whole_list_gr) #turns to a tuple
            return whole_list_gr
            i=-1 #this will end the loop since we found what we're looking for
        else:
            i+=1 #loop goes to the next part of the data_list
            
def get_percent(data_list, income):
    """
    Takes a list of data and an income and returns the cumulative percentage
    for the data line that the specified income is in the income range, 
    and the average income.
    """
    i=0
    while i!=-1:
        range_list_gp=[]
        whole_list_gp=[]
        if float(data_list[i][0])<=float(income)<=float(data_list[i][1]):
            range_list_gp.append(data_list[i][0]) #creating the sub list
            range_list_gp.append(data_list[i][1]) #just as before
            whole_list_gp.append(range_list_gp)
            whole_list_gp.append(data_list[i][4])
            whole_list_gp.append(data_list[i][6]) #appending necessary things
            whole_list_gp=tuple(whole_list_gp)    #making a tuple
            i=-1 #just to be safe and make sure function ends
            return whole_list_gp #though it seems that return is sufficient
        else:
            i+=1 #keep looking

def find_average(data_list):
    """
    Takes a list of data and runs through it to compute and return the average
    salary
    """
    numerator=0
    for i in range(59): #we know each set of data has 59 lines
        data_list[i][6]=float(data_list[i][6])
        data_list[i][2]=int(data_list[i][2])
        numerator+=(data_list[i][6]*data_list[i][2]) #finding numerator
    average=float(numerator)/int(data_list[58][3]) #dividing by number of people
    average=str(average) #making it a string
    while len(average)>8:
        average=average[0:-1] #fixing string length
    average="$"+average[0:2]+","+average[2:] #formatting properly (commas etc.)
    return average


def find_median(data_list):
    """
    Takes a list of data and returns the median income. 
    """
    min_distance=100
    for i in range(59):
        distance=abs(50-float(data_list[i][4])) 
        if distance<=min_distance: #looking for minimum distance
            min_distance=distance
            min_column=i #keep track of the column as well
        else:
            continue
    median=str(data_list[min_column][6])
    median="$"+median[0:2]+","+median[2:]+"0" #formatting our return
    return median

def do_plot(x_vals,y_vals,year): #header and info provided by Dr. Enbody
    '''Plot x_vals vs. y_vals where each is a \
    list of numbers of the same length.'''
    pylab.xlabel('Income')
    pylab.ylabel('Cumulative Percent')
    pylab.title("Cumulative Percent for income in"+" "+year)
    pylab.plot(x_vals,y_vals)
    pylab.show()


data_list=read_file() #program calls read file
average_income_year=find_average(data_list) #finds average and median
median_income_year=find_median(data_list)
print() #for neatness in Console

print("For the year", data_list[-1]+": ") #printing base output here
print("The average income was", average_income_year)
print("The median income was", median_income_year) #very straight-forward
    
x_vals = [float(data_list[i][0]) for i in range(40)] #choosing first 40 values
y_vals = [float(data_list[i][4]) for i in range(40)] #same for the y values
year = data_list[-1] #this is the year
do_plot(x_vals,y_vals,year) #we use our function with the above 3 variables

choice=input("Enter a choice to get (r)ange, (p)ercent, or nothing to stop: ")

while choice!="": #when a nonempty string is entered
    
    if choice=="r": #checking choice
        percent_choice=input("Enter a percent: ") #prompt for percent
        list_choice_r=get_range(data_list,percent_choice) #get_range
        percentage=percent_choice+".00%" #formatting
        print(percentage, "of incomes are below $"+list_choice_r[0][0])
        
        choice=input("Enter a choice to get (r)ange, (p)ercent, \
or nothing to stop: ") #ask for another choice

    elif choice=="p": #checking choice
        income_choice=input("Enter an income: ")
        list_choice_p=get_percent(data_list,income_choice) #get_percent
        income_amount=list_choice_p[0][0]
        if len(income_amount)<=9: #formatting more complicated here
            income_amount="$"+income_amount[0:-6]+","+income_amount[-6:]
        else: #formatting more complicated here
            income_amount="$"+income_amount[0:-9]+","+income_amount[-9:-6]\
            +","+income_amount[-6:]
        percent_of_top=float(list_choice_p[1])
        percent_of_top=round(percent_of_top,2) #more formatting
        percent_of_top=str(percent_of_top) #yields a percentage with 2 decimals
        print("An income of",income_amount,\
        "is in the top "+percent_of_top+"% of incomes.")
        
        
        choice=input("Enter a choice to get (r)ange, (p)ercent, \
or nothing to stop: ") #another choice

    else:
        choice=input("Invalid command, please enter a valid one: ")
        #in case of invalid command
        
print() #neatness
print("Program halted appropriately") #let user know the program has stopped

        
        
        
    
    
        
    
    

    
