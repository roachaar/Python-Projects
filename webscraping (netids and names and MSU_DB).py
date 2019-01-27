##############################################################################
    #  Computer Project #8: The MSU Directory
    #
    #  Algorithm
    #    We were given 3 functions that should all behave the same
    #        choosing to run off of sample_2.py provided
    #        8 of the 10 listed functions are used
    #            1)Program asks for a command from the user
    #                -Program can add people's information to a dictionary
    #                -Use files to search for thousands of names/NetIDs at once
    #                -Write to files and create a local database 
    #            2)Prints appropriate error messages
##############################################################################

#netids.txt
#names.txt


import requests
from bs4 import BeautifulSoup

def query_MSU_online_database(payload):
    '''Scrape one name (specified in payload) from MSU's People web page;
       return a one-element dictionary with NetID as the key.'''
    D = {}
    try:    
        '''
        This function is called for each student. It begins by posting
        payload (NetID or Firstname, Lastname) to the MSU people database.
        '''
        primary_URL = "https://search.msu.edu/people/"
        response = requests.post(primary_URL, data=payload, timeout=20)
        soup = BeautifulSoup(response.content, "lxml")
        
        '''This little part below is very important. We need to grab the UID
        of each student and then contruct a link using this UID. 
        This secondary link will contain the private details we are looking for.
        To understand why we need to do this, query the MSU people database 
        manually and observe the creation of the link containing the UID that 
        we are required to click before student's private details are shown to us.
        '''
        uid = ""
        for uid in soup.find_all('li',{'class':'name'}):
            if uid.a:    
                uid = uid.a.get("href")
        secondary_URL = 'https://search.msu.edu/people/' + uid
        print (secondary_URL)
        response = requests.get(secondary_URL)
        soup = BeautifulSoup(response.content, "lxml")
        #pretty_HTML = soup.prettify() #used this to observe HTML while coding
        #print(pretty_HTML)            #to know what to search for
        
        '''
        In this next part, we look for private details of students,
        print them on the screen, and store them in a file.
        '''    
        name, current_address, current_phone, permanent_address,\
        permanent_phone, mail_id, title, status, major = "","","","","","","","",""
        for info in soup.find_all('li',{'class':'name'}):
            name = info.text.strip()
        for info in soup.find_all('li',{'class':'homepostaladdress'}):
            current_address = info.text.strip()
        for info in soup.find_all('li',{'class':'homephone'}):
            current_phone = info.text.strip()
        for info in soup.find_all('li',{'class':'permanentpostaladdress'}):
            permanent_address = info.text.strip()
        for info in soup.find_all('li',{'class':'permanentphone'}):
            permanent_phone = info.text.strip()
        for info in soup.find_all('li',{'class':'mail'}):
            mail_id = info.text.strip()
        for info in soup.find_all('li',{'class':'title'}):
            title = info.text.strip()
        for info in soup.find_all('li',{'class':'classdesc'}):
            status = info.text.strip()
        for info in soup.find_all('li',{'class':'majordesc'}):
            major = info.text.strip()
        
        # HERE ARE SOME PRINT STATEMENTS TO ILLUSTRATE USAGE OF SOME OF THE VARIABLES
        ##print ("-" * 50)
        ##print("[ + ] Name: {}".format(name))
        ##print ("-" * 50)
        ##print("[ + ] Current Address: {}".format(current_address))

        # LET'S PUT SOMETHING IN D. YOU WILL WANT TO PUT IN MORE
        # Also, you will want the key to be the NetID which you need to extract from "mail"
        D[name] = [current_address]
        
        return D  
        
    except requests.ConnectionError:
        print("[ - ] No internet connection available.")
    except requests.exceptions.ReadTimeout:
        print("Connection timed out")
        
