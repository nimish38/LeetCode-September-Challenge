class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        muta, n = list(s), len(s)
        while True:
            start, i = len(muta), 0
            while i + k <= len(muta):
                val = muta[i: i + k]
                if len(set(val)) == 1:
                    del muta[i: i + k]
                    i = max(-1, i - k)
                i += 1
            if start == len(muta):
                return ''.join(muta)


print(Solution().removeDuplicates(s = "yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", k = 4))

