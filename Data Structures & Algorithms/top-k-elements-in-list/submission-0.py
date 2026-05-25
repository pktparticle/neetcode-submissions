from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntr = Counter(nums)
        sorted_cntr = sorted(cntr.items(), key = lambda x:x[1], reverse = True)
        return [key for key, val in sorted_cntr[:k]]