def tempQuery(payload):
    if ('nid' not in payload) and \
       ('fst' not in payload or 'lst' not in payload):
        raise ValueError
    
    samples = [
        {'hillbob' : ['Hill, Bob Fred',
                      '61 Noff Rd Morris MI 48458',
                      '810-225-8275',
                      '',
                      '',
                      'hillbob@msu.edu',
                      'Title: Student',
                      'Status: Freshman',
                      'Major: Mechanical Engineering']},
        {'wangalle' : ['Wang, Allen',
                       '16 Chandler Rd Apt 123 East Lansing MI 48823',
                       '714-970-7265',
                       '8106 Adding Dr Walloon Lake MI 48390',
                       '238-160-3230',
                       'wangalle@msu.edu',
                       'Title: Student',
                       'Status: Sophomore',
                       'Major: Computer Engineering']}]

    result = {'' : ['','','','','','','','','']}
    if 'nid' in payload:
        if payload['nid'] =='hillbob':
            result = samples[0]
        elif payload['nid'] == 'wangalle':
            result = samples[1]

    elif 'fst' in payload and 'lst' in payload:
        if payload['fst'] == 'Allen' and payload['lst'] == 'Wang':
            result = samples[1]
        elif payload['fst'] == 'Bob' and payload['lst'] == 'Hill':
            result = samples[0]
        

    ls = list(result.items())
    name = ls[0][0]
    data = ls[0][1]

    print ("-" * 50)
    print("[ + ] Name: {}".format(data[0]))
    print ("-" * 50)
    print("[ + ] Current Address: {}".format(data[1]))

    return result
    
def query_MSU_online_database_fake(payload):
    """ This function replaces the original query_MSU_online_database function.
        That function retrieved information from a web page; this function
        pretends to do the same thing: it takes a payload in the form of a netID
        or name and returns information about that person."""
     
    # netids and names allow us to index into our samples list 
    # (this is ugly but we are stuck because of the hasty design on Saturday)
    netids = ['hillbob','wangalle','hopperg','wozsteve']
    names = [('Hill','Bob'),('Wang','Allen'),('Hopper','Grace'),('Wozniak','Steve')]
    
    if ('nid' not in payload) and \
       ('fst' not in payload or 'lst' not in payload):
        raise ValueError
    
    # samples should have been a dictionary, but it was created in haste on Saturday
    samples = [
        {'hillbob' : ['Hill, Bob Fred',
                      '61 Noff Rd Morris MI 48458',
                      '810-225-8275',
                      '',
                      '',
                      'hillbob@msu.edu',
                      'Title: Student',
                      'Status: Freshman',
                      'Major: Mechanical Engineering']},
        {'wangalle' : ['Wang, Allen',
                       '16 Chandler Rd Apt 123 East Lansing MI 48823',
                       '714-970-7265',
                       '8106 Adding Dr Walloon Lake MI 48390',
                       '238-160-3230',
                       'wangalle@msu.edu',
                       'Title: Student',
                       'Status: Sophomore',
                       'Major: Computer Engineering']},
        {'hopperg'  : ['Hopper, Grace',
                       '127 Harrison Rd, East Lansing MI 48823',
                       '517-123-4567',
                       '27 Main St., South Haven, MI, 49090',
                       '269-123-9876',
                       'hopperg@msu.edu',
                       'Title: Student',
                       'Status: Senior',
                       'Major: Mathematics']},
        {'wozsteve' : ['Wozniak, Steve',
                       '345 University Dr., East Lansing, MI 48823',
                       '408-293-2468',
                       '1 Infinite Loop, Cupertino, CA 95015',
                       '',
                       'wozsteve@msu.edu',
                       'Title: Student',
                       'Status: Sophomore',
                       'Major: Computer Engineering']}
                       ]
    result = {}

    # if netid
    if 'nid' in payload:
        if payload['nid'] in netids:
            result = samples[netids.index(payload['nid'])]
    # else name
    elif 'fst' in payload and 'lst' in payload:
        if (payload['lst'], payload['fst']) in names:
            result = samples[names.index((payload['lst'], payload['fst']))]
             
    if not result: # if result is empty
        return result
        
    ls = list(result.items())
    name = ls[0][0]
    data = ls[0][1]

    print ("-" * 50)
    print("[ + ] Name: {}".format(data[0]))
    print ("-" * 50)
    print("[ + ] Current Address: {}".format(data[1]))
    print ("-" * 50)
    print("[ + ] Current Phone: {}".format(data[2]))
    print ("-" * 50)
    print("[ + ] Permanent Address: {}".format(data[3]))
    print ("-" * 50)
    print("[ + ] Permanent Phone: {}".format(data[4]))
    print ("-" * 50)
    print("[ + ] Mail ID: {}".format(data[5]))
    print ("-" * 50)
    print("[ + ] {}".format(data[6]))
    print ("-" * 50)                        # prints off information found
    print("[ + ] {}".format(data[7]))       # from the search
    print ("-" * 50)
    print("[ + ] {}".format(data[8]))   
    return result

