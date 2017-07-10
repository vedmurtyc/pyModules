# implement the below searching techniques
# 1. Linear search in a list
# 2. Binary Search in a sorted list.
# 3. Search for an element in a Binary tree
# 4. Search for an element in a Graph
import pdb

def linearSearch(elements, value):
	for i,e in enumerate(elements):
		if (e == value):
			return i
	return -1

def binarySearch(elements, value):
	return _binarySearch(elements, value, 0, len(elements))

def _binarySearch(elements, value, start, end):
	if start > end:
		return -1;
	mid = (start + end )//2
	if (value == elements[mid]):
		return mid
	elif(value < elements[mid]):
		return _binarySearch(elements, value, start, mid - 1)
	else:
		return _binarySearch(elements, value, mid + 1, end)

