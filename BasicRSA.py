# Reference: https://jhafranco.com/2012/01/29/rsa-implementation-in-python/

import sys
from Crypto.Util import number
from time import time

import RNS


def getPrime(numBits):
    primeNum = number.getPrime(numBits)
    return primeNum

#O(log-q)
def inv(p, q):
    # Multiplicative inverse
    def xgcd(x, y):
        # Extended Euclidean Algorithm
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

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generateRSAParameters(bits):
    # Generate Public and Private Keys
    p = getPrime(bits)
    q = getPrime(bits)
    var = (p - 1) * (q - 1)
    n = p * q
    return n

def encrypt(M, e, n):
    hexmsg = M.encode("hex")
    decmsg = int(hexmsg, 16)

    exp = exp_by_squaring(decmsg, e)
    # exp = decmsg ** e
    return exp % n

def exp_by_squaring(x, n):
    if n < 0:
        return exp_by_squaring(1 / x, -n)
    elif n == 0:
        return  1
    elif n == 1:
        return  x
    elif n % 2 == 0:
        return exp_by_squaring(x * x,  n / 2);
    else:
        return x * exp_by_squaring(x * x, (n - 1) / 2);
def printCipher(CT):
    for index, elem in enumerate(CT):
        sys.stdout.write(str(elem))
    print ""

def regularRSATrial(M, e, n):
    t1 = time()
    encrypt(M, e, n)
    t2 = time()
    diff = t2 - t1
    return diff

if __name__ == '__main__':
    import ParallelRSATrial
    # PRSA = ParallelRSA()
    numProcessors = 4

    for bits in [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]:
        #t1 = time()
        n = generateRSAParameters(bits)  # p,q,n,e,d
        e = 1000

        M = RNS.GetRandomMessage(bits)
        print bits
        print "Regular: ", regularRSATrial(M, e, n)

        ptime = ParallelRSATrial.ParallelRSATrial(e, n, M, numProcessors, bits)
        print "Parallel:", ptime
