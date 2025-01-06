from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank) -> int:
        if endGene not in bank:
            return -1
        que, muta, genes, n, bank, vis = deque([startGene]), 0, {'A', 'T', 'C', 'G'}, len(startGene), dict.fromkeys(bank,0), {startGene: 1}
        # print(genes - {'A'})
        while que:
            lvl = len(que)
            for _ in range(lvl):
                gene = que.popleft()
                for i in range(n):
                    for x in genes:
                        new_gene = gene[:i] + x + gene[i + 1:]
                        if new_gene in bank and new_gene not in vis:
                            if new_gene == endGene:
                                return muta + 1
                            que.append(new_gene)
                            vis[gene] = 0
            muta += 1
        return -1

print(Solution().minMutation(startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]))

