#  We choose to use more arrays to do this, but we could also do it in place
def quicksort(sequence):
	length = len(sequence)
	if length <= 1: # Skip over sequences that have length of 1 or 0
		return sequence
	else:
		pivot = sequence.pop() # pivot is arbitrary, just use the end of the list

	itemsLower = []
	itemsGreater = []

	for item in sequence:
		if item > pivot:
			itemsGreater.append(item)
		else: 
			itemsLower.append(item)

	return quicksort(itemsLower) + [pivot] + quicksort(itemsGreater)


print(quicksort([5,1,7,8,9,6,4,2,8,4,2,3,9]))