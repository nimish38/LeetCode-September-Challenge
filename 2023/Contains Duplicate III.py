class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k<=0 or t<0:
            return False
        bucket = {}
        window = t+1
    
        for ind, elem in enumerate(nums):
            val = elem // window
            
            # if already present in same bucket
            if val in bucket:
                return True
            else:
                bucket[val] = elem
                # if present in adjacent bucket satisfying condition
                if val - 1 in bucket and elem - bucket[val-1] <= t:
                    return True
                if val + 1 in bucket and bucket[val+1] - elem <= t:
                    return True
                # increment the window and remove first elemnet from bucket
                if ind >= k:
                    del bucket[nums[ind-k] // window]
        return False
            
            
                  
        