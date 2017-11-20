import math
import string
import random
import binascii
from Crypto.Util import number

def GenerateRNSBase(numbits, numbasis):
	primenums = []
	for n in range(numbasis):
		primenum = number.getPrime(numbits)
		while primenum in primenums:
			primenum = number.getPrime(numbits)
		primenums.append(primenum)
	return primenums

def maxbits(base, numbits, method="blocks"):
	""" returns the max value that can be stored in the rns """
	if (method == "mod"):
		result = 1
		for b in base:
			result *= b
		return math.floor(math.log(result, 2))
	else:
		return (numbits - 1) * len(base)

def ConvertIntToRNS(number, base, numbits, method="blocks"):
	""" return rns representation of an int """
	if method == "mod":
		result = []
		for b in base:
			result.append(number % b)

	else: # method == "blocks"
		# get str
		binstr = str(bin(number))[2:]
		padlen = 8 - (len(binstr) % 8)
		if (padlen == 8):
			padlen = 0
		for i in range(padlen):
			binstr = "0" + binstr

		# check length
		strlen = len(binstr)
		if strlen > maxbits(base, numbits, method):
			raise ValueError("Integer exceeds max rns integer")

		# padd to length
		padlen = maxbits(base, numbits, method) - strlen
		pad = "0" * int(padlen)
		binstr += pad


		result = []
		for i in range(len(base)):
			valstr = binstr[(numbits - 1)*i : (numbits - 1)*(i+1)]
			result.append(long(valstr, 2))
	
	return result

def ConvertMessageToRNS(msg, base, numbits, method="blocks"):
	if method == "blocks":
		hexmsg = msg.encode("hex")
		decmsg = int(hexmsg, 16)
		return ConvertIntToRNS(decmsg, base, numbits, method)

def ConvertRNSToMessage(rns, base, method="blocks"):
	if method == "blocks":
		# convert each element to binary of the appropriate length
		bits_rns = ""
		for i in range(len(rns)):
			number = rns[i]

			b = str(bin(base[i]))[2:]

			binary = str(bin(number))[2:]
			delta_zeros = 8 - (len(binary) % 8) - 1
			if (delta_zeros == 8):
				delta_zeros = 0

			# concatenate the binary
			for j in range(delta_zeros):
				bits_rns += '0'
			bits_rns += binary

		# convert binary to message
		bits2 = "0b" + bits_rns
		padlen = 8 - (len(bits_rns) % 8)
		if (padlen == 8):
			padlen = 0
		for i in range(padlen):
			bits2 += "0"

		binmsg = int(bits2, 2)
		Md = binascii.unhexlify('%x' % binmsg)

		if (Md[-1].encode("hex") == "00"):
			Md = Md[0:-1]
		return Md

def GetRandomIntMessage(n):
	return random.getrandbits(n)

def GetRandomMessage(n):
	size = n / 8
	chars=string.ascii_uppercase + string.digits
	return ''.join(random.choice(chars) for _ in range(size))


def main():

	numbits = 2**6
	method = "blocks"
	numbasis = 2
	print "numbits:", numbits
	print "method:", method
	print "numbasis:", numbasis

	M = GetRandomMessage(2*numbits - 1)
	base = GenerateRNSBase(numbits, numbasis)
	M_rns = ConvertMessageToRNS(M, base, numbits)
	print "M: ", M
	print "base:", base
	print "M_rns:", M_rns

	Md = ConvertRNSToMessage(M_rns, base)

	print "Md:", Md
	print "M == Md:", M == Md

if __name__ == '__main__':
	main()