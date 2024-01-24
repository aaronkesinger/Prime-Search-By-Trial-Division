# Trial Division Prime 

This is a python implementation finding prime numbers using [Trial Division](https://en.wikipedia.org/wiki/Trial_division). 

It gives the option to find <em>n</em> number of primes or all primes under a specified <em>n</em>

Sample Use
```python
primesUnderFifty = FindPrimesUnder(50)
findSixtyPrimes = FindNPrimes(60)

print('Primes Under 50: ', primesUnderFifty, '\n')
print('First 60 Prime Numbers: ', findSixtyPrimes)
print(len(findSixtyPrimes))


''' Output
Primes Under 50:  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47] 

First 60 Prime Numbers:  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281]
60
'''
```