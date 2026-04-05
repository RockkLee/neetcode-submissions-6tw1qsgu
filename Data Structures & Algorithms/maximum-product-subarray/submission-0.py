class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [(0, 0)] * (n + 1)
        ans = nums[0]
        for idx in range(1, n + 1):
            # take pre_max & cur
            pre_max_cur = dp[idx - 1][0] * nums[idx - 1]
            # take pre_min & cur
            pre_min_cur = dp[idx - 1][1] * nums[idx - 1]
            # take cur (discard pre_max & pre_min)
            cur = nums[idx - 1]

            maxx = max(pre_max_cur, pre_min_cur, cur)
            minn = min(pre_max_cur, pre_min_cur, cur)
            # dp[idx]: store the max and min values that contains the current value (nums[idx - 1])
            dp[idx] = (maxx, minn)
            # ans: compare the max value which contains the current value to the previous max value, which is ans itself,
            #      which can cover the missing logic that the previous longest substring might not be adjacent to the cur idx 
            ans = max(ans, maxx)
        return ans
