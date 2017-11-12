import math
import random
from Crypto.Util import number

class ResidueNumberSystem(object):
	"""
	Holds the RNS base and performs operations on numbers
	"""

	def __init__(self, method, numBits, numBasis):
		""" Set the RNS base vector. All base elements must be coprime """
		self.base = self.getBase(numBits, numBasis)
		self.numBits = numBits
		self.method = method

	def getBase(self, numBits, numBasis):
		primeNums = []
		for n in range(numBasis):
			primeNum = number.getPrime(numBits)
			while primeNum in primeNums:
				primeNum = number.getPrime(numBits)
			primeNums.append(primeNum)
		return primeNums

	def maxbits(self):
		""" returns the max value that can be stored in the rns """
		if (self.method == "mod"):
			result = 1
			for b in self.base:
				result *= b
			return math.floor(math.log(result, 2))
		else:
			return (self.numBits - 1) * len(self.base)

	def int2rns(self, number):
		""" return rns representation of an int """
		if self.method == "mod":
			result = []
			for b in self.base:
				result.append(number % b)

		else: # method == "blocks"
			# get str
			binstr = str(bin(number))[2:]

			# check length
			strlen = len(binstr)
			if strlen > self.maxbits():
				raise ValueError("Integer exceeds max rns integer")

			# padd to length
			padlen = self.maxbits() - strlen
			pad = "0" * int(padlen)
			binstr += pad


			result = []
			for i in range(len(self.base)):
				valstr = binstr[(self.numBits - 1)*i : (self.numBits - 1)*(i+1)]
				result.append(long(valstr, 2))
		
		return result

	def msg2rns(self, msg):
		if self.method == "blocks":
			hexmsg = msg.encode("hex")
			decmsg = int(hexmsg, 16)
			return self.int2rns(decmsg)

	def randomMessage(self, n):
		return random.getrandbits(n)

def main():
	bits = 2**10
	print "bits:", bits
	rns = ResidueNumberSystem("blocks", bits, 1)
	print "Max message bits:", rns.maxbits()
	
	M = rns.randomMessage(bits - 1)

	# M = "Hello World! How are you? Good man! :)"
	print "MsgInt: ", M
	print "Base:  ", rns.base
	# print "Msg: ", rns.msg2rns(M)
	print "MsgRNS:", rns.int2rns(M)

if __name__ == '__main__':
	main()