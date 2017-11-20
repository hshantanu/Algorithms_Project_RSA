    # Reference: https://jhafranco.com/2012/01/29/rsa-implementation-in-python/

from functools import reduce
from Crypto.Util import number
import sys
from time import time


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


def generateRSAParameters(bits):
    # Generate Public and Private Keys
    # 65537 is the largest known prime number of the form {\displaystyle 2^{2^{n}}+1} 2^{{2^{{n}}}}+1 ( {\displaystyle n=4} n=4).
    p = getPrime(bits)
    q = getPrime(bits)
    var = (p - 1) * (q - 1)
    n = p * q
    if n < 65537:
        e, d = 3, inv(3, var)
    else:
        e, d = 65537, inv(65537, var)
    val_list = [p, q, n, e, d]
    return val_list


def encrypt(M, e, n):
    # Return length (in bytes) of modulus
    size = len("{:02x}".format(n)) // 2
    output = []
    while M:
        nbytes = min(len(M), size - 1)
        # Converting text to integer
        int_text = reduce(lambda x, y: (x << 8) + y, map(ord, M[:nbytes]))
        assert int_text < n
        power = pow(int_text, e, n)
        # Converting an integer to a list of small integers
        output += [(power >> j) & 0xff for j in reversed(range(0, (size + 2) << 3, 8))]
        M = M[size:]
    return output


def decrypt(CT, d, p, q, n):
    # Decryption using Chinese Remainder Theorem
    size = len("{:02x}".format(n)) // 2
    output = ""
    while CT:
        # Convert a list of integers into an integer
        integer = reduce(lambda x, y: (x << 8) + y, CT[:size + 2])
        assert integer < n
        m1 = pow(integer, d % (p - 1), p)
        m2 = pow(integer, d % (q - 1), q)
        h = (inv(q, p) * (m1 - m2)) % p
        res = m2 + h * q
        # Convert an integer into a text string
        text = "".join([chr((res >> j) & 0xff) for j in reversed(range(0, size << 3, 8))])
        output += text.lstrip("\x00")
        CT = CT[size + 2:]
    return output


def printCipher(CT):
    for index, elem in enumerate(CT):
        sys.stdout.write(str(elem))
    print ""


def regularRSATrial(M, val_list):
    # val_list = [p, q, n, e, d]
    t1 = time()
    p = val_list[0]
    q = val_list[1]
    n = val_list[2]
    e = val_list[3]
    d = val_list[4]
    CT = encrypt(M, e, n)
    #    print "Cipher Text: "
    #    printCipher(CT)
    DT = decrypt(CT, d, p, q, n)
    #    print "Decrypted Text: "
    #    print DT
    t2 = time()
    #    print "Time: {:0.10f} seconds".format((t2 - t1))
    diff = float("{0:.5f}".format((t2-t1)*1000))                #in milliseconds
    return [M==DT, diff ];



if __name__ == '__main__':
    for bits in [16, 32, 64, 128, 512]:
        val_list = generateRSAParameters(bits)  # p,q,n,e,d
        print regularRSATrial("this is a test message.", val_list)
