import time, os, sys, basicCaesarCipher

def main():
    inputFilename = input("Please enter a filename: ")
    myKey = input("Please choose a key: ")
    myMode = input("Please choose a mode: ")
    outputFilename = input("%s.%s.txt" %(inputFilename,myMode))
    
    if not os.path.exists(inputFilename):
        print("The file %s does not exist. Quitting......" %(inputFilename))
        sys.exit()
        
    if os.path.exists(outputFilename):
        print("This will overwrite the file %s. (C)ontinue or (Q)uit?" %(outputFilename))
        response = input("> ")
        if not response.lower().startswith("c"):
            sys.exit
    
    
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()
    
    print("%sing...." %myMode.title())
    
    startTime = time.time()
    if myMode == "e":
        translated = basicCaesarCipher(myKey, content)
        
    elif myMode == "d":
        translated = basicCaesarCipher(myKey, content)
        
    totalTime = round(time.time()- startTime, 2)
    print("%sion time: %s seconds " %(myMode.title, totalTime))
    
    outputFileObj = open(outputFilename, "w")
    outputFileObj.write(translated)
    outputFileObj.close()
    
    print("Done %sing %s (%s character)." %(myMode, inputFilename, len(content)))
    print("%sed file is %s. " % (myMode.title(),outputFilename))

# If transpositionFileCipher.py is run (instead of as imported as a module) call)
# the main() function    
if __name__ == "__main__":
    main()         
        
        