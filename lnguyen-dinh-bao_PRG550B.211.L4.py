# Your solution may ONLY use the python modules listed below
# program: L4main.py
# author:  danny abesdris
# date:    february 12, 2021
# purpose: python main( ) program for PRG550 Winter 2021 Lab #4

import math
import random
import string
import collections
import datetime
import re
import time
import copy

# YOUR CODE BELOW...

def writeVertical(n) :
    for charac in str(n):
        print(charac)
def digitalSum(n) :
    length = len(str(n))
    result =0
    if length > 0 :
        for i in str(n):
            result+= int(i)
            digitalSum(str(n)[0:length - 1])
        
    return result
def exponents(a, b) :
    if a == 0:
        return 0
    if b == 0:
        return 1 
    elif b>0:
        return a*exponents(a,b-1)
    elif b<0:
        return (exponents(a,b+1))/a
def invertedImage(top, bottom, n, s) :
    if n>=1:
        print(' '*s ,top*n)
    elif n<1:
        return
    invertedImage(top, bottom, n-1, s+1)
    print(' '*s ,bottom*n)

def main( ) :
   writeVertical(98312)
   print("===")
   writeVertical(0)
   print("===")
   writeVertical(-123456789)
   print("===")
   print(digitalSum(1234))
   print("===")
   print(exponents(3, -4))
   print("===")
   print(exponents(16, 0))
   print("===")
   print(exponents(0, 9))
   print("===")
   print(exponents(-18, 7))
   print("===")
   print(exponents(12, 12))
   print("===")
   invertedImage('*', '#', 6, 0)
   print("===")
   invertedImage('@', '^', 18, 0)
# end main( )

if __name__ == "__main__" :
   main( )
       

