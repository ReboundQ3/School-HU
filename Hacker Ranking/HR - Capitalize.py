#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.     

def solve(s):
    name = s.split(" ")
    result = ""
    for part in name:
        i = 0
        for letter in part:
            if i == 0:
                result += letter.upper()
            else:
                result += letter
            i += 1
            
        result += " "
    
    return result
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
