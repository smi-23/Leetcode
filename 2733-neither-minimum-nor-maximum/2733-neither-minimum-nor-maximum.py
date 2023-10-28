from typing import List
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        # nums.sort()
        # n = len(nums)
        # if n <= 2:
        #     return -1
        # return nums[1]


        if len(nums)<=2:
            return -1
        return sorted(nums[:3])[1]
