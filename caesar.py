from lib.input import *
from lib.vars import alphabet
from lib.vars import listToString

if( inputHasKeys(["-k", "-i", "-a"]) ):
    in_key = int(getValueOfKey("-k"))
    in_txt = getValueOfKey("-i")
    in_alphabet = getValueOfKey("-a")
else:
    print("file.py -k {int KEY} -i {string TXT} -a {string ALPHABET_TYPE}")
    exit()

alen = len(alphabet[in_alphabet])

txt_list = list(in_txt)
decryp_list = [""] * len(in_txt)

for char in txt_list:
    index = alphabet[in_alphabet].index(char)
    print("Decrypting char-index: " + str(txt_list.index(char)) + " (" + char + ")")

    index = index + in_key # shift the alphabet
    while( index >= alen ): #cycle through the alphabet 
        diff = (index + in_key) - (alen - 1)
        index = 0 + diff # a bit spaghetti but who doesn't like spaghetti

    decryp_list[txt_list.index(char)] = alphabet[in_alphabet][index]

print( "Output: " + listToString(decryp_list) )
