##############################################################################
    #  Computer Project #5: Salary Lookup
    #
    #  Algorithm
    #    prompt for a file choice until a valid one is entered
    #       given a valid file choice, user inputs occupational keyword
    #           we search each line for the occupational keyword
    #           if line contains occupational keyword, line is printed
    #           program finds maximum, minimum, and average salary
    #           displays appropriate messages in all cases
##############################################################################

#national_M2014_dl.txt

total_salary=0          #we will be keeping track of these 4 variables  
count=0                 
salary_max=0            
salary_min=283482384834 #giant number

file_choice=input("Enter a file to open: ") #initial prompt for a file choice

while True:
    try:
        fp=open(file_choice) #we try to open it
        break #if we open successfully, the loop is broken
    except FileNotFoundError: #if we fail to open such file
        print("File Not Found") #we let the user know we can't find the file
        file_choice=input("Enter a file to open: ") #we ask for another file

occupation=input("Enter a occupational keyword: ") #after the loop is over
occupation=occupation.strip() #we ask for an occupational keyword
occupation=occupation.lower() #we will search the file for this keyword
print() #for aesthetics in the console

for line in fp: #for every line in the file
    occ_title=line[10:120] #we label parts of each line in the file
    occ_salary=line[172:185].strip() #stripped because we will be working with\
                                     #this a lot
    
    if "detailed" in line and "*" not in occ_salary: #check for detailed and\
                                                     #check for existent salary
        occ_salary_str=occ_salary[0:-3]+","+occ_salary[-3:]
        occ_salary_int=int(occ_salary)
        
##############################################################################
    #the following if and elif statements below are very similar, but were\
    #separated so that "Salary" and "Occupation" were only printed once.
##############################################################################
        if occupation in line.lower() and count<1:
            print("Salary    Occupation")
            print("${:>7}  {}".format(occ_salary_str,occ_title))
            
            count+=1                          #count and total salary will be\  
            total_salary+=occ_salary_int      #used to calculate the average
            
            salary_max=occ_salary_int      
            max_title=occ_title            #these 4 hold the initial max/min
            salary_min=occ_salary_int      #max and min are equal at this point
            min_title=occ_title            #we must save the title as well
        elif occupation in line.lower() and count>=1:
            print("${:>7}  {}".format(occ_salary_str,occ_title))
            
            count+=1                          #count and total salary will be\
            total_salary+=occ_salary_int      #used to calculate the average
            
            if occ_salary_int>=salary_max: #these lines use conditional\
                salary_max=occ_salary_int  #statements to keep track of the max\
                max_title=occ_title        #and min, the max/min is changed\
            if occ_salary_int<=salary_min: #each time a new one is found 
                salary_min=occ_salary_int  
                min_title=occ_title        
                
        else: #if occupation was not found in the line
            continue #we move onto the next line
            
    else: #if the line did was not "detailed" or did not have a salary
        continue #we move onto the next line

if salary_max!=salary_min and count!=0: #we see if we need to print max/min
    salary_max_str=str(salary_max) #turned into a string and comma added
    salary_max_str=salary_max_str[0:-3]+","+salary_max_str[-3:]
    salary_min_str=str(salary_min) #turned into a string and comma added
    salary_min_str=salary_min_str[0:-3]+","+salary_min_str[-3:]
    print() #for aesthetics in the console
    print("Max: ${:>7}  {}".format(salary_max_str,max_title))
    print("Min: ${:>7}  {}".format(salary_min_str,min_title))

if salary_max==salary_min and count!=0: #we print a nice message if only one\
                                        #occupation was found

    print() #for aesthetics in the console
    print("We only found one occupation matching your search.")

if count!=0:
    salary_avg=str(int(total_salary/count)) #calculated average, turned into a\
                                            #string after decimal removal
    
    salary_avg_str=salary_avg[0:-3]+","+salary_avg[-3:] #added a comma
    print() #for aesthetics in the console
    print("Across",count,"occupations, the average salary was $"+\
    salary_avg_str)
    
elif count==0: #if no occupations were found matching the given keyword
    print("Sorry, your search did not return any occupations.")