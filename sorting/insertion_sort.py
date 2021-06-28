# Insertion sort
def insertion_sort(arr: list) -> list:
    l = len(arr)
    for i in range(1,l):   # Start from 1 to last
        for j in range(i,0,-1):    
            if arr[j] < arr[j-1]:   # # Swap all elements before i with this condition
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

if __name__ == '__main__':
    print(insertion_sort([6,3,5,4,3,2,1]))