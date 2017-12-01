import RNS
import MM
import time
import math

def ParallelRSATrial(e, n, M, numProcessors, numbits):
	B = RNS.GenerateRNSBase((numbits/numProcessors + 1), numProcessors)

	# assume RNS base already available prior to encryption
	time1 = time.time()
	Mrns = RNS.ConvertMessageToRNS(M, B, numbits)
	Mrns_d = []

	time1 = time.time() - time1
	time2 = 0

	for i in range(len(B)):
		m = Mrns[i]
		b = B[i]
		start = time.time()
		c = MM.MontogomeryExponentiation(m, e, n)
		stop = time.time()
		time2 = max(time2, stop - start)

	print (time1 ," ", time2)
	return time1+time2

def bitlength(n):
	binstr = str(bin(n))[2:]
	l = len(binstr)
	return l

def main():
	import BasicRSA
	import RNS
	numbits = 16
	numProcessors = 2
	n = BasicRSA.generateRSAParameters(numbits)
	# print val_list
	print "n:", n
	e = 1000

	method = "blocks"
	numbasis = 2
	print "numbits:", numbits
	print "method:", method
	print "numbasis:", numbasis

	rns = RNS.ResidueNumberSystem()
	M = rns.GetRandomMessage(2*numbits - 1)
	print "M: ", M

	# PRSA = ParallelRSA()
	time = ParallelRSATrial(e, n, M, numProcessors, numbits)
	
	print "time:", time

if __name__ == '__main__':
	main()

