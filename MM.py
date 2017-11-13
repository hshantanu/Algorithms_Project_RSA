from lib.MI import *
import math

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

    #	xBar = MReductionF(x, N, mFactor);
    #	yBar = MReductionF(y, N, mFactor);

    mfBar = modInverse(mFactor, N);
    #	numBar = xBar * yBar * mfBar;
    numBar = x * y * mFactor;
    resBar = numBar % N;

    return (resBar*mfBar) % N;

###End of function


#to multiply two numbers in montogomery domain
def ReverseMMultiplication(a, b, N, rBar):
    return (a*b*rBar)%N;
###End of function



# as much as i can understand, this algorithm was defined in the RNS paper we read,
# NOT WORKING :(
def PaperBased_MExponentiation_notWorking(x, e, N):
    mFactor = findMFactor(N);
    mfBar = mFactor % N;
    xBar = MReductionF(x, N, mFactor);
    temp = mfBar;

    count = bits(e) - 1;

    while count >= 0:

        temp = MMultiplicationF(temp, temp, N, mFactor);

        if count == 0:
            temp = MMultiplicationF(temp, xBar, N, mFactor);

        count -= 1;
    ###End Of Loop

    ans = modInverse(temp, N);
    return ans;

###End of function


# Initially finds all power in the form "(x^2i) % N" using modulo exponentiation
# then mutiplies the power results to create "(x^e) % N" using montgomery multiplication
# WORKS FINE
def ModuloExponentiation(x, e, N):

    mFactor = findMFactor(N);

    res = [];
    count = 1;
    tempExp = x % N;
    res.append([count, tempExp]);

    while count < e:
        count *= 2;
        tempExp *= tempExp;
        tempExp = tempExp % N;
        res.append([count, tempExp]);

    if count == e:
        return tempExp;
    else:
        ans = [];
        count = e;
        size = len(res) - 1;

        for i in range(size, -1, -1):
            temp = res[i];
            if count>0 and count>=temp[0]:
                count -= temp[0];
                ans.append(temp[1]);

        size = len(ans);

        if size == 2:
            return MMultiplicationF(ans[0], ans[1], N, mFactor);
        else:
            temp = MMultiplicationF(ans[0], ans[1], N, mFactor);
            for i in xrange(2, size):
                temp = MMultiplicationF(temp, ans[i], N, mFactor);
            return temp;

###End of function


### IMPLEMENTED AS PER MY UNDERSTANDING
# first converts 'x' to montgomery domain, using 'mFactor', named as xBar
# then finds all power in the form "(xBar^2i) % N" using montogomery and modulo exponentiation
# then mutiplies the power results to create "(x^e) % N" using montgomery mutiplication
# WORKS FINE :)
def MExponentiation(x, e, N):

    mFactor = findMFactor(N);
    mfBar = modInverse(mFactor, N);

    print str(mFactor) +"   "+ str(mfBar);

    res = [];
    count = 1;
    tempExp = MReductionF(x, N, mFactor);               #PS: xBar = tempExp
    res.append([count, x]);

    while count < e:
        count *= 2;
        tempExp *= tempExp;
        tempExp = MReverse(tempExp, N, mfBar);
        res.append([count, tempExp]);

    if count == e:
        return MReverse(tempExp, N, mfBar);
    else:
        ans = [];
        count = e;
        size = len(res) - 1;

        for i in range(size, -1, -1):
            temp = res[i];
            if count>0 and count>=temp[0]:
                count -= temp[0];
                ans.append(temp[1]);

        size = len(ans);

        if size == 2:
            return ReverseMMultiplication(ans[0], ans[1], N, mfBar);
        else:
            temp = ReverseMMultiplication(ans[0], ans[1], N, mfBar);
            for i in xrange(2, size):
                temp = ReverseMMultiplication(temp, ans[i], N, mfBar);
            return temp;

###End of function



if __name__ == "__main__":
    import sys;
    if len(sys.argv) > 2:
        print MExponentiation(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]));
    else:
        #print MMultiplication(43, 56, 97);
        print MExponentiation(43, 57, 97);
        print ModuloExponentiation(43, 57, 97);

        #		from lib.Langui import generateLargePrime;
        #		x = generateLargePrime(128);
        #		e = generateLargePrime(128);
        #		n = generateLargePrime(64);
        #		print "x="+ str(x) +" | e="+ str(e) +" | n="+ str(n);
        #		print MExponentiation(x, e, n);