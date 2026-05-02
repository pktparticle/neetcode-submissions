class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[target-nums[i]] = i
        