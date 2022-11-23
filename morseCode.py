import sys

morseCode = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....',
              'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.',
              'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
              'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',
              '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....',
              '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-',
              '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}

def decrypt(morse_code):
    
    english = ""
    morse = ""
    morse_counter = len(morse_code)
    j = 0
    for i in morse_code:
        j += 1
        
        if j == morse_counter:
            english += list(morseCode.keys())[list(morseCode.values()).index(morse)]

        if(i != " "):
            counter = 0
            morse += i
            
        else:
            counter += 1
            
            if(counter == 2):
                english += " "
                
            else:
                english += list(morseCode.keys())[list(morseCode.values()).index(morse)]
                morse = ''
                
    return english         

for line in sys.stdin:
    print(decrypt(line))
