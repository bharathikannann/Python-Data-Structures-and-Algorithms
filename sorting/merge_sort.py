# Merge sort
def merge_sort(arr: list):
    beg, end = 0,len(arr) - 1
    return _merge_sort(arr,beg, end)

# Dividing the lists until 1 element is present
def _merge_sort(arr: list, beg: int, end: int):
    if(beg < end):
        mid = (beg + end) // 2
        _merge_sort(arr, beg, mid)
        _merge_sort(arr, mid+1, end)
        _merge(arr, beg, mid, end)   # Merge the arrays

def _merge(arr: list, beg: int, mid: int, end: int):
    left = mid - beg + 1   # No of elements in left side
    right = end - mid      # No of elements in right side
    leftarr = [0] * left   # Create temp lists
    rightarr = [0] * right
    # Copy values to temp lists
    for i in range(left):  
        leftarr[i] = arr[beg+i]
    for i in range(right):
        rightarr[i] = arr[mid+i+1]
    # Initialize k to beg, since we are changing values in place
    i,j,k = 0,0,beg
    while(i<left and j<right):   # Loop until any one loop becomes empty
        if leftarr[i] < rightarr[j]:
            arr[k] = leftarr[i]  # Change the original array
            i = i+1
        else:
            arr[k] = rightarr[j]
            j = j+1
        k += 1                   # Increment k since it updates in every loop
    # If any one list is not emptied, add them directly to original array
    while(i<left):
        arr[k] = leftarr[i]
        k,i = k+1, i+1
    while(j<right):
        arr[k] = right[j]
        k,j = k+1, j+1

if __name__ == '__main__':
    a = [4,3,2,1]
    merge_sort(a)
    print(a)