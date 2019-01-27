##############################################################################
    #  Computer Project #9: Processing Agricultural Data from Excel
    #
    #  Algorithm
    #    Prompt for 2 files, one food crop and one non-food crop
    #        use dictionary_maker on each fileee to organize its information
    #        7 functions in total
    #            Each plays a unique role in calculating stats from the files
    #                -calculating averages for each year
    #                -calculating max_adoption rates
    #                    -for each crop and year 
    #            Prints results neatly and provides appropriate error messages
##############################################################################

#food_crop.csv
#non-food_crop.csv

def dictionary_maker(fp1):
    '''
    looks through a file and strips it to make a list, then turns this list
    into a dictionary, also grabs what type of crop is being considered
    '''
    crop_dict={}
    for line in fp1:
        if "#" not in line:  
            line=line.strip().split(',')
            crop_dict[line[0]]=line[1:-1] #line[0] is a state, the rest is info
        if "# crop" in line: #this is how we find what crop we're talking about
            a=line.find(":")
            crop_dict['crop']=line[a+2:]
    del(crop_dict['Other States']) #we will not be using this line
    return crop_dict
    
def average_finder(food_dict):
    '''
    looks through a dictionary with str keys and lst values, calculates the
    average of the numbers in the list, ignoring blanks, then puts average into
    the dictionary
    '''
    for key,value in food_dict.items():
        sum_perc=0 #initializing
        count=0
        for item in value:
            if item!="":
                sum_perc+=int(item) #adding and counting to calculate average
                count+=1
        avg="{0:.3f}".format(round(sum_perc/count,3)) #average to 3 decimals
        value.append(avg)
    return food_dict
    
def average_capture(food_avg_dict,non_food_avg_dict):
    '''
    makes a new dictionary combining the information from two other
    dictionaries, dictionary in the form of {key : list of averages}
    '''
    main_avg_dict={}
    for key,value in food_avg_dict.items():
        if key not in non_food_avg_dict.keys():
            main_avg_dict[key]=[value[-1],"N/A"] #this list is now complete
        else:
            main_avg_dict[key]=[value[-1]] #we will append later since there
                                           #is another value to be found
    for key,value in non_food_avg_dict.items():
        if key not in food_avg_dict.keys():
            main_avg_dict[key]=["N/A",value[-1]] #this list is now complete
        elif key in food_avg_dict.keys():
            main_avg_dict[key].append(value[-1]) #this completes the list from
    return main_avg_dict                         #above
    
def max_finder(food_dict):
    '''
    finds the largest number in the list for each key in the dictionary,
    assigns the lowest possible year to max, returns a dictionary of maximums
    '''
    max_dict={}
    for key,value in food_dict.items():
        for i in range(len(value)):
            if value[i]!="":
                value[i]=float(value[i])
            else:
                value[i]=-1 #no percentage will ever be less than 0
                            #so this properly dismisses all empty values
        for i in range(len(value)):
            if value[i]==max(value):
                max_year=food_dict['Years'][i] #so we are done looking now
                break
        max_dict[key]=[max_year,max(value)] #making a new dictionary
    return max_dict
    
def min_finder(food_dict):
    '''
    finds the smallest number in the list for each key in the given dictionary
    and assigns the lowest possible year to thee min, returns a dictionary of
    minimums
    '''
    min_dict={}
    for key,value in food_dict.items():
        for i in range(len(value)):
            if value[i]!=-1: #these are the empty string elements
                value[i]=float(value[i])
            else:
                value[i]=101 #no percentage will ever be higher than 100
                             #so this properly dismisses all empty values
        for i in range(len(value)):
            if value[i]==min(value):
                min_year=food_dict['Years'][i] #we found the minimum, so we
                break                          #stop looking
        min_dict[key]=[min_year,min(value)]
    return min_dict
    
def max_min_dict(max_dict_fc,min_dict_fc):
    '''
    creates a dictionary combining the max values and min values along with
    their respective years in which they occur
    '''
    masterD={}
    masterD.update(max_dict_fc) #updates masterD with the max values
    for key,value in min_dict_fc.items():
        masterD[key].extend(value) #gives the remaining min values
                                   #creating new entries if necessary
    del(masterD['Years']) #didn't need this entry
    return masterD
    
def adoption_rate(max_min_fc):
    '''
    calculates the adoption rate using the max-min master dictionary provided
    by the previous function
    '''
    adoption_rate_dict={} #initialize a dictionary        
    for key,value in max_min_fc.items():
        state=key
        max_year=int(value[0])
        max_value=int(value[1]) #making all of these integers
        min_year=int(value[2])
        min_value=int(value[3])
        if max_year>min_year: #so we get the right sign
            adoption_rate=round((max_value-min_value)/(max_year-min_year),3)
        elif min_year>max_year: #to ensure a correct sign
            adoption_rate=round((min_value-max_value)/(min_year-max_year),3)
        else:
            continue
        if adoption_rate not in adoption_rate_dict:
            adoption_rate_dict[adoption_rate]=[state,min_year,max_year]
        else:
            
#==============================================================================
#       this else statement allows us to give a dummy value to a state,
#       it ensures we don't lose values like Tennessee or Texas that share
#       the same adoption rate
#==============================================================================
            
            adoption_rate+=len(state)+min_year+max_year #add an error term
            adoption_rate_dict[adoption_rate]=[state,min_year,max_year]
    return adoption_rate_dict

