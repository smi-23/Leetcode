from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        # 주어진 days 안에서 m개의 꽃다발을 만들 수 있는지 확인
        def isEnoughDays(days):
            # 현재 꽃들의 수  / 현재까지 만든 꽃다발 수
            flowers, bouquets = 0, 0
            for day in bloomDay:
                if day <= days:
                    flowers += 1
                else:
                    flowers = 0

                if flowers == k:
                    bouquets += 1
                    if bouquets == m:
                        break
                    flowers = 0
            return bouquets == m

        left, right = 1, max(bloomDay)
        while left < right:
            days = left + (right - left) // 2
            if isEnoughDays(days):
                right = days
            else:
                left = days + 1
        return left