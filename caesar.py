import sys
from lib.vars import alphabet

if( len(sys.argv) >= 4 ):
    in_key = int(sys.argv[1])
    in_txt = sys.argv[2]
    in_alphabet = sys.argv[3]
else:
    print("file.py {int KEY} {string TXT} {string ALPHABET_TYPE}")
    exit()

alen = len(alphabet[in_alphabet])

txt_list = list(in_txt)
decryp_list = [""] * len(in_txt)

for char in txt_list:
    index = alphabet[in_alphabet].index(char)
    
    index = index + in_key # shift the alphabet
    while( index >= alen ): #cycle through the alphabet 
        diff = (index + in_key) - (alen - 1)
        index = 0 + diff # a bit spaghetti but who doesn't like spaghetti

    decryp_list[txt_list.index(char)] = alphabet[in_alphabet][index]

print(decryp_list)
