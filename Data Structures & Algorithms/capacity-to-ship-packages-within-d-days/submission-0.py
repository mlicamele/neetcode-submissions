class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        c = 1
        while True:
            count = 1
            curr = 0
            for i in range(len(weights)):
                if weights[i] > c:
                    count = days + 1
                    break
                if curr + weights[i] > c:
                    curr = weights[i]
                    count += 1
                else:
                    curr += weights[i]
            if count <= days:
                break
            c *= 2
        l = c//2 + 1
        r = c
        while l < r:
            mid = (l + r)//2
            count = 1
            curr = 0
            for i in range(len(weights)):
                if weights[i] > mid:
                    count = days + 1
                    break
                if curr + weights[i] > mid:
                    curr = weights[i]
                    count += 1
                else:
                    curr += weights[i]
            if count <= days:
                r = mid
            else:
                l = mid + 1
        return l
        