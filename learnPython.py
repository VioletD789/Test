#page 30, Q1
#propagate the rightmoght 0's with 1's 
def prop_rightmost_1(x):
	print(bin(x))
	print(bin(x|(x-1)))
	return x|(x-1)


#page 30
def swap_bits(x,i,j):
	#print(bin(x))
	a_shift = x>>i
	b_shift = x>>j
	if a_shift&1 != b_shift&1:
		i_shift = 1<<i
		j_shift = 1<<j
		combine = i_shift^j_shift
		#print(bin(x^combine))
		return x^combine
	else:
		return x

print(reversed(range(4)))
