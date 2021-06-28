# Bubble sort
def bubble_sort(arr: list) -> list:
    l = len(arr)
    for i in range(l - 1):
        swapped = False
        for j in range(l - i - 1):   
            if arr[j] > arr[j+1]:   # If an element is greater than after element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:   # It indicates that all the elements are sorted 
            break         # And we can neglect further checking
    return arr

if __name__ == '__main__':
    print(bubble_sort([6,5,4,3,2,1]))