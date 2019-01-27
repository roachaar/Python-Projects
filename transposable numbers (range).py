##############################################################################
    #  Computer Project #6: Transposable Numbers
    #
    #  Algorithm
    #    6 functions in total are defined
    #        many of the functions are composed of their preceding functions
    #        there is only one line of code other than the functions
    #            1)process_file() prompts for a file using open_file()
    #            2)process_file() applies the other functions to the file
    #            3)process_file() prints results: transposed numbers
##############################################################################

#range.txt

def rotate(string):
    """
    Takes a string and moves the last character to the front
    string: the string to be processed (str)
    Returns: The string with the last character moved to the front
    """
    string=str(string)
    string=string[-1]+string[0:-1] #the last letter is now first
    return string
   
def is_transpose(string1,string2):
    """
    Takes 2 strings and checks if they match
    If the strings do not match, we rotate string2 and check again
    Returns: If no match is found through repeated rotations: False
    Returns: If a match is found through repeated rotations:  True
    """
    string1=str(string1)
    string2=str(string2)
    count=0
    while count<=len(string1):
        if string1==string2: #a match
            return True
        elif string1!=string2: #not a match
            string2=rotate(string2) #rotation happens
            count+=1 #we count rotations so we don't rotate forever
    return False

def get_transposability(number):
    """
    Takes a number and multiplies it by the digits 2 through 9
    Then checks value of is_transpose
    Returns: If is_transpose returns True, we print the product
    Returns: If is_transpose returns False, we do not print the product
    """
    for i in range(2,9+1): #multiplying from 2 to 9
        number=int(number)
        multiple=i*number
        multiple=str(multiple)
        workable=multiple #we want to print the unrotated multiple
        if is_transpose(number,workable)==True: #number is transposable
            print("    "+str(number)+" * "+str(i)+" = "+multiple)
        elif is_transpose(number,workable)==False: #number is not transposable
            continue

def get_transposability_zero(number):
    """
    Takes a number of one less order of magnitude and adds a "0" to the front
    Then checks value of is_transpose with each multiple (2 through 9)
    Returns: If is_transpose returns True, we print the product
    Returns: If is_transpose returns False, we do not print the product     
    """
    number_str=str(number)
    number_str="0"+number_str #putting a zero at the beginning of a string
    for i in range(2,9+1):
        multiple=i*number
        multiple=str(multiple)
        workable=multiple #same as in get_transposability
        if is_transpose(number_str,workable)==True:
            print("    "+number_str+" * "+str(i)+" = "+multiple)
        elif is_transpose(number,workable)==False:
            continue

def open_file():
    """
    Prompts for a file choice
    Attempts to open the file
    If no such file exists, we ask for another
    When a valid file is entered, the file is opened
    """
    file_choice=input("Input file name: ") #ask for a file name
    while True:
        try:
            fp=open(file_choice) #try to open it
            return fp #return it if it works
            break
        except FileNotFoundError: #if no file is found
            print("File Not Found") #print error statement
            file_choice=input("Input file name: ") #ask for a new one

def process_file():
    """
    Calls open file
    Finds a start and end value
    Checks numbers from start to end value and prints transposable ones
        This is done using get_transposabiity and get_transposability_zero
    """
    fp=open_file() #call open file
    for line in fp: #once file is opened
        line=line.strip() 
        if "start" in line or "end" in line: #we don't want this line
            continue
        else: #here we find start and end numbers
            space=line.find(" ")
            start=line[0:space]
            end=line[space:]
            end=end.strip()
    print("\nTransposed numbers from"+" "+start+" to "+end)
    print()
    for i in range(int(start),int(end)+1): #from start to end
        if i<100000: #we find transposables from start to 99999
            get_transposability_zero(i)
        else: #from 100000 to end
            get_transposability(i)
            
process_file() #we simply call process_file() and it does all of the work

    