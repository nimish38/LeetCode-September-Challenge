class Solution:
    def romanToInt(self, s: str) -> int:
        conversions = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        count, last = 0, float('inf')
        for i in range(len(s)):
            val = conversions[s[i]]
            count += val
            if last < val:
                count -= 2 * last
            last = val
        return count

print(Solution().romanToInt(s = "MCMXCIV"))