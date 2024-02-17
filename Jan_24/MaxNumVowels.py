class Solution:
    def countVowels(self, str, vowels):
        cnt = 0
        for char in str:
            if char in vowels:
                cnt += 1
        return cnt

    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        curVow, maxVow = self.countVowels(s[:k], vowels), 0
        for i in range(1, len(s) - k + 1):
            if s[i - 1] in vowels:
                curVow -= 1
            if s[i + k - 1] in vowels:
                curVow += 1
            maxVow = max(curVow, maxVow)
        return maxVow

print(Solution().maxVowels("leetcode", 3))