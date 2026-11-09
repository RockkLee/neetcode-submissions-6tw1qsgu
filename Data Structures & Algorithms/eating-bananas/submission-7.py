class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_hours(speed: int):
            summ = 0
            for p in piles:
                if p < speed:
                    summ += 1
                    continue
                summ += (p // speed) + (1 if p % speed > 0 else 0)
            return summ
        
        max_speed = max(piles)
        min_speed = max_speed
        l, r = 1, max_speed
        while l <= r:
            mid = int((l + r) / 2)
            hours = get_hours(mid)
            if h >= hours:
                min_speed = mid
                r = mid - 1
            else:
                l = mid + 1
        return min_speed
            
