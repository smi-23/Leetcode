from typing import List
class Solution:
    def unequalTriplets(self, nums: List[int])->int:
        nums.sort()
        cnt = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                if nums[i] == nums[j]:
                    continue
                for k in range(j+1, len(nums)):
                    if nums[i] != nums[j] != nums[k]:
                        cnt += 1
        return cnt
nums = [4,4,2,4,3,5,6]
"""
# nums = [4,4,2,4,3]  
# nums = [1,2,3]       
# nums = [1,1,1,1]   
"""   

solution = Solution()
result = solution.unequalTriplets(nums)
print(f"result = {result}")