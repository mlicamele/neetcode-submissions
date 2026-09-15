class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        res = 0
        for j in range(len(gas)):
            total += gas[j] - cost[j]
            if total < 0:
                total = 0
                res = j + 1
        return res
        