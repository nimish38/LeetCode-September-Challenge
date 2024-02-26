class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # store passesnger amount in car at ith pos   
        cap = [0]*1002
        start_min = 100000
        end_max = -1
        
        for trip in trips:
            # store start and end pos of car
            if start_min > trip[1]:
                start_min = trip[1]
            if end_max < trip[2]:
                end_max = trip[2]
            # update passenger list     
            for i in range(trip[1], trip[2]):
                cap[i] += trip[0]
        # passenger > capacity return false        
        for i in range(start_min, end_max+1):
            if cap[i] > capacity:
                return False
        return True    