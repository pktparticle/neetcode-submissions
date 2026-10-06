from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))
    
    def _binarySearch(self, arr: list, timestamp:int):
        left, right = 0, len(arr)
        ans = ''
        while left < right:
            mid = left + (right-left)//2
            if arr[mid][1] > timestamp:
                right = mid
            else:
                ans = arr[mid][0]
                left = mid+1
        return ans
        
    def get(self, key: str, timestamp: int) -> str:
        arr = self.timemap[key]
        return self._binarySearch(arr, timestamp)
        
