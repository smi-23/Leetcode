from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ""
        ans = ""
        for i in s:
            if i not in temp:
                temp += i
            else:
                ind = temp.index(i)
                if len(temp) > len(ans):
                    ans = temp
                else:
                    ans = ans
                temp = temp[ind +1:]
            
                temp += i
        if len(temp) > len(ans):
            ans = temp
        else:
            ans = ans
        return len(ans)         
        