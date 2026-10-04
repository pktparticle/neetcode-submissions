from heapq import heappush, heappop
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        d = {}
        i = 0
        n = len(intervals)
        for q in sorted(queries):
            while i<n and intervals[i][0]<=q:
                heappush(minHeap, (1+intervals[i][1]-intervals[i][0], intervals[i][1]))
                i+=1
            while minHeap and minHeap[0][1]<q:
                heappop(minHeap)
            res = minHeap[0][0] if minHeap else -1
            d[q]=res
        return [d[q] for q in queries]