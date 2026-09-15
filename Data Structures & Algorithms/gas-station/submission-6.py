class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        s = [g - c for g, c in zip(gas, cost)]
        total = 0
        res = 0
        for j in range(len(s)):
            total += s[j]
            if total < 0:
                total = 0
                res = j + 1
        return res
        