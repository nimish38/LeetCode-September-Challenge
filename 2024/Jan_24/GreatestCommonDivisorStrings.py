import math
class Solution:
    # def gcd(self, a, b):
    #     if a == b:
    #         return a
    #     if a > b:
    #         return self.gcd(a - b, b)
    #     else:
    #         return self.gcd(a, b - a)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if str1 == str2:
        #     return str1
        #
        # if len(str1) > len(str2):
        #     big = str1
        #     small = str2
        # else:
        #     big = str2
        #     small = str1
        #
        # multiples = len(small)
        # while multiples > 0:
        #     if len(big) % multiples == 0 and len(small) % multiples ==0:
        #         curr = small[:multiples]
        #         if curr * (len(big)//multiples) == big and curr * (len(small)//multiples) == small:
        #             return curr
        #     multiples -= 1
        # return ""

        #         Optimal Solution
        if str1 + str2 != str2 + str1:
            return ""
        gcdNum = math.gcd(len(str1), len(str2))
        return str1[:gcdNum]




check = Solution()
print(check.gcdOfStrings('ABCABCABC', 'ABCABC'))