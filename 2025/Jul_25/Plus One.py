class Solution(object):
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + carry < 10:
                digits[i] = digits[i] + 1
                return digits
            digits[i] = 0
        if carry:
            digits.insert(0, 1)
        return digits

print(Solution().plusOne(digits = [9., 9]))