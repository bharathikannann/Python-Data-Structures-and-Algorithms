# Linear Search
def linear_search(arr: list, target: int) -> int:
    # arr - Collection of items
    # target - element tobe found
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1

'''
Example
>>>linear_search([1,2,3,4],1)
0
>>>linear_search([1,2,3,4],2)
1
>>>linear_search([1,2,3,4],3)
2
>>>linear_search([1,2,3,4],4)
3
>>>linear_search([1,2,3,4],5)
-1
'''

if __name__ == '__main__':
    print("Linear Search")
    print(linear_search([1,2,3,4],2))