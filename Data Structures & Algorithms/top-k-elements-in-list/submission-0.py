import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for n in nums:
            h[n] = h.get(n, 0) + 1
        pq = []
        for n in h:
            heapq.heappush(pq, (h[n], n))
            if len(pq) > k:
                heapq.heappop(pq)
        res = []
        for i in range(k):
            _, n = heapq.heappop(pq)
            res.append(n)
        return res

        # O(nlgk) time
            # O(1) hash insert for each of n nums --> O(n)
            # O(lgk) heap push for each of n nums --> O(nlgk)
            # O(lgk) heap pop for each of k heap elems --> O(klgk)
        # O(n + k) space
            # O(n) for hash map
            # O(k) for pq

'''
# Better bucket sort:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for n in nums:
            h[n] = h.get(n, 0) + 1
        b = [[] for _ in range(len(nums) + 1)]
        for k in h:
            b[h[k]].append(k)
        res = []
        for i in range(n, 0, -1):
            if len(res) >= k:
                return res
            for n in b[i]:
                res.append(n)
        return res

        # O(n) time
            # O(1) hash insert for each of n nums --> O(n)
            # O(1) append for each of n nums --> O(n)
            # O(1) append for each of k elems --> O(k)
        # O(n) space
            # O(n) for hash map
            # O(n) for buckets
'''