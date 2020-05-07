from lib.input import *
from lib.vars import alphabet
from lib.vars import listToString

if( inputHasKeys(["-k", "-i", "-a"]) ):
    in_key = int(getValueOfKey("-k"))
    in_txt = getValueOfKey("-i")
    in_alphabet = getValueOfKey("-a")
else:
    print("file.py -k {int KEY} -i {string TXT} -a {string ALPHABET_TYPE}")
    print("-k: The encryption/decryption key")
    print("-i: The text to be encrypted/decrypted")
    print("-a: The alphabet (SWE or ENG)")
    exit()

alen = len(alphabet[in_alphabet])

txt_list = list(in_txt)
decryp_list = [""] * len(in_txt)

charindex = -1
for char in txt_list: # loop through all of the chars 
    charindex = charindex + 1

    index = alphabet[in_alphabet].index(char)
    print("Decrypting char-index: " + str(charindex) + " (" + char + ")")

    index = index + in_key # shift the alphabet
    while( index > alen - 1 ): #cycle through the alphabet 
        index = (index + in_key) - (alen - 1)

    decryp_list[charindex] = alphabet[in_alphabet][index]

print( "Output: " + listToString(decryp_list) )
