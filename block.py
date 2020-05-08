from lib.input import *
from lib.vars import alphabet
from lib.vars import listToString

if( inputHasKeys(["-k", "-i", "-t"]) ):
    in_key = getValueOfKey("-k")
    in_txt = getValueOfKey("-i")
    in_mode = int(getValueOfKey("-t"))
    blockSize = len(in_key)
else:
    print("file.py -k {int KEY} -i {string TXT} -t {MODE}")
    print("-k: The encryption/decryption key")
    print("-i: The text to be encrypted/decrypted")
    print("-t: The mode (0=encrypt or 1=decrypt)")
    exit()

def keyToIntTuple(key):
    return tuple(map(int, list(key)))

def applyKeyToBlock(keyT, blockL): # function to apply a key to a block
    blockDe = [""] * blockSize

    for i in range(blockSize):
        blockDe[i] = blockL[keyT[i]] 
    
    print(blockDe)
    return blockDe

KEY = keyToIntTuple(in_key) # define and make the key a tuple so that we can index it

applyKeyToBlock(keyToIntTuple(in_key), list(in_txt))

 
