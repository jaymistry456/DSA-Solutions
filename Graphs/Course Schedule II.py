# https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # TC: O(v+e), SC: O(v+e)
        visited = [0] * numCourses  # 0: unvisited, 1: visiting, 2: visited
        graph = defaultdict(list)   # key (course) -> value (prereqs for course)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        res = []
        cycle = False
        def dfs(course):
            nonlocal cycle
            if visited[course] == 0:
                visited[course] = 1
                for prereq in graph[course]:
                    dfs(prereq)
                visited[course] = 2
                res.append(course)
            elif visited[course] == 1:
                cycle = True
                return
            else:
                return
        for course in range(numCourses):
            dfs(course)
            if cycle:
                return []
        return res