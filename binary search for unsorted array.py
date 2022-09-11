# Python3 implementation to search an
# element in the unsorted array using
# minimum number of comparisons

# function to search an element in
# minimum number of comparisons
def search(arr, n, x):
	
	# 1st comparison
	if (arr[n-1] == x) :
		return "Found"

	backup = arr[n-1]
	arr[n-1] = x

	# no termination condition and
	# thus no comparison
	i = 0
	while(i < n) :
		
		# this would be executed at-most n times
		# and therefore at-most n comparisons
		if (arr[i] == x) :
			
			# replace arr[n-1] with its actual
			# element as in original 'arr[]'
			arr[n-1] = backup

			# if 'x' is found before the '(n-1)th'
			# index, then it is present in the
			# array final comparison
			if (i < n-1):
				return "Found"

			# else not present in the array
			return -1
		i = i + 1

# Driver Code
arr = [4, 6, 1, 5, 8]
n = len(arr)
x = int (input ("Enter the number: "))
result=(search(arr, n, x))
if result==-1:
    print(search(arr, n, x))
else:
    print ("{Element is present in array", str(result))


