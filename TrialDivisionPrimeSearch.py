# -*- coding: utf-8 -*-
"""
Trial Division Prime Search

@author: Aaron
"""
from math import sqrt
def CheckPrimality(x,y):
    i = 0
    while x[i] <= int(sqrt(y)):
        if y % x[i] == 0:
            return False
        i += 1
    return True

def FindPrimesUnder(maxNum): # use this function to find all primes under n
    primes = [2]
    for i in range(3,maxNum,2):
        if CheckPrimality(primes, i) == True:
            primes.append(i)
    return primes

def FindNPrimes(n): # Use this function to find n number of primes
    primes = [2]
    i = 3
    while len(primes) < n:
        if CheckPrimality(primes, i) == True:
            primes.append(i)
        i += 1
    return primes