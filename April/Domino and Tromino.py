class Solution:

    ## Formula derived is F(n) = 2*F(n-1) + F(n-3)
    ## Check derivation in codestorywithmik video

    def numTilings(self, n: int) -> int:
        def solve(n):
            if n == 1 or n == 2:
                return n
            if n == 3:
                return 5
            if memoi[n] == -1:
                memoi[n] = (2 * solve(n - 1)) + solve(n - 3)
            return memoi[n]

        memoi = [-1]*(n+1)
        return solve(n) % 1000000007

print(Solution().numTilings(100))