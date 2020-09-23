class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # If sum of gas is less than sum of cost, then there is no way to get through all stations
        if sum(gas) < sum(cost):
            return -1
        
        # Otherwise, there must be one unique solution, so the first one I find is the right one
        gas_tank, start_index = 0, 0
        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            
            if gas_tank < 0:
                start_index = i+1
                gas_tank = 0
                
        return start_index        
        