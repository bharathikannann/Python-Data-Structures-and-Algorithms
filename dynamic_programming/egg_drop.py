# Egg dropping problem
# Minimum no of trials needed in worst case to find the floor
def egg_drop(eggs, floors):
    INT_MAX = 32767   
    dp = [[0] * (floors + 1) for _ in range(eggs + 1)]
    for i in range(1, eggs + 1):   # If we have only one floor, then we need 1 try
        dp[i][1] = 1
    for i in range(1, floors + 1): # If we have one egg we need to go to all floors
        dp[1][i] = i
    for e in range(2, eggs + 1):
        for f in range(2, floors + 1):
            dp[e][f] = INT_MAX
            for i in range(1, f + 1): # For trying in each floors
                # There are two possibilities
                # Eggs breaks -> Subtract one egg and check all floors down (e-1,i-1)
                # Egg not breaks -> With same no of eggs we need to check all floors above it (e,f - i)
                # If floors =4, and we are checking in floor 2 and if egg breaks the number of upper floors will be (4-2)->(f-i)
                res = 1 + max(dp[e - 1][i - 1], dp[e][f - i])
                if res < dp[e][f]:   # Get the minimum worst case posibilities
                    dp[e][f] = res
    return dp[eggs][floors]

if __name__ == '__main__':
    print(egg_drop(2, 2))