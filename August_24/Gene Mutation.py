from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank) -> int:
        if endGene not in bank:
            return -1
        que, muta, genes, n = deque([startGene]), 0, ['A', 'T', 'C', 'G'], len(startGene)
        while que:
            lvl = len(que)
            for _ in range(lvl):
                gene = que.popleft()
                for i in range(n):
                    if gene[i] != endGene[i]:
                        for x in genes - gene[i]:
                            new_gene = gene[:i] + x + gene[i + 1:]
                            if new_gene in bank:
                                if new_gene == endGene:
                                    return muta + 1
                                que.append(new_gene)
            muta += 1
        return -1

    

