import itertools
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def IsPowerOfTwo( x):
            return x & (x - 1) == 0

        num = list(str(n))
        perms = list(itertools.permutations(num))

        for val in perms:
            if val[0] == '0':
                continue
            number = int(''.join(val))
            if IsPowerOfTwo(number):
                return True
        return False

Solution().reorderedPowerOf2(435)