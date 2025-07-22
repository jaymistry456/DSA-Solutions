# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # TC: O(V + E), SC: O(V + E)
        visited = [0] * numCourses  # 0: unvisited, 1: visiting, 2: visited
        graph = defaultdict(list)   # key (node) -> value (prerequisites)
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
        cycle = False
        def dfs(course):
            nonlocal cycle
            if visited[course] == 0:
                visited[course] = 1
                for requisite in graph[course]:
                    dfs(requisite)
                visited[course] = 2
            elif visited[course] == 1:
                cycle = True
                return
        for course in range(numCourses):
            dfs(course)
        return not cycle  