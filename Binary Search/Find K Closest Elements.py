# https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # brute-force
        # TC: O(nlogn + klogk), SC: O(n)
        arr.sort(key=lambda num:(abs(num - x), num))
        return sorted(arr[:k])

        # better
        # TC: O(n + klogk), SC: O(k)
        n = len(arr)
        # find the closest num
        closest = 0
        for i in range(n):
            if abs(arr[i] - x) < abs(arr[closest] - x):
                closest = i
        # traverse in both directions from the closest num
        l = closest - 1
        r = closest + 1
        res = [arr[closest]]
        while len(res) < k:
            if l >= 0 and r < n:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
            elif l >= 0:
                res.append(arr[l])
                l -= 1
            elif r < n:
                res.append(arr[r])
                r += 1
        return sorted(res)


        # optimal
        # TC: O(logn + klogk), SC: O(k)
        n = len(arr)
        # find the closet num
        start = 0
        end = n - 1
        while start < end:
            mid = start + (end - start) // 2
            if arr[mid] < x:
                start = mid + 1
            else:
                end = mid
        # traverse in both directions
        res = []
        l = start - 1
        r = start
        while len(res) < k:
            if l >= 0 and r < n:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
            elif l >= 0:
                res.append(arr[l])
                l -= 1
            elif r < n:
                res.append(arr[r])
                r += 1
        return sorted(res)