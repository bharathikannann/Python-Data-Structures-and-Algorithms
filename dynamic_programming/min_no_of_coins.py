# Minimum number of coins needed to make the given amount
def min_no_of_coins(amount:int, coins: list) -> int:
    # DP stores the number of coin used for each amount
    # Initialize all values to amount + 1 as a dummy value
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0   # We can't use any coin for 0 amount
    for a in range(1, amount + 1):
        for c in range(len(coins)):
            if coins[c] <= a:   # Only if coin amount is less then given amount
                dp[a] = min(dp[a], dp[a - coins[c]] + 1)   # Check min of current coins used and given coin used 
    if dp[amount] > amount:   # If we can't produce the amount with thosse coins
        return -1
    return dp[amount]
    '''
    Dp table
    Amount      ->   0  1  2  3  4  5  6  7  8  9  10 11
    No of coins ->  [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
    '''

if __name__ == "__main__":
    print(min_no_of_coins(11,[1,2]))
    print(min_no_of_coins(11,[2]))