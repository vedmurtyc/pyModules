# implement the below searching techniques
# 1. Linear search in a list
# 2. Binary Search in a sorted list.
# 3. Search for an element in a Binary tree
# 4. Search for an element in a Graph

def linearSearch(elements, value):
	for i,e in enumerate(elements):
		if (e == value):
			return i
	return -1

def binarySearch(elements, value, start, end):
	mid = (start + end )//2
	if (value == elements[mid]):
		return mid
	elif(start < end):
		binarySearch(elements[:mid], value, start, mid)
		binarySearch(elements[mid+1:], value, mid+1, end)
	else:
		return -1