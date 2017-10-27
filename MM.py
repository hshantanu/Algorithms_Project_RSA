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


def MReduction(x, N):
	mFactor = findMFactor(N);
	return MReductionF(x, N, mFactor);
###End of function

def MReductionF(x, N, MF):
	return (x*MF) % N;
###End of function


def MMultiplication(x, y, N):
	#mFactor = 100;
	mFactor = findMFactor(N);
	return MMultiplicationF(x, y, N, mFactor);
###End of function

def MMultiplicationF(x, y, N, mFactor):
	
	xBar = MReductionF(x, N, mFactor);
	yBar = MReductionF(y, N, mFactor);

	mfBar = modInverse(mFactor, N);
	numBar = xBar * yBar * mfBar;
#	numBar = x * y * mFactor;
	resBar = numBar % N;

	return (resBar*mfBar) % N;

###End of function


def MExponentiation(x, e, N):
	
	mFactor = findMFactor(N);

	res = [];
	count = 1;
	tempExp = x;
	res.append([count, x]);

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


if __name__ == "__main__":
	import sys;
	if len(sys.argv) > 2:
		print MExponentiation(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]));
	else:
		#print MMultiplication(43, 56, 97);
		from lib.Langui import generateLargePrime;
		x = generateLargePrime(128);
		e = generateLargePrime(128);
		n = generateLargePrime(64);
		print "x="+ str(x) +" | e="+ str(e) +" | n="+ str(n);
		print MExponentiation(x, e, n);