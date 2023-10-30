from typing import List
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        ans = []
        for i in range(n):
            if number[i] == digit:
                ans.append(number[:i]+ number[i+1:])
        return str(max(ans))
                