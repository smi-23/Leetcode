from typing import List
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for n1, n2 in prerequisites:
            graph[n2].append(n1)
        
        visited = set()
        traced = set()
        
        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)
            return True
        
        for i in list(graph):
            if not dfs(i):
                return False
        return True
            

numCourses = 2
prerequisites = [[1,0],[0,1]]

solution = Solution()
result = solution.canFinish(numCourses, prerequisites)
print(f"result = {result}")

"""
for i in list(graph): 라인으로 변경하면 에러가 해결되는 이유는 list(graph)가 실제로 딕셔너리 graph의 키 목록을 가져오기 때문입니다. 이렇게하면 순회하는 동안에 graph가 변경되어도 순회 중에 에러가 발생하지 않습니다. Python은 이 키 목록에 대한 고정된 스냅샷을 생성하여 순회를 수행하기 때문에 안정적으로 순회할 수 있습니다.

반면에 for i in graph:를 사용하면 graph의 내용이 변경되면서 순회 중에 문제가 발생합니다. 즉, 순회 중에 딕셔너리 내용이 동적으로 변경되면서 런타임 시에 에러가 발생하게 되는데, 이를 방지하기 위해 list(graph)와 같이 미리 고정된 키 목록을 만들어 사용하는 것이 좋습니다.
"""
