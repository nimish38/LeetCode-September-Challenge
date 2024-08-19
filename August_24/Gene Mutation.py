class Solution:
    def minMutation(self, startGene: str, endGene: str, bank) -> int:
        if endGene not in bank:
            return -1
        diff = []
        for i in range(len(startGene)):
            if startGene[i] != endGene[i]:
                diff.append(i)

        
