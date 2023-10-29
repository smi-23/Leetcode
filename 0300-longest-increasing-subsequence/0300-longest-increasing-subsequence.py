from typing import List
from collections import defaultdict, deque
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1) 
        return max(dp) + 1
            
            

nums = [10,11,12,2,5,3,7,101,18]
solution = Solution()
result = solution.lengthOfLIS(nums)
print(f"result = {result}")