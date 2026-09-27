class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        forward, backward, product = [1]*n, [1]*n, [1]*n
        forward[0]=nums[0]
        backward[n-1]=nums[n-1]
        for i in range(1,n):
            forward[i]=nums[i]*forward[i-1]
        for i in range(n-2, -1, -1):
            backward[i]=nums[i]*backward[i+1]
        product[0]=backward[1]
        product[n-1]=forward[n-2]
        for i in range(1,n-1):
            product[i]=forward[i-1]*backward[i+1]
        return product