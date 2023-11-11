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
            
# nums[i]를 value가 아닌 key로 사용하는 이유는 빠른 검색을 위한 용도로 사용됩니다. 
# 즉, 특정 값을 가지는 키를 가지고 있는지 빠르게 확인할 수 있습니다.
nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)
print(f"target = {target}")
# print("target =", target)
print("nums =", nums)
print(f"result = {result}")