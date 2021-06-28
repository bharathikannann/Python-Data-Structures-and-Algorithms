# Number of edit distance required to change one string to another
def edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[None] * (n + 1) for i in range(m + 1)]
    for row in range(m + 1):
        for col in range(n + 1):
            if row == 0:
                dp[row][col] = col
            elif col == 0:
                dp[row][col] = row
            elif s1[row - 1] == s2[col - 1]:   # If both strings are equal no operation is required
                dp[row][col] = dp[row - 1][col - 1]
            else:                              # Get one plus min of insert, delete, replace
                dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1]) + 1
    return dp[m][n]

    '''
    Dp Table
        '' s  a  t  u  r  d  a  y
     ''|0, 1, 2, 3, 4, 5, 6, 7, 8|
     s |1, 0, 1, 2, 3, 4, 5, 6, 7|
     u |2, 1, 1, 2, 2, 3, 4, 5, 6|
     n |3, 2, 2, 2, 3, 3, 4, 5, 6|
     d |4, 3, 3, 3, 3, 4, 3, 4, 5|
     a |5, 4, 3, 4, 4, 4, 4, 3, 4|
     y |6, 5, 4, 4, 5, 5, 5, 4, 3|
    '''

if __name__ == '__main__':
    print(edit_distance("sunday","saturday"))