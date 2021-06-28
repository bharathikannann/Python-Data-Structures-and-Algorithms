# Binary search
# Searches element in a sorted list
def binary_search(arr: list, n: int) -> int:
    # Arr - Sorted list
    # N - value to be found
    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = (high + low) // 2
        if arr[mid] == n:   # If value id found
            return mid
        if arr[mid] > n:    # Check only left half
            high = mid - 1
        else:               # Check only right half
            low = mid + 1
    return -1

if __name__ == '__main__':
    print(binary_search([1,2,3,4],4))