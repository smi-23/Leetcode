# int를 str로 변혼해서 가볍게 풀이
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        i = 0
        while (i <= (len(x)-1-i)):
            if x[i] != x[len(x)-i-1]:
                return False
            else:
                i += 1
        return True