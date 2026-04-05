class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_speed = max(piles)
        min_speed = max_speed
        l, r = 1, max_speed

        def get_hours(speed: int) -> int:
            hr = 0
            for p in piles:
                if p < speed:
                    hr += 1
                else:
                    hr += (p // speed) + (1 if p % speed > 0 else 0)
            return hr

        while l <= r:
            mid = (l + r) // 2
            hr = get_hours(mid)
            if hr > h:
                l = mid + 1
            else:
                r = mid - 1
                min_speed = mid
        return min_speed
