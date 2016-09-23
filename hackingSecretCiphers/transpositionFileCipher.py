import time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():
    inputFilename = input("Please enter a filename: " )
    # BE CAREFUL! If a file with the outputFilename name already exists.
    # this program program will overwrite that file.
    myKey = input("Please choose a key: ")
    myKey = int(myKey)
    myMode = input("Please enter a mode: ")
    outputFilename = "%s.%s.txt" %(inputFilename,myMode)
    
    #If the input file does not exist, then the program terminates early.
    if not os.path.exists(inputFilename):
        print("The file %s does not exist. Quitting...." %(inputFilename))
        sys.exit()
    
    # If the output file already exists, give the user a chance to quit
    if os.path.exists(outputFilename):
        print("This will overwrite the file %s. (C)ontinue or (Q)uit?" %(outputFilename))
        response = input("> ")
        if not response.lower().startswith("c"):
            sys.exit()
    
    # Read the message from the input file         
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()
    
    print("%sing..." %(myMode.title()))
    
    # Measure how long the encryption/decryption takes.
    startTime = time.time()
    if myMode == "encrypt":
        translated = transpositionEncrypt.encryptMessage(myKey,content)
    elif myMode == "decrypt":
        translated = transpositionDecrypt.decryptMessage(myKey, content)
        
    totalTime = round(time.time() - startTime, 2)
    print("%sion time: %s seconds" %(myMode.title(), totalTime))
    
    # write out the translated message to the output file 
    outputFileObj = open(outputFilename, "w")
    outputFileObj.write(translated)
    outputFileObj.close()
    
    print("Done %sing %s (%s character)." %(myMode, inputFilename, len(content)))
    print("%sed file is %s. " % (myMode.title(),outputFilename))

# If transpositionFileCipher.py is run (instead of as imported as a module) call)
# the main() function    
if __name__ == "__main__":
    main()         
        
               
    