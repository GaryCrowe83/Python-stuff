"""
This is a brute force hack. This means that the program is going to guess the encryption key by going through 
one guess at a time. So through sheer brute effort cracks the encryption. Hence the name.
This essentially works like the decryption part of the Caesar Cipher 
"""
message = input("Please enter the message you want decrypt ")
LETTERS = "0[1]2{3}4/5?<6>7|8@9'A#B~C+D-E=F_G!H$I%J^K&L*M(N)O,P.Q;R:S TUVWXYZ"

#This loops through  every possible key
for key in range(len(LETTERS)):
    #This stores the decrypted message
    translated = ''
    
    #The rest of the program is the same as the original Caesar program
    
    #run the decryption code on each symbol in the message
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) #get the number of the symbol
            num = num - key
            
            # handle the wrap-around if num is 26 or less than 0
            if num < 0:
                num = num + len(LETTERS)
            
            #add number's symbol at the end translated     
            translated = translated + LETTERS[num]
        
        else:
           
            #just add the symbol without decrypting
            translated = translated + symbol
    
    # display the current key being tested, along with its decryption
    print("Key #%d " %key + " " + translated)