# Generate fibanocci sequence
def fibanocci_sequence(n: int) -> int:
    if n<=1:
        return n
    dp = [None] * n
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n-1]

if __name__ == "__main__":
    print(fibanocci_sequence(5))