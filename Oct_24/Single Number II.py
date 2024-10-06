class Solution:
    def singleNumber(self, nums) -> int:

        def twos_complement(j):
            return j - (1 << (j.bit_length()))

        # Left shift by two bits: x << 2 - is similar to multiply by 4
        # check if kth bit is 0 or 1: (1 << k) && num - first right shift 1 by k bits then and it with the number
        # make kth bit as 1 : (1 << k) || num - first right shift 1 by k bits then or it with number

        res = 0
        for k in range(0, 32):
            curr, cntOne = 1 << k, 0
            for num in nums:
                if curr & num:
                    cntOne += 1
            if cntOne % 3:
                res = res | curr
        if res not in nums:
            return twos_complement(res)
        return res


print(Solution().singleNumber(nums = [-2,-2,1,1,4,1,4,4,-4,-2]))