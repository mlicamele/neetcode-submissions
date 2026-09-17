class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        m = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > m:
                res.insert(0, i)
                m = heights[i]
        return res