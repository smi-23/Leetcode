from typing import List
from collections import defaultdict, deque
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 아래와 같이 완탐으로 풀면 시간초과 발생
        # max_price = 0
        
        # for i in range(len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         price = prices[i]-prices[j]
        #         price = -1 * price
        #         max_price = max(max_price, price)
        # return max_price
        
        max_profit = 0
        min_price = prices[0]
        for price in prices[1:]:
            max_profit = max(max_profit, price-min_price)
            min_price = min(min_price, price)
        return max_profit

prices = [7,1,5,3,6,4]

solution = Solution()
result = solution.maxProfit(prices)
print(f"result = {result}")