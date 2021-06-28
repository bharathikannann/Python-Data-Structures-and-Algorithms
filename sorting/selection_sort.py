# Selection sort
# For visualization check https://visualgo.net/en/sorting
# The smallest element is found each time and is moved to front 
def selection_sort(arr: list) -> list:
    l = len(arr)
    for i in range(l - 1):
        minidx = i   # To keep track of min element
        for j in range(i + 1, l):
            if arr[minidx] > arr[j]:   # If any element is smaller than min index
                minidx = j
        if minidx != i:   # If min index is i then no swap
            arr[i], arr[minidx] = arr[minidx], arr[i]   # swap minindex with i
    return arr            

if __name__ == '__main__':
    print(selection_sort([4,3,2,1]))