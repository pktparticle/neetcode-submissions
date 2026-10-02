class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible_to_finish_with_speed(speed: int) -> bool:
            time = 0
            for p in piles:
                time += math.ceil(p/speed)
            return time <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right-left)//2 
            if feasible_to_finish_with_speed(mid):
                right = mid
            else:
                left = mid+1
        return left