class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        muta, n = list(s), len(s)
        while True:
            start, i = len(muta), 0
            while i + k < n:
                if len(set(muta[i: i + k])) == 1:
                    del muta[i : i + k]
                    i = 0
            if start == len(muta):
                return ''.join(muta)

        

