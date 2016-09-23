import sys, math
def main():
    Cipher()
def Cipher():
    boole1 = True
    boole2 = True
    
    while(boole1 == True):
        message = input("Please enter a message:\n")
        op = input("Please select an operation: \n(e)ncrypt  (d)ecrypt\n(ex)it\n")
        
        if(op == 'e' or op == 'encrypt'):
            print(encrypt(message))
        elif(op == 'd' or op == 'decrypt'):
            print(decrypt(message))
        elif(op == 'ex' or op == 'exit'):
            print("Closing Program........Goodbye")
            sys.exit()
        else:
            print("Invalid input please try again.")
        
        while(boole2 == True):    
            response = input("Do you wish to (C)ontinue or (Q)uit?\n")
            response.lower()
            if(response == 'c' or response == 'continue'):
                boole2 = False
            if(response == 'q' or response == 'quit'):
                print("Closing Program........Goodbye")
                sys.exit()                
def encrypt(message):
    letters = "0[1]2{3}4/5?<6>7|8@9'A#aB~bC+cD-dE=eF_fG!gH$hI%iJ^jK&kL*lM(mN)nO,oP.pQ;qR:rSsTtUuVvWwXxYyZz "
    translated = ""
    p = 48611
    q = 53993
    n = 17
     
    for i in range(len(message)):
        x = letters.index(message[i])
        x = x%n
        x = int(x)
        x = str(x)
        translated = translated + x + " "
    return translated   

def decrypt(message):
    letters = "0[1]2{3}4/5?<6>7|8@9'A#aB~bC+cD-dE=eF_fG!gH$hI%iJ^jK&kL*lM(mN)nO,oP.pQ;qR:rSsTtUuVvWwXxYyZz "
    translated = ""
    p = 48611
    q = 53993
    n = 17
    
    l = message.split()
    for i in range(len(l)):
        for j in range(len(letters)):
            x = (j*n) + int(l[i])
            if()
            translated += letters[x]     
    return translated     
if __name__ == '__main__':
    main()   