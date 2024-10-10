class Solution:
    def plusOne(self, digits):
        i, carry = len(digits) - 1, False
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
            carry = True
            i -= 1
            while i >= 0 and carry:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = False
                i -= 1
            if carry:
                digits = [1] + digits
            return digits

print(Solution().plusOne(digits=[1,2,3,9,9]))