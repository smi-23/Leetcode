from typing import List
class Solution:
    def twoSum(self, nums: list[int], target: int)->list[int]:
        table = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in table:
                return table[complement], i
            else:
                table[num] = i

nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)
print(f"target = {target}")
# print("target =", target)
print("nums =", nums)
print(f"result = {result}")