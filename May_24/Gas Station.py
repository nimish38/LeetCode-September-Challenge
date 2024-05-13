class Solution:
    def canCompleteCircuit(self, gas, cost):
        def checkcircuit(ind):
            tank, n = gas[ind] - cost[ind], len(gas)
            curr = (ind + 1) % n
            while curr != ind:
                tank += gas[curr] - cost[curr]
                if tank < 0:
                    return False
                curr = (curr + 1) % n
            if tank >= 0:
                return True
            return False

        for i in range(len(gas)):
            if gas[i] > cost[i]:
                if checkcircuit(i):
                    return i
        return -1

print(Solution().canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))