class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triplets = set()
        for i in range(n):
            target = -nums[i]
            d = {}
            for j in range(i+1, n):
                if target-nums[j] in d:
                    triplet = sorted([nums[d[target-nums[j]]], nums[j], nums[i]])
                    triplets.add(tuple(triplet))
                else:
                    d[nums[j]]=j
        return list(triplets)