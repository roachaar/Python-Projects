##############################################################################
    #  Computer Project #1: National Debt
    #
    #  Algorithm
    #    prompt for national debt and denomination of currency
    #    user inputs the above
    #    program does simple arithmetic to calculate two pieces of information
    #       1: national debt as a height in miles of stacked currency
    #       2: this height compared to the distance between the earth and moon
    #    lastly, the program displays these values to the user
##############################################################################

national_debt_str = input('Enter the national debt: ') #user inputs his or her\ 
#nation's national debt

denomination_str = input('Enter a denomination of currency: ') #user\ 
#inputs a chosen denomination of the same currency as the national debt is\ 
#given in

national_debt_float = float(national_debt_str) #we identify these as the values\
#in which they are meant to be

denomination_int = int(denomination_str) #again

BILL_HEIGHT=.0043 #in inches
INCHES_PER_FOOT= 12 #inches per foot
FEET_PER_MILE=5280 #feet per mile
AVG_DISTANCE_BETWEEN_EARTH_AND_MOON=238857 #in miles

height_of_national_debt_float = (national_debt_float/denomination_int)*\
(BILL_HEIGHT)/(INCHES_PER_FOOT)/(FEET_PER_MILE) #we use dimensional analysis to\
#get the height in miles 

compared_to_moon_float= (national_debt_float/denomination_int)*(BILL_HEIGHT)/\
(INCHES_PER_FOOT)/(FEET_PER_MILE)/(AVG_DISTANCE_BETWEEN_EARTH_AND_MOON) #same\
#thing here, only we now divide by the distance between the earth and the moon

print('The height of your national debt in miles of your chosen denomination of\
 currency is:',height_of_national_debt_float)
print('The ratio of this height and the distance between the earth and the moon\
 is:' ,compared_to_moon_float) #these 2 values are printed for the user to see
