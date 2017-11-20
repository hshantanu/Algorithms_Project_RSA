import RNS
import MM
import time
import math

class ParallelRSA(object):
	"""
	Performs trials of RSA
	"""

	def ParallelRSATrial(self, p, q, n, e, d, M, numProcessors, numbits):
		time1 = time.time()
		rns = RNS.ResidueNumberSystem()
		B = rns.GenerateRNSBase(numbits, numProcessors)
		Mrns = rns.ConvertMessageToRNS(M, B, numbits)
		Mrns_d = []

		time1 = time.time() - time1

		time2 = 0

		for i in range(len(B)):
		# for m in Mrns:
			m = Mrns[i]
			b = B[i]
			start = time.time()
			print "m:", m
			c = MM.MontogomeryExponentiation(m, e, b)
			print "c:", c
			Mrns_d.append(MM.MontogomeryExponentiation(c, d, b))
			stop = time.time()
			time2 = max(time2, stop - start)

		print "Base:  ", B
		print "Mrns_d:", Mrns_d
		print "Mrns:  ", Mrns
		# TODO: This does not match up. Somethng about encryption/decryption isn't working here
		# Shouldn't these calls to MontExp() encode then decode m?
		# Since we're not using n, instead the RNS base, need to do something different...

		time3 = time.time()
		Md = rns.ConvertRNSToMessage(Mrns, B)
		while (Md[-1].encode("hex") == "00"):
			Md = Md[0:-1]
		time3 = time.time() - time3
		return [Md, time1+time2+time3]

	def bitlength(self, n):
		binstr = str(bin(n))[2:]
		l = len(binstr)
		# print "binstr:", binstr
		# print "len(binstr):", l
		return l

def main():
	import BasicRSA
	import RNS
	numbits = 16
	numProcessors = 2
	val_list = BasicRSA.generateRSAParameters(numbits)
	# print val_list
	p = val_list[0]
	q = val_list[1]
	n = val_list[2]
	e = val_list[3]
	d = val_list[4]
	print "p:", p
	print "q:", q
	print "n:", n
	print "e:", e
	print "d:", d

	method = "blocks"
	numbasis = 2
	print "numbits:", numbits
	print "method:", method
	print "numbasis:", numbasis

	rns = RNS.ResidueNumberSystem()
	M = rns.GetRandomMessage(2*numbits - 1)
	print "M: ", M

	PRSA = ParallelRSA()
	[Md, time] = PRSA.ParallelRSATrial(p, q, n, e, d, M, numProcessors, numbits)
	
	print "Md:", Md
	print "time:", time

	# p = 13
	# q = 11
	# n = 143
	# e = 2
	# d = 4
	# M = "hello"
	# numProcessors = 4
	# prsa = ParallelRSA();
	# [Md, t] = prsa.ParallelRSATrial(p, q, n, e, d, M, numProcessors)
	# print "M: ", M
	# print "Md:", Md

if __name__ == '__main__':
	main()

