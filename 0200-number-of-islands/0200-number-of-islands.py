from typing import List
from collections import defaultdict, deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

        def bfs(x, y):
            q = deque()
            q.append((x, y))
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if (
                        nx < 0
                        or nx >= n
                        or ny < 0
                        or ny >= m
                        or grid[nx][ny] == "0"
                    ):
                        continue
                    grid[nx][ny] = "0"
                    q.append((nx, ny))

        def dfs(x, y):
            if (
                x < 0
                or x >= n
                or y < 0
                or y >= m
                or grid[x][y] == "0"
            ):
                return
            grid[x][y] = "0"

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                dfs(nx, ny)

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    # bfs(i, j)
                    ans += 1
        return ans


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

solution = Solution()
result = solution.numIslands(grid)
print(f"result = {result}")
