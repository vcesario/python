'''
	[nextsubset.py]
	This function takes two lists as parameters, where the first one is a subset of the second one.
	It then calculates the next subset of the same length within the given set.
	E.g.: in the superset [1, 2, 3, 4, 5, 6]
		- the first subset of size 3 is [1, 2, 3]
		- the last subset of size 3 is [4, 5, 6]

	author: github.com/vcesario
'''

def nextSubset(subset, superset):
	size = len(subset);
	SIZE = len(superset);
	k = size - 1;
	trail = SIZE - 1;

	while k >= 0:
		pos = superset.index(subset[k]);
		if pos < trail:
			break;
		k = k - 1;
		trail = trail - 1;
	
	if k >= 0:
		while k < size:
			pos = pos + 1;
			subset[k] = superset[pos];
			k = k + 1;
		return subset;
	
	return None;		

superset = [1, 2, 3, 4, 5, 6];

subset = [1, 2, 6];
nxt = nextSubset(subset, superset);
assert(nxt == [1, 3, 4]); #True

subset = [4, 5, 6];
nxt = nextSubset(subset, superset);
assert(nxt == None); #True