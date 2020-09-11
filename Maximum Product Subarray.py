class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # get local max and min at each step to hand - * - = + cases
        localMax = nums[0]
        localMin = nums[0]
        maxProd = nums[0]
        
        for i in range(1, len(nums)):
            
            if nums[i] > 0:
                # store local maxima by multiplying current no by local maxima 
                localMax = max(localMax * nums[i], nums[i])
                # store local minima 
                localMin = min(localMin * nums[i], nums[i])
                
            else:
                # if current no is -ve, get local maxima by product of localminima(maybe -ve) by current no(-ve)
                # store in temp var so as to calculate local minima in next step by previous local maxima 
                temp_localMax = max(localMin * nums[i], nums[i])
                localMin = min(localMax * nums[i], nums[i])
                # assign local maxima 
                localMax = temp_localMax
            # get maximum of local man=xima at each step    
            maxProd = max(localMax, maxProd)  
            
            #print(localMax, localMin)    

        return maxProd     