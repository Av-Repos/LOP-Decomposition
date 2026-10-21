import sys
import os
import numpy as np
from utils.IO import *
from utils.decompose import *

print("######################## Fourier Transform-based instance decomposition of the LOP - By Xabier Benavides ########################")
print("###                                                                                                                           ###")
print("###       This program decomposes any given LOP instance into two sub-instances containing the first-order (p.dat) and the    ###")
print("###       the second-order information (h.dat) of the original problem. The decomposition is based on the Fourier Transform   ###")
print("###       of the objective function.                                                                                          ###")
print("###                                                                                                                           ###")
print("#################################################################################################################################")

print()

# Instance reading
while(True):

	infile = input("Enter path to LOP instance: ")

	print()
	print("Reading instance...")
	
	try:
		b_matrix, n = read_LOP(infile)
	except:
		print("An unexpected error has occurred while reading the instance, try again!")
		print()
		continue
	
	break
	
# Instance decomposition	
print("Decomposing instance...")
p_matrix, h_matrix = decompose(b_matrix,n)
print()

# Sub-instance saving
while(True):
	outfile = input("Enter folder in which to save the sub-instances: ")

	print()
	print("Saving sub-instances...")
	try:
		print_LOP(p_matrix,n,outfile+"/p.dat")
		print_LOP(h_matrix,n,outfile+"/h.dat")
	except:
		print("An unexpected error has occurred while saving the sub-instances, try again!")
		print()
		continue
		
	print("Done!")
	break
