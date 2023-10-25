from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for a in zip(*strs):
            print(f"zil = {zip(strs)}")
            print(f"a = {a}")
            if len(set(a)) == 1: 
                res += a[0]
            else: 
                return res
        return res

strs = ["flower","flow","flight"]

solution = Solution()
result = solution.longestCommonPrefix(strs)
print(f"result = {result}")