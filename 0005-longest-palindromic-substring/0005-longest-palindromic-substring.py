class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 시간 복잡도 문제를 해결해야 하는 풀이
        if len(s) == 1:
            return s
        max_len = 1
        max_str = s[0]
        # max_str = []
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    if j-i+1 > max_len:
                        max_len = j-i+1
                        max_str = s[i:j+1]
        return max_str