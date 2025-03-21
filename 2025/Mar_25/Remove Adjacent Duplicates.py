class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        muta, n = list(s), len(s)
        while True:
            start, i = len(muta), 0
            while i + k < len(muta):
                val = muta[i: i + k]
                if len(set(val)) == 1:
                    del muta[i : i + k]
                    i = -1
                i += 1
            if start == len(muta):
                return ''.join(muta)


print(Solution().removeDuplicates(s = "pbbcggttciiippooaais", k = 2))

