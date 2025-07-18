# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # DFS
        # TC: O(m*n), SC: O(m*n)
        original_color = image[sr][sc]  # store the starting pixel color
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # for adjacent traversal
        m = len(image)
        n = len(image[0])
        visited = set() # only needed when original_color == color
        
        def dfs(r, c):
            image[r][c] = color
            visited.add((r, c))
            for dr, dc in directions:
                if 0 <= r + dr < m and 0 <= c + dc < n and (r + dr, c + dc) not in visited and image[r + dr][c + dc] == original_color:
                    dfs(r + dr, c + dc)
        dfs(sr, sc)

        return image


        # BFS
        # TC: O(m*n), SC: O(m*n)
        original_color = image[sr][sc]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # for adjacent traversal
        m = len(image)
        n = len(image[0])
        
        q = deque()
        visited = set()
        q.append((sr, sc))
        visited.add((sr, sc))

        while q:
            r, c = q.popleft()
            image[r][c] = color
            for dr, dc in directions:
                if 0 <= r + dr < m and 0 <= c + dc < n and (r + dr, c + dc) not in visited and image[r + dr][c + dc] == original_color:
                    q.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
        return image