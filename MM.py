from BasicRSA import inv as modInverse;
from time import time

#Assumed 64bit multiplication because of 64bit system architecture
ARCH=64;

#Base=2; Length is calculated
def findMFactor(N):
    POW = 1;
    N -= 1;
    while POW < ARCH:
        N |= N >> POW;
        POW *= 2;
    N += 1;
    return N;
###End of function


### R.R^-1 - N.N' = 1
# Finds N'
def modulusBar(N):
    R = findMFactor(N)
    RI = modInverse(R, N)
    return modulusBarF(N, R, RI)
###End of function

def modulusBarF(N, R, RI):
    temp = 1 + R*RI
    return temp/N
###End of function

def MReduction(x, N):
    mFactor = findMFactor(N);
    return MReductionF(x, N, mFactor);
###End of function

def MReductionF(x, N, MF):
    return (x*MF) % N;
###End of function

#to reverse back a number from montogomery domain
def MReverse(x, N, rBar):
    return (x*rBar) % N;
###End of function


def MMultiplication(x, y, N):

    mFactor = findMFactor(N)
    mfBar = modInverse(mFactor, N)

    xBar = MReductionF(x, N, mFactor)
    yBar = MReductionF(y, N, mFactor)

    a = MMultiplicationF(xBar, yBar, N, mFactor, mfBar)
    a = MReverse(a, N, mfBar)
    b = MMultiplicationOLD(x, y, N, mFactor, mfBar)
    #return [a, b];
    return a


###End of function


def MMultiplicationF(xBar, yBar, N, mFactor, mfBar):

    NB = modulusBarF(N, mFactor, mfBar)

    t = xBar * yBar
    u = t + ( ((t*NB) % mFactor)*N )
    u = u / mFactor

    if u >= N:
        return u-N
    else:
        return u

###End of function


def MMultiplicationOLD(x, y, N, mFactor, mfBar):

    numBar = x * y * mFactor;
    resBar = numBar % N;

    return (resBar*mfBar) % N;

###End of function


def getFactors(N):

    mFactor = findMFactor(N);
    mfBar = modInverse(mFactor, N);

    return [mFactor, mfBar];

###End of function


def MontogomeryExponentiation(x, e, N):

    mFactor = findMFactor(N);
    mfBar = modInverse(mFactor, N);

    return MontogomeryExponentiationI(x, e, N, mFactor, mfBar)

###End of function



def MontogomeryExponentiationI(x, e, N, mFactor, mfBar):

    X = MReductionF(x, N, mFactor);
    R = mFactor % N;
    E = e;

    while E > 0:

        if E%2 == 0:
            X = MMultiplicationF(X, X, N, mFactor, mfBar);
            E /= 2;
        else:
            R = MMultiplicationF(X, R, N, mFactor, mfBar);
            E -= 1;
    ###End Of Loop

    return MReductionF(R, N, mfBar)

###End of function


if __name__ == "__main__":
    import sys;
    if len(sys.argv) > 2:
        print MontogomeryExponentiation(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]));
    else:
        M = 436
        # N = 2707015397
        # d = 1316468333
        e = 13

        N = 437
        d = 61

        c = MontogomeryExponentiation(M, e, N)
        print c
        print MontogomeryExponentiation(c, d, N)
        #print MMultiplication(5, 6, N);