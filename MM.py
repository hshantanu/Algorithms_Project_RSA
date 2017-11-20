from BasicRSA import inv as modInverse;

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

def bits(N):
    POW = 1;
    N -= 1;
    temp = N;
    while temp > 0:
        temp = N >> POW;
        POW += 1;
    return POW;
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
    #mFactor = 100;
    mFactor = findMFactor(N);
    return MMultiplicationF(x, y, N, mFactor);
###End of function

def MMultiplicationF(x, y, N, mFactor):

    #xBar = MReductionF(x, N, mFactor);
    #yBar = MReductionF(y, N, mFactor);

    mfBar = modInverse(mFactor, N);
    #numBar = xBar * yBar * mfBar;
    numBar = x * y * mFactor;
    resBar = numBar % N;

    return (resBar*mfBar) % N;

###End of function


#to multiply two numbers in montogomery domain
def ReverseMMultiplication(a, b, N, rBar):
    return (a*b*rBar)%N;
###End of function


def ModularExponentiation(x, e, N):

    X = x % N;
    E = e;
    R = 1;

    while E > 0:

        if E%2 == 0:
            X = (X*X) % N;
            E /= 2;
        else:
            R = (X*R) % N
            E -= 1;

    ###End Of Loop

    return R%N;

###End of function


def MontogomeryExponentiation(x, e, N):

    mFactor = findMFactor(N);
    X = x % N;
    E = e;
    R = 1;

    while E > 0:

        if E%2 == 0:
            X = MMultiplicationF(X, X, N, mFactor);
            E /= 2;
        else:
            R = MMultiplicationF(X, R, N, mFactor);
            E -= 1;
    ###End Of Loop

    return R%N;

###End of function



if __name__ == "__main__":
    import sys;
    if len(sys.argv) > 2:
        print MontogomeryExponentiation(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]));
    else:
        M = 6936;
        e = 65537;
        N = 2707015397;
        d = 1316468333

        #print ModularExponentiation(M, e, N);
        c = MontogomeryExponentiation(M, e, N);
        print c;
        print MontogomeryExponentiation(c, d, N);

        #		from lib.Langui import generateLargePrime;
        #		x = generateLargePrime(128);
        #		e = generateLargePrime(128);
        #		n = generateLargePrime(64);
        #		print "x="+ str(x) +" | e="+ str(e) +" | n="+ str(n);
        #		print MExponentiation(x, e, n);