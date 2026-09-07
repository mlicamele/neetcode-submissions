class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            curr_end = intervals[i][1]
            curr_start = intervals[i][0]
            if curr_start < end:
                end = min(end, curr_end)
                count += 1
            else:
                end = curr_end
        return count
            
