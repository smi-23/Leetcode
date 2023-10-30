class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        ans1 = nums1.copy()
        ans2 = nums2.copy()
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    if num1 in ans1:
                        ans1.remove(num1)
                    if num2 in ans2:
                        ans2.remove(num2)
        return [ans1, ans2]