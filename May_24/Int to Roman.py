class Solution:
    def intToRoman(self, num: int) -> str:
        res, j = '', 0
        conversions = {'M': 1000, 'C': 100, 'X': 10, 'I': 1}
        exceptions = ['D', 'L', 'V']
        conv = list(conversions.keys())
        for i in range(3):
            char = conv[i]
            val = conversions[char]
            count = num // val
            num %= val
            res += char * count

            cond = val / 10
            if num >= 9 * cond:
                res += conv[i + 1] + conv[i]
                num -= 9 * cond

            if num >= 5 * cond:
                res += exceptions[j]
                num -= 5 * cond

            if num >= 4 * cond:
                res += conv[i + 1] + exceptions[j]
                num -= 4 * cond

            j += 1
        res += 'I' * num
        return res



        # m_count = num // 1000
        # num = num % 1000
        # res += 'M' * m_count
        #
        # if num >= 900:
        #     res += 'CM'
        #     num -= 900
        #
        # if num >= 500:
        #     res += 'D'
        #     num -= 500
        #
        # if num >= 400:
        #     res += 'CD'
        #     num -= 400
        #
        # c_count = num // 100
        # num %= 100
        # res += 'C' * c_count
        #
        # if num >= 90:
        #     res += 'XC'
        #     num -= 90
        #
        # if num >= 50:
        #     res += 'L'
        #     num -= 50
        #
        # if num >= 40:
        #     res += 'XL'
        #     num -= 40
        #
        # x_count = num // 10
        # num %= 10
        # res += 'X' * x_count
        #
        # if num >= 9:
        #     res += 'IX'
        #     num -= 9
        #
        # if num >= 5:
        #     res += 'V'
        #     num -= 5
        #
        # if num >= 4:
        #     res += 'IV'
        #     num -= 4
        #
        # res += 'I' * num
        # return res

print(Solution().intToRoman(3749))





