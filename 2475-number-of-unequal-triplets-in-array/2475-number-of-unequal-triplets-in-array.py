class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                if nums[i] == nums[j]:
                    continue
                for k in range(j+1, len(nums)):
                    if 0 <= nums[i] < nums[j] < nums[k]:
                        cnt += 1
        return cnt