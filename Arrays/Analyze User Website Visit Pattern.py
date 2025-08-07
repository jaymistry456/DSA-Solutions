# https://leetcode.ca/all/1152.html

from collections import defaultdict
from typing import List

class Solution:
    def mostVisitedPattern(
        self, usernames: List[str], timestamps: List[int], websites: List[str]
    ) -> List[str]:
        # TC: O(nlogn), SC: O(n)
        arr = list(zip(usernames, timestamps, websites))
        arr.sort(key=lambda x:x[1])
        userWebsites = defaultdict(list)    # user -> list of websites
        for user, time, website in arr:
            userWebsites[user].append(website)
        patternVisitCount = defaultdict(int)    # 3-site pattern -> no. of users matching this pattern
        for user, sites in userWebsites.items():
            n = len(sites)
            if n >= 3:
                uniquePatterns = set()
                for i in range(n):
                    for j in range(i + 1, n):
                        for k in range(j + 1, n):
                            uniquePatterns.add((sites[i], sites[j], sites[k]))
                for pattern in uniquePatterns:
                    patternVisitCount[pattern] += 1
        res = []
        maxVisited = 0
        for pattern, noOfUsers in patternVisitCount.items():
            if noOfUsers > maxVisited or (noOfUsers == maxVisited and pattern < res):
                maxVisited = noOfUsers
                res = list(pattern)
        return res