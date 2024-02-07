class Solution:
    def reverseVowels(self, s: str) -> str:
        strList = list(s)
        vowels = 'AaEeIiOoUu'

        i, j = 0, len(s) - 1
        while(i < j):
            if strList[i] in vowels and strList[j] in vowels:
                strList[i], strList[j] = strList[j], strList[i]
                i += 1
                j -= 1
            else:
                if strList[i] not in vowels:
                    i += 1
                if strList[j] not in vowels:
                    j -= 1

        return ''.join(strList)


a = Solution()
print(a.reverseVowels('leetcode'))

