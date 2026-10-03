class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        n=len(intervals)
        i=0
        res = []
        start, end = newInterval
        while i<n and intervals[i][1]<newInterval[0]:
            res.append(intervals[i])
            i+=1
        while i<n and intervals[i][0]<=newInterval[1]:
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            i+=1
        res.append([start, end])
        while i<n:
            res.append(intervals[i])
            i+=1
        return res