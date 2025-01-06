class Solution:

    ## Formula derived is F(n) = 2*F(n-1) + F(n-3)
    ## Check derivation in codestorywithmik video

    def numTilings(self, n: int) -> int:
        if n==1 or n==2:
            return n
        memoi = [-1]*(n+1)
        memoi[0], memoi[1], memoi[2], memoi[3] = 0, 1, 2, 5

        for i in range(4, n+1):
            memoi[i] = (2*memoi[i-1]) + memoi[i-3]

        return memoi[n] % 1000000007

print(Solution().numTilings(100))