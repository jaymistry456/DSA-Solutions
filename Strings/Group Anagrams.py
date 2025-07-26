# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute-force
        # TC: O(m*nlogn), SC: O(m*n)  m = number of strs, n = avg. len. of string
        res = defaultdict(list) # key (sorted string) -> value (anagrams of string)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())


        # optimal
        # TC: O(m*n), SC: O(m*n)
        res = defaultdict(list) # key (freq arr of chars) -> value (strs)
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            res[tuple(arr)].append(s)
        return list(res.values())