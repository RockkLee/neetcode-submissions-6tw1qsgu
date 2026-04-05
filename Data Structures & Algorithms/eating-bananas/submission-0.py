class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # target: maximum hours to eat bananas, but the value still need to less than `h`
        def cal_hours(speed: int) -> int:
            hr = 0
            for _, pile in enumerate(piles):
                if pile < speed:
                    hr += 1
                else:
                    hr += math.ceil(pile / speed)
            return hr

        # speed of eating all bananas
        speed_l = 1
        speed_r = max(piles)
        ans = speed_r
        while speed_l <= speed_r:
            speed_m = (speed_l + speed_r) // 2
            hrs = cal_hours(speed_m)
            if hrs <= h:
                ans = speed_m
                speed_r = speed_m - 1  # Decrease the speed to get the max hrs
            else:
                speed_l = speed_m + 1  # Increase the speed to make hrs less than `h`
        return ans
