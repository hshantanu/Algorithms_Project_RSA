# Reference: https://jhafranco.com/2012/01/29/rsa-implementation-in-python/

from functools import reduce
from Crypto.Util import number
import sys
from time import time
import RNS
import random

def getPrime(numBits):
    primeNum = number.getPrime(numBits)
    return primeNum

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

    exp = exp_by_squaring(decmsg, 100000)
    return exp % n
    # # Return length (in bytes) of modulus
    # size = len("{:02x}".format(n)) // 2
    # output = []
    # while M:
    #     nbytes = min(len(M), size - 1)
    #     # Converting text to integer
    #     int_text = reduce(lambda x, y: (x << 8) + y, map(ord, M[:nbytes]))
    #     assert int_text < n
    #     power = pow(int_text, e, n)
    #     # Converting an integer to a list of small integers
    #     output += [(power >> j) & 0xff for j in reversed(range(0, (size + 2) << 3, 8))]
    #     M = M[size:]
    # return output

def decrypt(CT, d, p, q, n):
    exp = exp_by_squaring(CT, 100000)
    return exp % n

    # # Decryption using Chinese Remainder Theorem
    # size = len("{:02x}".format(n)) // 2
    # output = ""
    # while CT:
    #     # Convert a list of integers into an integer
    #     integer = reduce(lambda x, y: (x << 8) + y, CT[:size + 2])
    #     assert integer < n
    #     m1 = pow(integer, d % (p - 1), p)
    #     m2 = pow(integer, d % (q - 1), q)
    #     h = (inv(q, p) * (m1 - m2)) % p
    #     res = m2 + h * q
    #     # Convert an integer into a text string
    #     text = "".join([chr((res >> j) & 0xff) for j in reversed(range(0, size << 3, 8))])
    #     output += text.lstrip("\x00")
    #     CT = CT[size + 2:]
    # return output

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

    for bits in [8, 16, 32, 64, 128]:
        #t1 = time()
        n = generateRSAParameters(bits)  # p,q,n,e,d
        e = 1000

        M = RNS.GetRandomMessage(bits)
        print bits
        print "Regular: ", regularRSATrial(M, e, n)

        ptime = ParallelRSATrial.ParallelRSATrial(e, n, M, numProcessors, bits)
        print "Parallel:", ptime
