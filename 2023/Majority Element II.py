class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        # check unique number in list
        for num in set(nums):
            # if number appers more than n/3 times in list add it to result
            if nums.count(num) > n//3:
                res.append(num)
        return res        
        