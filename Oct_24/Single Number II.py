class Solution:
    def singleNumber(self, nums) -> int:

        # Left shift by two bits: x << 2 - is similar to multiply by 4
        # check if kth bit is 0 or 1: (1 << k) && num - first right shift 1 by k bits then and it with the number
        # make kth bit as 1 : (1 << k) || num - first right shift 1 by k bits then or it with number

        res = 0
        for k in range(0, 32):
            curr, cntOne, cntZer = 1 << k, 0, 0
            for num in nums:
                if curr & num == 0:
                    cntZer += 1
                else:
                    cntOne += 1
            if cntOne % 3:
                res = res | curr
        return res


print(Solution().singleNumber(nums = [0,1,0,1,0,1,99]))