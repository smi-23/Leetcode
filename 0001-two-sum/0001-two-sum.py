from typing import List
class Solution:
    def twoSum(self, nums: list[int], target: int)->list[int]:
        table = {}
        n = len(nums)

        # for i, num in enumerate(nums):
        #     complement = target - num
        #     if complement in table:
        #         return table[complement], i
        #     else:
        #         table[num] = i
                
        
        ## enumerate를 안하고
        for i in range(n):
            complement = target - nums[i]
            if complement in table:
                return [table[complement], i]
            else:
                table[nums[i]] = i

        # ## 완탐
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if target == nums[i] + nums[j]:
        #             return [i, j]
            

nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)
print(f"target = {target}")
# print("target =", target)
print("nums =", nums)
print(f"result = {result}")