from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        ans = []
        for num in nums:
            if num == target:
                ans.append(nums.index(num))
                break
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                ans.append(i)
                return ans
            
        return [-1, -1]