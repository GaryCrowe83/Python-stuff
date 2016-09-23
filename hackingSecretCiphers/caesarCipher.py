import sys
def main():

    """This code is a modified version of the Caesar Cipher found Hacking Secret Ciphers by Al Sweigart.
    The code is basically the same but with  added features such as:
    1. The ability to choose which 'mode' you want through user input.
    2. The ability to choose the 'message' value through user input.
    3. The ability to choose the 'key' value through user input.
    4. The ability to choose the alphabet.
    5. The program enters an infinite loop where it keeps asking the user to input the 
       correct input if the wrong input is inputed for the value alphabet.
    6. The program ends if the chosen mode does not exist.
    """
    
    # this stores your message 
    message = input("Please enter your message: ")
    # this puts your message through the cipher and returns a translated string
    translated = cipher(message)
    # this outputs the translated string and concatenates it with a '|' character
    # in case there are spaces at the end of the translated string   
    print(translated + "|")    
def chooseAlphabet(L):
    # This allows you to choose which alphabet you want to use for encryption/decryption.
    # The brute force technique relies on the hacker knowing what alphabet is being used. This would
    # be harder to do if the sender could which alphabets whenever they wanted to. 
    b1 = False
    
    while b1 == False:
        alphabet = input("Please select your alphabet- \n(1)standard \n(2)extended(letters and numbers) \n(3)extended  \n(4)custom: ")
        alphabet = int(alphabet)
            
        if alphabet >= 1 or alphabet <= 4:
            if(alphabet == 1):
                L = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
                break
    
            elif(alphabet == 2):
                L= "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
                break
                    
            elif(alphabet == 3):
                L="0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz[]{}'@#~/?.>,<|!%^&*()-_=+ "
                break
                
            elif(alphabet == 4):
                L = "0[1]2{3}4/5?<6>7|8@9'A#aB~bC+cD-dE=eF_fG!gH$hI%iJ^jK&kL*lM(mN)nO,oP.pQ;qR:rSsTtUuVvWwXxYyZz "
                break
            
            else:
                print("Input is invalid. Please try again.")         
        
    return L          
def chooseMode():
    # Choose whether to encrypt or decrypt
    mode = input("Please choose a mode (e)ncrypt or (d)ecrypt: ")
    
    # If "encrypt" or "decrypt" is not entered the program terminates early.
    if mode == "e":
        mode = "encrypt"
    
    elif mode == "d":
        mode = "decrypt"    
    
    else:    
        print("The mode you have chosen does not exist. You are out of attempts. Quitting...")
        sys.exit()
    
    return mode
def chooseKey():
    key = input("Please choose a key: ")
    key = int(key)
    return key     
def cipher(message):
    mode = chooseMode()
    L = ""
    LETTERS = chooseAlphabet(L)
    keyOptions = len(LETTERS) - 1
    print("You have %d possible keys" %keyOptions)
    key = chooseKey()
    
    # An empty String to store the translated string
    translated = ''

    # This part checks if there is a value in message that is also in LETTERS
    # if so then one of two operations will execute depending on which mode is chosen
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
        
            # If encrypt is chosen then the key will be added to the index reference number of the symbol
            # then that symbol will be replaced with whatever letter the new index reference is for
            if mode == "encrypt":
                num = num + key
        
        
            # If decrypt is chosen then then the key will be taken away from the index reference number
            # then that symbol will be replaced with the symbol the new index reference is for 
            elif mode == "decrypt":
                num = num - key
        
            # This is to handle if num is greater than len(LETTERS) or 0
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)
            
            translated = translated + LETTERS[num]
        
        else:
            translated = translated + symbol
            
    return translated    
if __name__  == "__main__":
    main()                                             