import rsa
import RNS
from time import time

#Always need to add 88
for bits in [128, 512]:

	rns = RNS.ResidueNumberSystem()
	M = rns.GetRandomMessage(bits - 88)
	M = M.encode('utf8')
	(pbk, prk) = rsa.newkeys(bits)
	#M = "T".encode('utf8')
	#print('-------------------pbk-----------------------', pbk)
	#print('-------------------prk-----------------------', prk)
	T1 = time()
	CT = rsa.encrypt(M, pbk)
	message = rsa.decrypt(CT, prk)
	T2 = time()
	print(message.decode('utf8'))
	print T2 - T1