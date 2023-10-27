from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [(1, 0, "(")]
        for i in range(2 * n - 1):
            temp_len = len(stack)
            for j in range(temp_len):
                left, right, parenthesis = stack.pop(0)
                # there are two potential data: (left + 1, right), (left, right + 1)
                if left + 1 <= n and right <= n and left + 1 >= right:
                    stack.append((left + 1, right, parenthesis + "("))
                if left <= n and right + 1 <= n and left >= right + 1:
                    stack.append((left, right + 1, parenthesis + ")"))
        res = []
        for item in stack:
            res.append(item[2])
        return res