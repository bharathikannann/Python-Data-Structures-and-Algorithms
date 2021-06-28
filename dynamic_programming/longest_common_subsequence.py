# Longest common subsequence of two strings
# longest_common_subsequence("AGGTAB", "GXTXAYB") -> 4 which is GTAB
def longest_common_subsequence(s1, s2):
    m = len(s1) + 1
    n = len(s2) + 1
    dp = [[None] * n for i in range(m)]
    for row in range(m):
        for col in range(n):
            if row == 0 or col == 0:   # Base case for empty strings
                dp[row][col] = 0
            elif s1[row - 1] == s2[col - 1]:   # If both strings are equal
                dp[row][col] = dp[row - 1][col - 1] + 1   # Then the answer is best solution without those two strings plus 1
            else:
                dp[row][col] = max(dp[row-1][col], dp[row][col - 1])   # Max of without one of the letters in both strings
    return dp[m - 1][n - 1]

    '''
    Dp table looks like
         '' G  X  T  X  A  Y  B
    ''   0, 0, 0, 0, 0, 0, 0, 0
    A    0, 0, 0, 0, 0, 1, 1, 1
    G    0, 1, 1, 1, 1, 1, 1, 1
    G    0, 1, 1, 1, 1, 1, 1, 1
    T    0, 1, 1, 2, 2, 2, 2, 2
    A    0, 1, 1, 2, 2, 3, 3, 3
    B    0, 1, 1, 2, 2, 3, 3, 4
    '''

if __name__ == "__main__":
    print(longest_common_subsequence("AGGTAB", "GXTXAYB"))