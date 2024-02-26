class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # cant have unique no.s more than 9
        # max addition of 1 - 9 is 45 
        if k > 9 or n > 45:
            return []
        
        from itertools import combinations
        sol = []
        
        # get all possible combinations of length k, if sum is n add to solution
        for comb in list(combinations([1,2,3,4,5,6,7,8,9],k)):
            if sum(comb) == n:
                sol.append(list(comb))
        return sol        