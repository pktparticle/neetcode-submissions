class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0]<=end:
                end = max(end, intervals[i][1])
            else:
                res.append([start, end])
                start, end = intervals[i]
        res.append([start, end])
        return res