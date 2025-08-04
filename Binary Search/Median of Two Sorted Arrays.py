# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # brute-force
        # TC: O(mlogm+nlogn), SC: O(m+n)
        arr = nums1 + nums2
        arr.sort()
        n = len(arr)
        if n % 2 == 1:
            return arr[n // 2]
        else:
            return (arr[n // 2 - 1] + arr[n // 2]) / 2


        # better
        # TC: O(m+n), SC: O(m+n)
        i = 0
        j = 0
        m = len(nums1)
        n = len(nums2)
        res = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        while i < m:
            res.append(nums1[i])
            i += 1
        while j < n:
            res.append(nums2[j])
            j += 1
        totalLength = m + n
        if totalLength % 2 == 1:
            return res[totalLength // 2]
        else:
            return (res[totalLength // 2 - 1] + res[totalLength // 2]) / 2


        # optimal
        # TC: O(logm+logn), SC: O(1)
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        totalLength = m + n
        l = 0
        r = m
        while l <= r:
            i = l + (r - l) // 2
            j = totalLength // 2 - i
            l1 = nums1[i - 1] if i - 1 >= 0 else float('-inf')
            r1 = nums1[i] if i < m else float('inf')
            l2 = nums2[j - 1] if j - 1 >= 0 else float('-inf')
            r2 = nums2[j] if j < n else float('inf')
            if l1 <= r2 and l2 <= r1:
                if totalLength % 2 == 1:
                    return min(r1, r2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                r = i - 1
            else:
                l = i + 1