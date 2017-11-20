import RNS
import MM
import time

class ParallelRSA(object):
	"""
	Performs trials of RSA
	"""

	def ParallelRSATrial(self, p, q, n, e, d, M, numProcessors):
		time1 = time.time()
		
		numbits = self.bitlength(n) / numProcessors - 1
		print "numbits:", numbits
		rns = RNS.ResidueNumberSystem()
		B = rns.GenerateRNSBase(numbits, numProcessors)
		Mrns = rns.ConvertMessageToRNS(M, B, numbits)
		Mrns_decrypted = []

		time1 = time.time() - time1
		time2 = 0

		for m in Mrns:
			start = time.time()
			c = MM.MontogomeryExponentiation(m, e, n)
			Mrns_decrypted.append(MM.MontogomeryExponentiation(c, d, n))
			stop = time.time()
			time2 = max(time2, stop - start)

		time3 = time.time()
		M_decrypted = rns.ConvertRNSToMessage(Mrns_decrypted, B)
		time3 = time.time() - time3
		return [M_decrypted, time1+time2+time3]

	def bitlength(self, n):
		binstr = str(bin(n))[2:]
		l = len(binstr)
		print "binstr:", binstr
		print "len(binstr):", l
		return l

def main():
	p = 13
	q = 11
	n = 143
	e = 2
	d = 4
	M = "hello"
	numProcessors = 4
	prsa = ParallelRSA();
	[Md, t] = prsa.ParallelRSATrial(p, q, n, e, d, M, numProcessors)
	print "M: ", M
	print "Md:", Md

if __name__ == '__main__':
	main()

