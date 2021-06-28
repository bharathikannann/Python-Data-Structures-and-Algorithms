# Return the sum between two indices
class RangeSumQuery:
    def __init__(self, arr):
        # arr ->  [1,2,3]
        # dp -> [0,1,3,6] after calculations
        self.dp = [0] * (len(arr) + 1)
        for i in range(0, len(arr)):
            self.dp[i + 1] = self.dp[i] + arr[i]
        # Sum between two range
    def range_sum_query(self, i, j):
        return self.dp[j] - self.dp[i - 1]        

if __name__ == '__main__':
    rsq = RangeSumQuery([1,2,3])
    print(rsq.range_sum_query(1,2))
    print(rsq.range_sum_query(2,3))
    print(rsq.range_sum_query(1,3))