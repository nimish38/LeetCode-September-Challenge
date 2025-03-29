class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                left, right = s[i + 1: j + 1], s[i: j]
                if left == left[:: -1] or right == right[:: -1]:
                    return True
                return False
        return True


print(Solution().validPalindrome(s = "aabbbcaa"))