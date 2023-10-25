from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # 입력 리스트를 정렬

        for i in range(len(nums) - 2):
            # 중복된 요소 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    triplet = [nums[i], nums[left], nums[right]]
                    result.append(triplet)

                    # 중복된 요소 건너뛰기
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result

# 입력 데이터
nums = [-1, 0, 1, 2, -1, -4]

# Solution 클래스의 인스턴스 생성
solution = Solution()

# tripleSum 메소드 호출
result = solution.threeSum(nums)
print("result =", result)