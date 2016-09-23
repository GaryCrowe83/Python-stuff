import pyperclip

def main():
    myMessage = input("Please enter the file you wish to encrypt: ")
    myMessage = myMessage.upper()
    myKey = input("Please enter the key you choose: ")
    myKey = int(myKey) 
    
    ciphertext = encryptMessage(myKey, myMessage)
    
    # Print with a | (called a "pipe" character) after it in case
    # there are spaces at the end of the encrypted message. 
    print(ciphertext + "|")
    
    pyperclip.copy(ciphertext)
    
def encryptMessage(key, message):
    #Each string in the ciphertext represents a column in the grid
    ciphertext = [""]*key
    
    #Loop through each column in ciphertext.
    for col in range(key):
        pointer = col
        
        #Keep looping until pointer goes past the length of the message.
        while pointer < len(message):
            # Place the character at pointer in message at the end of the
            # current column in the ciphertext
            ciphertext[col] += message[pointer]
            
            # mover pointer over 
            pointer += key
    
    # Convert the ciphertext list into a single into a single string value and return it        
    return "".join(ciphertext)

# If transpositionEncrypt.py is run (instead of as imported as a module) call)
# the main() function
if __name__ == "__main__":
    main()            