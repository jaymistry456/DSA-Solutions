# https://leetcode.com/problems/minimum-genetic-mutation/

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # TC: O(m*l^2), SC: O(m*l)
        if endGene not in bank:
            return -1
        hashmap = defaultdict(list)    # pattern -> list of genes matching pattern
        for i in range(len(bank)):
            gene = bank[i]
            for j in range(len(gene)):
                pattern = gene[:j] + "*" + gene[j+1:]
                hashmap[pattern].append(gene)
        q = deque()
        q.append(startGene)
        visited = set()
        visited.add(startGene)
        res = 0
        while q:
            for _ in range(len(q)):
                currGene = q.popleft()
                if currGene == endGene:
                    return res
                for i in range(len(currGene)):
                    pattern = currGene[:i] + "*" + currGene[i+1:]
                    for neiGene in hashmap[pattern]:
                        if neiGene not in visited:
                            q.append(neiGene)
                            visited.add(neiGene)
            res += 1
        return -1