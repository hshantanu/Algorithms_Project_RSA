import RNS
import MM
import time
import math

class ParallelRSA(object):
	"""
	Performs trials of RSA
	"""

	def ParallelRSATrial(self, e, n, M, numProcessors, numbits):
		time1 = time.time()
		rns = RNS.ResidueNumberSystem()
		B = rns.GenerateRNSBase(numbits, numProcessors)
		Mrns = rns.ConvertMessageToRNS(M, B, numbits)
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

		return time1+time2

	def bitlength(self, n):
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

	PRSA = ParallelRSA()
	time = PRSA.ParallelRSATrial(e, n, M, numProcessors, numbits)
	
	print "time:", time

if __name__ == '__main__':
	main()

