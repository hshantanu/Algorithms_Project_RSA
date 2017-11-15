import math
import string
import random
from Crypto.Util import number

class ResidueNumberSystem(object):
	"""
	Holds the RNS base and performs operations on numbers
	"""

	# def __init__(self, method, numBits, numBasis):
	def __init__(self):
		""" Set the RNS base vector. All base elements must be coprime """
		# self.base = self.getBase(numBits, numBasis)
		# self.numBits = numBits
		# self.method = method

	def GenerateRNSBase(self, numbits, numbasis):
		primenums = []
		for n in range(numbasis):
			primenum = number.getPrime(numbits)
			while primenum in primenums:
				primenum = number.getPrime(numbits)
			primenums.append(primenum)
		return primenums

	def maxbits(self, base, numbits, method="blocks"):
		""" returns the max value that can be stored in the rns """
		if (method == "mod"):
			result = 1
			for b in base:
				result *= b
			return math.floor(math.log(result, 2))
		else:
			return (numbits - 1) * len(base)

	def ConvertIntToRNS(self, number, base, numbits, method="blocks"):
		""" return rns representation of an int """
		if method == "mod":
			result = []
			for b in base:
				result.append(number % b)

		else: # method == "blocks"
			# get str
			binstr = str(bin(number))[2:]

			# check length
			strlen = len(binstr)
			if strlen > self.maxbits(base, numbits, method):
				raise ValueError("Integer exceeds max rns integer")

			# padd to length
			padlen = self.maxbits(base, numbits, method) - strlen
			pad = "0" * int(padlen)
			binstr += pad


			result = []
			for i in range(len(base)):
				valstr = binstr[(numbits - 1)*i : (numbits - 1)*(i+1)]
				result.append(long(valstr, 2))
		
		return result

	def ConvertMessageToRNS(self, msg, base, numbits, method="blocks"):
		if method == "blocks":
			hexmsg = msg.encode("hex")
			decmsg = int(hexmsg, 16)
			return self.ConvertIntToRNS(decmsg, base, numbits, method)

	def GetRandomIntMessage(self, n):
		return random.getrandbits(n)

	def GetRandomMessage(self, n):
		size = n / 8
		chars=string.ascii_uppercase + string.digits
		return ''.join(random.choice(chars) for _ in range(size))


def main():
	numbits = 2**8
	method = "blocks"
	numbasis = 2;
	print "numbits:", numbits
	print "method:", method
	print "numbasis:", numbasis

	rns = ResidueNumberSystem()
	M = rns.GetRandomMessage(2*numbits - 1)
	base = rns.GenerateRNSBase(numbits, numbasis)
	M_rns = rns.ConvertMessageToRNS(M, base, numbits)

	print "M:", M
	print "base:", base
	print "M_rns:", M_rns

if __name__ == '__main__':
	main()