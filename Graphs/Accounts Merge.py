# https://leetcode.com/problems/accounts-merge/description/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU == rootV:
            # cycle detected, union not possible
            return False
        else:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1
            return True

class Solution:
    # n = no. of accounts, e = no. of emails across all accounts
    # TC: O(n + eloge), SC: O(n + e)
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        unionFind = UnionFind(n)
        # email -> accounts
        emailToAcc = {}     # key (email) -> value (first account index)
        for i in range(n):
            for email in accounts[i][1:]:
                if email in emailToAcc:
                    unionFind.union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i
        # account -> emails (merge emails for root accounts)
        accToEmails = defaultdict(set)    # key (account) -> value (set of emails)
        for email, acc in emailToAcc.items():
            leader = unionFind.find(acc)
            accToEmails[leader].add(email)
        # sort the emails
        res = []
        for acc, emails in accToEmails.items():
            res.append([accounts[acc][0]] + sorted(emails))
        return res