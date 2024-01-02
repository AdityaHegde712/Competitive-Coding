#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def xor(arr):
    result = 0
    for i in arr:
        result = result ^ i
    return result


def sansaXor(arr):
    # First we make all possible sub lists of the given list
    # Then we XOR all the elements of the sub lists
    # Then we XOR all the XORs of the sub lists
    # This gives us the answer
    list_of_sublists = []
    for set_len in range(len(arr)):
        for j in range(len(arr)-set_len):
            list_of_sublists.append(arr[j:j+set_len+1])
    
    result = []
    for item in list_of_sublists:
        result.append(xor(item))
    
    return xor(result)


    

if __name__ == '__main__':
    # t = int(input().strip())
    t = 1

    for t_itr in range(t):
        # n = int(input().strip())
        n = 4

        # arr = list(map(int, input().rstrip().split()))
        arr = [4,5,7,5]

        result = sansaXor(arr)

        print(str(result) + '\n')
