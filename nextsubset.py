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

subset = [1, 2, 6];
superset = [1, 2, 3, 4, 5, 6];
print('after ' + str(subset) + ' comes ' + str(nextSubset(subset, superset)));