""""
The following Cipher takes in a string and encrypts each character with a square number based
on the position of that character in the alphabet. 
Note: The cipher below can't encrypt double quotes ("). Any double quotes won't be encrypted on won't appear
in the decrypted text. 
This is program is a template for more advanced mathematical ciphers.
In future the only things that need to be changed are the encryption and decryption functions.
The rest of the program acts as a simplistic user interface that can be used with any other cipher
in Python.
The specifics of how the program operates are detailed below.       
"""
import sys, math
def main():
    #All the main function does is call the cipher.
    #Everything else is handled in the functions below.
    Cipher()    
def square(message):
    #This is the encryption algorithm
    translated = "" #empty string to store encrypted message
    #String to store the alphabet in use
    letters = "0[1]2{3}4/5?<6>7|8@9'A#aB~bC+cD-dE=eF_fG!gH$hI%iJ^jK&kL*lM(mN)nO,oP.pQ;qR:rSsTtUuVvWwXxYyZz "
    
    for symbol in range(len(message)): #loops through the message to be encrypted
        if message[symbol] in letters: #if char in message is also in letters
            x = letters.index(message[symbol]) #get the index of the char in letters
            x = x*x #square it
            x = str(x) #converted it to a string
            translated = translated + x + " " #concatenate it with translated string
            
    return translated #return the encrypted message                  
def squareRoot(message):
    #This is the decryption algorithm 
    translated = "" #empty  string to store decrypted text
    letters = "0[1]2{3}4/5?<6>7|8@9'A#aB~bC+cD-dE=eF_fG!gH$hI%iJ^jK&kL*lM(mN)nO,oP.pQ;qR:rSsTtUuVvWwXxYyZz "
    #string the alphabet in use
    l = message.split() #splits encrypted string into a list
    for i in range(len(l)): #loop through list 
        l[i] = int(l[i]) # cast each str into an int 
        x = math.sqrt(l[i]) #find the square root of number
        x = int(x) #cast as int 
        translated += letters[x] #concatenate with translated string   
    return translated
def Cipher():
    #Sets up a boolean variables 
    boole = True
    boole2 = True 
    #Creates an infinite loop in order to create a user interface
    while(boole == True):
        #User chooses what kind of operation they want to carry out
        #User inputs 'e' for the encryption algorithm
        #User inputs 'd' for the decryption algorithm
        #User inputs 'ex' to exit the program
        #If the user inputs an invalid input it asks them to try again
        boole2 = True #set to True to access the inner loop below
        message = input("Please enter a message:\n")
        op = input("Please select an operation: \n(e)ncrypt  (d)ecrypt  \n(ex)it\n") #Takes in input 
        op = op.lower() #Changes input to lower case
        if(op == 'e' or op == 'encrypt'):  #if op is 'e' run encryption algorithm
                        #Note: the input for this is a string
            print(square(message)) #output the result
        elif(op == 'd' or op == 'decrypt'):#if op is 'd' run decryption algorithm
                        #Note: the input here must be a string of integers
            print(squareRoot(message)) #output the result
        elif(op == "ex" or op == 'exit'): #if user inputs 'ex' then the program ends
            print("Closing program........Goodbye")
            sys.exit()
        else:
            print("Invalid input. Please try again") #if none of the above try again
        
        while(boole2 == True):
            #This asks the user if the want to continue to use the program
            #The user inputs 'c' or 'C' to continue to program
            #The user inputs 'q' or 'Q' to exit the program    
            #If the user inputs an invalid input it asks them to try again
            response = input("Do you wish to (C)ontinue or (Q)uit?\n")
            response = response.lower() #set response to lower case
            if(response == 'c' or response == 'continue'): #If response is 'c' then pass and continue the loop 
                boole2 = False #set boole2 to false to exit the inner loop
            elif(response == 'q' or response == 'quit'): #If response is 'q' then exit the program
                print("Closing program........Goodbye")
                sys.exit()
            else:
                print("Invalid input. Please try again") #If response is invalid asks user to try again         
if __name__ == '__main__':
    main()    