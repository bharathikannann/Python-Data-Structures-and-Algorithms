# Quick sort
def quick_sort(arr: list):
    _quick_sort(arr, 0, len(arr) - 1)

def partition(arr: list, l:int, h:int):
    i = l                                  # Index of larger element that is to be swapped
    pivot = arr[h]                         # Pivot choosen as last element
    for j in range(l, h):
        if arr[j] < pivot:                 # If pivot is larger, then swap j with larger element
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[h], arr[i] = arr[i], arr[h]        # Swap pivot with i
    return i

def _quick_sort(arr: list, l:int, h:int):
    if l < h:
        p = partition(arr, l, h)           # P is in appropriate position
        _quick_sort(arr, l, p-1)           # Partition left side of p
        _quick_sort(arr, p+1, h)           # Partition right side of p

if __name__ == '__main__':
    a = [4,3,2,1,4,3]
    quick_sort(a)
    print("Sorted List")
    print(a)