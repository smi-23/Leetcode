# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.

from typing import List
from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
         c = Counter(arr)
         s = sorted(arr, key = lambda x: (c[x], x))
         return len(set(s[k:]))

            
            
# arr = [2,1,1,3,3,3]
arr = [4,3,1,1,3,3,2]
# arr = [5,5,4]
# k = 1
k = 3
solution = Solution()
result = solution.findLeastNumOfUniqueInts(arr, k)
print(f"result = {result}")
