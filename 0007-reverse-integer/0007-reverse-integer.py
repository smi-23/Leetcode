class Solution:
    def reverse(self, x: int) -> int:
        if x <0:
            flag = -1
        else:
            flag = 1
        s = str(abs(x))
        x = int(s[::-1])
        if x < 2**31:
            return x * flag
        else:
            return 0