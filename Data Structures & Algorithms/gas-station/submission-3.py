class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        total = 0
        ans = 0
        for i in range(n):
            if total == 0:
                ans = i
            total += gas[i] - cost[i]
            if total < 0:
                total = 0

        return ans