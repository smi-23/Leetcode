from typing import List
from collections import defaultdict, deque
class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==0 or n ==1:
            return 1
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
            

n = 2

solution = Solution()
result = solution.climbStairs(n)
print(f"result = {result}")