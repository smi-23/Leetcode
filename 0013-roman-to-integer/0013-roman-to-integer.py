class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        ans = 0
        n = len(s)
        for i in range(n):
            if i < n-1 and table[s[i]] < table[s[i+1]]:
                ans -= table[s[i]]
            else:
                ans += table[s[i]]
        return ans
