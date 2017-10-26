import math

class ResidueNumberSystem(object):
	"""
	Holds the RNS base and performs operations on numbers
	"""

	def __init__(self, method="mod", base=0):
		""" Set the RNS base vector. All base elements must be coprime """
		if (method == "mod"):
			if (base == 0):
				self.base = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
			else:
				self.base = base
		elif (method == "blocks"):
			if (base == 0):
				self.base = self.get32bitbase();
			else:
				raise ValueError("Only use default blocks with method='blocks'")
		else:
			raise ValueError("method must be either 'mod' or 'blocks'")

		self.method = method
		self.maxintlen = math.log(self.maxint(), 2)

	def get32bitbase(self):
		""" returns a 31 bit base of size 10 """
		K = [5, 17, 65, 99, 107, 135, 153, 185, 209, 267]
		n = 32;
		base = []
		for k in K:
			base.append(pow(2,n) - k)
		return base


	def maxint(self):
		""" returns the max value that can be stored in the rns """
		if (self.method == "mod"):
			result = 1
			for b in self.base:
				result *= b
			return result - 1
		else:
			length = 0
			for b in self.base:
				length += math.floor(math.log(b, 2))
			result = pow(2,length)
			return result


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
			if strlen > self.maxintlen:
				raise ValueError("Integer exceeds max rns integer")

			# padd to length
			padlen = self.maxintlen - strlen
			pad = "0" * int(padlen)
			binstr += pad

			result = []
			for i in range(len(self.base)):
				valstr = binstr[31*i:31*(i+1)]
				result.append(int(valstr))
		
		return result

	def msg2rns(self, msg):
		if self.method == "blocks":
			hexmsg = msg.encode("hex")
			decmsg = int(hexmsg, 16)
			return self.int2rns(decmsg)



def main():
	rns = ResidueNumberSystem("blocks")
	print "base: ", rns.base
	print "max:", rns.maxint()
	
	M = "Hello World! How are you? Good man! :)"
	print "message(", M, ":", rns.msg2rns(M)

	# a = pow(2, 100) + pow(2, 200)
	# print "rns(", a, "):", rns.int2rns(a)



	# print "lg(max):", math.log(rns.maxint(), 2) # max is a 310 bit message
	# print "max msg length", math.log(rns.maxint(), 2)/8, "bytes"

	# rns = ResidueNumberSystem("mod")
	# print "base: ", rns.base

	# max = rns.maxint()
	# print "max: ", max

	# a = 23
	# A = rns.int2rns(23)
	# print "rns(", a, "): ", A


if __name__ == '__main__':
	main()