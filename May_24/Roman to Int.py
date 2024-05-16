class Solution:
    def romanToInt(self, s: str) -> int:
        conversions = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        exceptions = {'IV': 2, 'IX': 2, 'XL': 20, 'XC': 20, 'CD': 200, 'CM': 200}

        count, last = 0, '*'
        for i in range(len(s)):
            count += conversions[s[i]]
            if last + s[i] in exceptions:
                count -= exceptions[last + s[i]]
            last = s[i]
        return count

print(Solution().romanToInt(s = "LVIII"))