def banner():
    '''Just a banner''' #Enbody's function, self-explanatory
    asciitext = '''
     __  __ ____  _   _   ____  _        _ _             
    |  \/  / ___|| | | | / ___|| |_ __ _| | | _____ _ __ 
    | |\/| \___ \| | | | \___ \| __/ _` | | |/ / _ \ '__|
    | |  | |___) | |_| |  ___) | || (_| | |   <  __/ |   
    |_|  |_|____/ \___/  |____/ \__\__,_|_|_|\_\___|_|   
                                                 
      ____           _             _ 
     / ___|___ _ __ | |_ _ __ __ _| |
    | |   / _ \ '_ \| __| '__/ _` | |
    | |__|  __/ | | | |_| | | (_| | |
     \____\___|_| |_|\__|_|  \__,_|_| CSE 231 - Spring 2016
     '''
    print(asciitext)

MENU = '''
  1. NetID
  2. Firstname Lastname
  3. Multiple NetIDs from file
  4. Multiple Firstname Lastname pairs from file
  5. Display dictionary
  6. Remove name from dictionary
  7. Write dictionary
  x. Exit'''


    
'''
Main Function: Input file type refers to whether we are providing an input
file that contains: 1. Firstname Lastname pairs or
2. NetIDs. The user is forced to choose between 1 or 2.
The function 'query_MSU_online_database()' is called for each
line in these files (each call corresponds to 1 student)
'''

def netid_query(masterD,name):
    '''
    netid_query searches the database for a provided netid and
    prints information and puts it in a dictionary
    '''
    payload = {'nid':name}
    if len(name)>8:
        print("\nAll NetIDs are composed of 8 characters or less")
    elif len(name)<=8:
        D = query_MSU_online_database_fake(payload)
        masterD.update(D)
        if D=={}: #this means no such NetID was found
            print("\nNetID not found")
        
def name_query(masterD,name):
    '''
    name_query searches the database for a provided name (first and last) and
    prints information and puts it in a dictionary
    '''
    name=name.lower().split()    #turn into a list and capitalize first letter
    payload = {'lst':name[1].capitalize(),'fst':name[0].capitalize()}
    D = query_MSU_online_database_fake(payload)
    masterD.update(D)
    if D=={}: #this means we didn't find the name
        print("\nName not found")

def open_file():
    '''
    standard open file function that asks for a file to open until a valid file
    is entered
    '''
    file_choice=input("\nWhat file would you like to open? Enter here: ")
    while True:
        try:
            print("\n--Attempting to open "+file_choice+"--")
            fp=open(file_choice)
            break               #ends the loop
        except FileNotFoundError:
            print("\nFile not found")      #error message
            fp=input("\nEnter another file choice: ")  #asks for another input
    print("\n--Successfully opened "+file_choice+"--")
    return fp  #return the file

def multiple_netid_query(masterD):
    '''
    uses the single netid_query function on each line of a file and prints out
    the info associated with each NetID if any
    '''
    fp=open_file() #calling open file
    for line in fp:
        line=line.split() #turn it into a list incase weird input is entered
        netid_query(masterD,line[0]) #line[0] is a NetID, calling function
        print()
        
def multiple_name_query(masterD):
    '''
    uses the single name_query function on each line of a file and prints out
    the info associated with each Name on each line if any exists
    '''
    fp=open_file() #calling open_file
    for line in fp:
        name_query(masterD,line) #calling name_query
        print()

