class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minV=len(nums)+1
        if sum(nums)<target:
            return 0
        start=0
        tot=0
        for end in range(len(nums)):
            tot+=nums[end]
            while tot>=target:
                minV=min(minV,end-start+1)
                tot-=nums[start]
                start+=1
        return minV