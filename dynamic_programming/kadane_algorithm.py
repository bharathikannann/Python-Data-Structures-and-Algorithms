# Largest sub array problem
def kadane_algorithm(arr: list) -> int:
    l = len(arr)
    maxhere = arr[0]   
    maxoutput = 0      # For getting the max subarray value
    for i in range(1,l):
        # If adding the element to prev max is greater or the current number is greater
        maxhere = max(arr[i], arr[i] + maxhere) 
        # Keep track of greatest maxhere
        maxoutput = max(maxhere, maxoutput)
        '''
        Example : 
        arr =      [-2, -3, 4, -1, -2, 1, 5, -3]
        maxhere =   -2  -3  4   3   1  2  7   4
        maxoutput = -2  -2  4   4   4  4  7   7
        '''
    return maxoutput

if __name__ == '__main__':
    print(kadane_algorithm([-2,-3,4,-1,-2,1,5,-3]))