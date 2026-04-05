from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # a: the distance between the starting point and the start of the circle
        # b: the distance that the tortoise ran in the circle
        # c: the distance between the starting point of the circle and the position of the tortoise
        #
        # The distance the tortoise ran: "a + b"
        # The distance the hare ran: "a + b + (c + b)" (add c + b because the hare runs twice as fast as the tortoise)
        #
        # Then:
        # distance(hare) = 2 * distance(tortoise)
        # a + b + (c + b) = 2 * (a + b)
        # a + 2b + c = 2a + 2b
        # a = c
        #
        # Therefore, after finding the meeting point, we need to move an additional `a` steps
        # to reach the start of the circle.

        # Phase 1: find an intersection point inside the cycle
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: move one pointer from start; they meet at the cycle start (the duplicate)
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow
