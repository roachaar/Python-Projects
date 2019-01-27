    ###########################################################
    #  Computer Project #3
    #
    #  Algorithm
    #    prompt for an integer
    #    input an integer
    #    loop while not end-of-data
    #       call function to count number of digits in integer
    #       output the number of digits
    #       prompt for an integer
    #       input an integer
    #    display closing message
    ###########################################################
letters = "abcdefghijklmnopqrstuvwxyz"
answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")
while answer.upper() != 'Q':
    if answer.upper() == "D":
        c_key = ''
        a_key = ''
        b_key = ''
        d_key = ''
        valid_word = False
        while valid_word == False:
            key_word = input("Please enter a string to encode: ")
            if key_word.isalpha() == True and len(key_word)<=26:
                valid_word = True
                for ch in key_word:
                    if ch not in c_key:
                        c_key += ch
                for i in letters:
                    if i not in c_key:
                        c_key += i
                for ch in c_key:
                    d_key += c_key[(5*c_key.find(ch)+8) % 26]
            else:
                print("Please enter a valid string of all letters with length <= 26")
        message = input("Enter a message: ")
        for ch in message:
            if ch.isalpha() == True:
                b_key += c_key[d_key.find(ch)]
            else:
                b_key += ch
        for ch in b_key:
            if ch.isalpha() == True:
                a_key += letters[c_key.find(ch)]
            else:
                a_key += ch
        print("Your message is decrypted as:", a_key)
        answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")                
        continue
    elif answer.upper() == "E":
        c_key = ''
        a_key = ''
        b_key = ''
        valid_word = False
        while valid_word == False:
            key_word = input("Please enter a string to encode: ")
            if key_word.isalpha() == True and len(key_word)<=26:
                valid_word = True
                for ch in key_word:
                    if ch not in c_key:
                        c_key += ch
                for i in letters:
                    if i not in c_key:
                        c_key += i
            else:
                print("Please enter a valid string of all letters with length <= 26")
        message = input("Enter a message: ")
        for ch in message:
            if ch.isalpha() == True:
                a_key += c_key[letters.find(ch)]
            else:
                a_key += ch
        for ch in a_key:
            if ch.isalpha() == True:
                b_key += c_key[(5*c_key.find(ch)+8) % 26]
            else:
                b_key += ch
        print("Your message is encrypted as:", b_key)
        answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")        
        continue
    elif answer.upper() == "Q":
        break
    else:
        print("PLease enter a valid command") 
        answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")
print("Program halted successfully")