crop_file=input("\nEnter a food crop file name: ") #ask for file names
non_crop_file=input("\nEnter a non-food crop file name: ")

while True:
    try:
        fp1=open(crop_file)
        fp2=open(non_crop_file) #try to open both
        found=True #since we found both files
        break
    except FileNotFoundError:
        found=False
        print("\nOne or more of your two files were invalid, Program halting\n")
        break #if we fail to open files, the program will halt and print this
    
if found==True: #found being True indicates both files opened
    food_dict=(dictionary_maker(fp1))
    crop_fc=food_dict.pop('crop') #we immediately pop the crop entry
    non_food_dict=(dictionary_maker(fp2))
    crop_nfc=non_food_dict.pop('crop') #it is saved for our printing later
    
    food_avg_dict = average_finder(food_dict) #just calling functions above
    non_food_avg_dict = average_finder(non_food_dict) #for each crop
    
    main_avg_dict = average_capture(food_avg_dict,non_food_avg_dict)
    main_avg_dict = sorted(main_avg_dict.items()) #this allows us to print below
                                                  #in alphabetical order with ease  
    
    print("\n{:<16}{:>12}{:>16}".format("State","Food Crop","Non-Food Crop"))
    for i in range(len(main_avg_dict)):
        if main_avg_dict[i][0]!="Years":
            print("{:<16}{:>12}{:>16}".format(main_avg_dict[i][0],\
            main_avg_dict[i][1][0],main_avg_dict[i][1][1]))
    print("-"*50,"\n") #basic printing/formatting going on here
        
    max_dict_fc=max_finder(food_dict)
    max_dict_nfc=max_finder(non_food_dict) #calling functions again
    
    min_dict_fc=min_finder(food_dict)
    min_dict_nfc=min_finder(non_food_dict) #more calling of our functions

    max_min_fc=max_min_dict(max_dict_fc,min_dict_fc)
    max_min_nfc=max_min_dict(max_dict_nfc,min_dict_nfc) #calling
    
    adoption_rate_dict_fc=adoption_rate(max_min_fc)
    adoption_rate_dict_nfc=adoption_rate(max_min_nfc) #and again, last one
    
#==============================================================================
#   we now have all of our max_adoption rate information, but we must correct
#   our error term from earlier, we this is done for each one below  
#============================================================================== 
    
    adoption_rate_dict_fc=sorted(adoption_rate_dict_fc.items()) #sorting tuples
    adoption_rate_dict_fc.reverse() #descending order
    for i in range(len(adoption_rate_dict_fc)):
        adoption_rate_dict_fc[i]=list(adoption_rate_dict_fc[i]) #make it a list
        if adoption_rate_dict_fc[i][0]>1000: #indicates we added error term
            adoption_rate_dict_fc[i][0]-=(adoption_rate_dict_fc[i][1][1]+\
            adoption_rate_dict_fc[i][1][2]+len(adoption_rate_dict_fc[i][1][0]))
    adoption_rate_dict_fc=sorted(adoption_rate_dict_fc)
    adoption_rate_dict_fc.reverse()
    
#==============================================================================
#   we are just subtracting the same numbers we added on earlier to preserve
#   uniqueness, this gives us our actual data back    
#==============================================================================
    
    adoption_rate_dict_nfc=sorted(adoption_rate_dict_nfc.items())
    adoption_rate_dict_nfc.reverse() #now in descending order
    for i in range(len(adoption_rate_dict_nfc)):
        adoption_rate_dict_nfc[i]=list(adoption_rate_dict_nfc[i]) #list this
        if adoption_rate_dict_nfc[i][0]>1000: #indicates we added error term
            adoption_rate_dict_nfc[i][0]-=(adoption_rate_dict_nfc[i][1][1]+\
            adoption_rate_dict_nfc[i][1][2]+\
            len(adoption_rate_dict_nfc[i][1][0]))
    adoption_rate_dict_nfc=sorted(adoption_rate_dict_nfc)
    adoption_rate_dict_nfc.reverse() #the error term has been taken care of
                                     #and now we can print    
        
    print("Percent max_adoption rate for food crop.")
    print("\nCrop: ",crop_fc) #our food crop from way earlier is used
    print("{:<16}{:>8}{:>11}{:>11}\n"\
    .format("State","Rate","Min-year","Max-year")) #formatting
    for i in range(len(adoption_rate_dict_fc)):
        print("{:<16}{:>+8.3f}{:>11}{:>11}".format(adoption_rate_dict_fc[i]\
        [1][0],adoption_rate_dict_fc[i][0],adoption_rate_dict_fc[i][1][1]\
        ,adoption_rate_dict_fc[i][1][2]))
     
    print("-"*50,"\n")

    print("Percent max_adoption rate for non-food crop.")
    print("\nCrop: ",crop_nfc) #our non-food crop from way earlier is used
    print("{:<16}{:>8}{:>11}{:>11}\n"\
    .format("State","Rate","Min-year","Max-year")) #formatting
    for i in range(len(adoption_rate_dict_nfc)):
        print("{:<16}{:>+8.3f}{:>11}{:>11}".format(adoption_rate_dict_nfc[i]\
        [1][0],adoption_rate_dict_nfc[i][0],adoption_rate_dict_nfc[i][1][1]\
        ,adoption_rate_dict_nfc[i][1][2]))
            
    print("\nProgram finished displaying results\n") #completion message
            


             
    
    