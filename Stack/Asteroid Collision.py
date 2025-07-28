# https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # TC: O(n), SC: O(n)
        stack = []
        n = len(asteroids)
        for i in range(n):
            curr = asteroids[i]
            while stack and stack[-1] > 0 and curr < 0:
            # collision
                if abs(curr) > stack[-1]:
                    stack.pop()
                elif abs(curr) < stack[-1]:
                    curr = 0
                    break
                else:
                    stack.pop()
                    curr = 0
                    break
            if curr != 0:
                stack.append(curr)
        return stack