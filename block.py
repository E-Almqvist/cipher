#!/usr/bin/env python

import math
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
    if(in_mode == 0):
        print("Encrypting block: " + str(blockL) )
        for i in range(blockSize):
            blockDe[i] = blockL[keyT[i]] # encrypting
    elif(in_mode == 1):
        print("Decrypting block: " + str(blockL) )
        for i in range(blockSize):
            blockDe[keyT[i]] = blockL[i] # decrypting

    return blockDe

def splitInput(inputL, n):
    print("Splitting input: " + str(n))
    out = []
    inputLen = len(inputL)
    x = inputLen / float(n)
    
    last = 0.0
    while last < inputLen:
        out.append( inputL[ int(last):int(last + x) ] )
        last += x

    return out

def getOutput(blocksL):
    out = ""
    for block in blocksL:
        out += listToString(block)

    return out

#
# Do the encrypting/decrypting stuff with the input
# 
TXT = list(in_txt)
KEY = keyToIntTuple(in_key) # define and make the key a tuple so that we can index it

amountBlocks = len(TXT) / blockSize
if( math.floor(amountBlocks) != math.ceil(amountBlocks) ):
    print("Error: Input didn't match key size.")
    print("amountBlocks: " + str(amountBlocks))
    exit()

Blocks = splitInput(TXT, amountBlocks)
BlocksDe = [None] * len(Blocks) 

count = -1
for block in Blocks:
    count += 1
    BlocksDe[count] = applyKeyToBlock(KEY, block)


### Finally print the output
print( getOutput(BlocksDe) )
