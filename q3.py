
def func(arr):

	n = len(arr)

	# If length of array is even
	if n % 2 == 0:
		z = n // 2
		e = arr[z]
		q = arr[z - 1]
		return (e + q) / 2
		
		
	# If length of array is odd
	else:
		z = n // 2
		return arr[z]
		

# Driver code
if __name__ == "__main__":
	
    arr1 = [ 1, 3]
    arr2 = [ 2]

    # Concatenating the two arrays
    arr3 = arr1 + arr2

    # Sorting the resultant array
    arr3.sort()

    print('Median is: ', func(arr3))
 

