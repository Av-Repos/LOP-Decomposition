import sys
import os
import numpy as np

# Function that decomposes a LOP instance into the (n-1,1) and (n-2,1,1) components according to the Fourier transform
def decompose(b_matrix,n):

	######## (n-1,1) component ########

	b_matrix_ = b_matrix.copy()
	b_matrix_[np.diag_indices(n)] = 0
	
	row_sum = b_matrix_.sum(axis=1, keepdims=True)  # shape: [n, 1]
	col_sum = b_matrix_.sum(axis=0, keepdims=True)  # shape: [1, n]
	
	p_matrix = ((n-1)*row_sum+(n-1)*col_sum+row_sum.T+col_sum.T)/(n*(n-2))
	
	p_matrix[np.diag_indices(n)] = 0

	######## (n-2,1,1) component ########
	
	h_matrix = b_matrix-p_matrix

	return p_matrix, h_matrix
