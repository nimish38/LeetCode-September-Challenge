class Solution:

    ## Formula derived is F(n) = 2*F(n-1) + F(n-3)
    ## Check derivation in codestorywithmik video

    def numTilings(self, n: int) -> int:
        def solve(n):
            if n == 1 or n == 2:
                return n
            if n == 3:
                return 5
            return (2 * solve(n - 1)) + solve(n - 3)
        return solve(n)

print(Solution().numTilings(4))