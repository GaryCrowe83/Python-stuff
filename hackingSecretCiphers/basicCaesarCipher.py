message = input("Please enter your message: ")
meesage = message.upper()
LETTERS = "ABCDEFGHIJKLMNOGQRSTUVWZYZ"
translated = ""
key = input("Please choose a key(1 - 25): ")
key = int(key)
mode = input("Please choose (e)ncrypt or (d)ecrypt mode: ")

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        
        if mode == "e":
            num = num + key
                
        elif mode == "d":
            num = num - key
            
        if num >= len(LETTERS):
            num = num - len(LETTERS)
            
        elif num < 0:
            num = num + len(LETTERS)
            
        translated = translated + LETTERS[num]
        
    else:
        translated = translated + symbol                         
                
    
print(translated)        