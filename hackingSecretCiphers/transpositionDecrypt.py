import math, pyperclip

def main():
    myMessage = input("Please enter the message you want to decrypt: ")
    myKey = input("Please enter your Key: ")
    
    plaintext = decryptMessage(myKey,myMessage)
    
    # Print with a | after it in case there are spaces 
    # At the end of the decrypted message
    print(plaintext + "|")
    
    pyperclip.copy(plaintext)
    
def decryptMessage(key,message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First we need to calculate a few values.
    
    # The number of "columns" in our transposition grid: 
    numOfColumns = math.ceil(len(message)/key)
    # The number of "rows" in our grid will need 
    numOfRows = key
    # The number of "shaded" boxes in our last "column" of the grid  
    numOfShadedBoxes = (numOfColumns*numOfRows) - len(message)
    
    # Each string in palintext represents a "column" on the grid.  
    plaintext = [""] * numOfColumns
    
    # The col and row variables point to where in the grid the next
    # character in the encrypted message will go
    col = 0
    row = 0
    
    for symbol in message:
        plaintext[col] += symbol
        col += 1 # point to the next column
        
        # If there are no more columns OR we're at a shaded box, go back to
        # the first column  and next row
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
            
    return "".join(plaintext)

# If transpositionDecrypt.py is run (instead of as imported as a module) call)
# the main() function
if __name__== "__main__":
    main()        
        
    