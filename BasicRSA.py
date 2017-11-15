#Reference: https://jhafranco.com/2012/01/29/rsa-implementation-in-python/

from random import randrange, getrandbits
from itertools import repeat
from functools import reduce
from Crypto.Util import number
import sys

def getPrime(numBits):
    primeNum = number.getPrime(numBits)
    return primeNum

def inv(p, q):
    #Multiplicative inverse
    def xgcd(x, y):
        #Extended Euclidean Algorithm
        s1, s0 = 0, 1
        t1, t0 = 1, 0
        while y:
            q = x // y
            x, y = y, x % y
            s1, s0 = s0 - q * s1, s1
            t1, t0 = t0 - q * t1, t1
        return x, s0, t0      
 
    s, t = xgcd(p, q)[0:2]
    assert s == 1
    if t < 0:
        t += q
    return t

def generateRSAParameters(bits):
    #Generate Public and Private Keys
    #65537 is the largest known prime number of the form {\displaystyle 2^{2^{n}}+1} 2^{{2^{{n}}}}+1 ( {\displaystyle n=4} n=4).
    val_list = []
    p = getPrime(bits)
    q = getPrime(bits)
    var = (p - 1) * (q - 1)
    n =  p * q
    if n < 65537:
        e, d = 3, inv(3, var)
    else:
        e, d = 65537, inv(65537, var)
    val_list.append([p, q, n, e, d])
    return val_list

for bits in [64]:    
    val_list = generateRSAParameters(bits) #p,q,n,e,d