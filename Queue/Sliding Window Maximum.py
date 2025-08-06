# https://leetcode.com/problems/sliding-window-maximum/description/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute-force
        # TC: O(n*k), SC: O(1)
        res = []
        n = len(nums)
        for i in range(n - k + 1):
            currMax = float('-inf')
            for j in range(i, i + k):
                currMax = max(currMax, nums[j])
            res.append(currMax)
        return res


        # optimal
        # TC: O(n), SC: O(k)
        q = deque()    # stores indexes with largest at the start (left)
        l = 0
        r = 0
        n = len(nums)
        res = []
        while r < n:
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            q.append(r)
            if r >= k - 1:
                res.append(nums[q[0]])
                l += 1
            if q[0] < l:
                q.popleft()
            r += 1
        return res