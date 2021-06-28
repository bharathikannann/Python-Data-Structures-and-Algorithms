# knapsack 0/1 problem
def knapsack01(values, weights, maxweight):
    dp =[[None] * (maxweight + 1) for _ in range(len(weights) + 1)]
    for i in range(len(values) + 1):
        for m in range(maxweight + 1):
            ci = i - 1   # Current item since index of list starts at 0
            if i == 0 or m == 0:
                dp[i][m] = 0
            elif weights[ci] > m:   # Fill wit zero if the current index is less than m, it means we cannot but any item 
                dp[i][m] = dp[i - 1][m]   # Fill it with values that we can add without that item
            else:
                withi = values[ci] + dp[i - 1][m - weights[ci]] 
                withouti = dp[i - 1][m]
                dp[i][m] = max(withi, withouti)   # Max with that item and without
    return dp[-1][-1]
    '''
    Dp table
    Maxweight - maximum weight
    weights - [5, 3,  4, 2] 
    values -  [60,50,70,30]
    Each column in weights and rows correspond to i'th item
    Item 1 -> weight = 5, value -> 60
    Maxweight 0  1  2   3   4   5       
    Item0 -  [0, 0, 0,  0,  0,  0 ]
    Item1 -  [0, 0, 0,  0,  0,  60]
    Item2 -  [0, 0, 0,  50, 50, 60]
    Item3 -  [0, 0, 0,  50, 70, 70]
    Item4 -  [0, 0, 30, 50, 70, 80]
    '''
    

if __name__ == '__main__':
    print(knapsack01([60,50,70,30], [5,3,4,2], 5))


# Complexities
# 
# - n = total items
# - m = max weight (max weight constraint)
# 
# `Time: O(nm)` (we will be solving this many subproblems)
# 
# `Space: O(nm)` (we will store the results of n*m subproblems)


