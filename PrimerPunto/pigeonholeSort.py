# source code : https://www.geeksforgeeks.org/pigeonhole-sort/?ref=header_outind


# Python program to implement Pigeonhole Sort */

# source code : "https://en.wikibooks.org/wiki/
# Algorithm_Implementation/Sorting/Pigeonhole_sort"
def pigeonhole_sort(a):
	# size of range of values in the list 
	# (ie, number of pigeonholes we need)
	my_min = min(a)
	my_max = max(a)
	size = my_max - my_min + 1

	# our list of pigeonholes
	holes = [0] * size

	# Populate the pigeonholes.
	for x in a:
		assert type(x) is int, "integers only please"
		holes[x - my_min] += 1

	# Put the elements back into the array in order.
	i = 0
	for count in range(size):
		while holes[count] > 0:
			holes[count] -= 1
			a[i] = count + my_min
			i += 1
			