def dictionary_printer(masterD):
    '''
    looks inside of masterD and prints the information of each person
    contained in it in a way similar to the 'database_query' function above
    '''
    for key,value in masterD.items():
        print ("-" * 50)                     #nothing new here, just printing
        print("[ + ] Name: {}".format(value[0]))
        print ("-" * 50)
        print("[ + ] Current Address: {}".format(value[1]))
        print ("-" * 50)                     #with a bit of formatting
        print("[ + ] Current Phone: {}".format(value[2]))
        print ("-" * 50)
        print("[ + ] Permanent Address: {}".format(value[3]))
        print ("-" * 50)
        print("[ + ] Permanent Phone: {}".format(value[4]))
        print ("-" * 50)
        print("[ + ] Mail ID: {}".format(value[5]))
        print ("-" * 50)
        print("[ + ] {}".format(value[6]))
        print ("-" * 50)
        print("[ + ] {}".format(value[7]))
        print ("-" * 50)
        print("[ + ] {}".format(value[8]))   #pretty standard printing going on
        print()
        
def dictionary_removal(masterD,netid):
    '''
    prompts for a NetID and removes that NetID from the master dictionary
    if it currently exists in there
    '''
    if netid in masterD:    
        masterD.pop(netid.lower()) #.pop removes the netid from the dictionary        
    elif netid not in masterD:
        print("\nThat NetID is not currently in the master dictionary")    
    
banner() #we call banner
print(MENU) #prints menu

masterD = {} #initialize our main dictionary we will be working with

choice=input("\nWhat would you like to do? (enter a command): ") #prompts for
                                                                 #first command
while choice!="x": #so, if x is entered, we stop the while loop
    if choice=='1':
        print("\n--NetID--")
        given_netid = input ("\n[ i ] Enter NetID: ")
        given_netid = given_netid.lower() #turn input to lowercase
        netid_query(masterD,given_netid) #call function
        choice=input("\nWhat would you like to do next? (enter a command): ")
        
    elif choice=='2':
        print("\n--Firstname Lastname--")
        firstlast = input("\n[ i ] Enter Firstname Lastname: ")
        fstlst_list = firstlast.split() #turn the given name into a list
        if len(fstlst_list)!=2: #check for length=2 (2 names given, fst+lst)
            print("\nYou didn't enter a first and last name")
        else:
            name_query(masterD,firstlast) #call function
        choice=input("\nWhat would you like to do next? (enter a command): ")
        
    elif choice=='3':
        print("\n--Multiple NetIDs from file--")
        multiple_netid_query(masterD) #call function
        choice=input("\nWhat would you like to do next? (enter a command): ")
        
    elif choice=='4':
        print("\n--Multiple Firstname Lastname pairs from file--")
        multiple_name_query(masterD) #call function
        choice=input("\nWhat would you like to do next? (enter a command): ")
        
    elif choice=='5':
        print("\n--Display dictionary--")
        print()
        dictionary_printer(masterD) #just calls function above
        choice=input("\nWhat would you like to do next? (enter a command): ")
        
    elif choice=='6':
        print("\n--Remove name from dictionary--")
        netid=input("\nEnter a NetID to remove from the master dictionary: ")
        dictionary_removal(masterD,netid.lower()) #calls function above
        choice=input("\nWhat would you like to do next? (enter a command): ")
        
    elif choice=='7':
        print("\n--Write dictionary--")
        fp=open("MSU_DB.txt","w")
        print(masterD,file=fp) #printing in MSU_DB.txt
        fp.close()
        print("\n--Master Dictionary written to 'MSU_DB.txt' successfully--")
        choice=input("\nWhat would you like to do next? (enter a command): ")
        
    else: #covers all commands that are not 1, 2, 3, 4, 5, 6, 7, or x
        print("\n--You entered an invalid command, please try again.--")
        choice=input("\nWhat would you like to do next? (enter a command): ")

print("\n--Program exited appropriately--\n") #we let the user know that we
                                              #shut down appropriately


    
   