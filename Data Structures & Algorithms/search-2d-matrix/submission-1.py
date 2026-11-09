# [
#  [0, 1, 2, 3],
#  [4, 5, 6, 7],
#  [8, 9,10,11]
# ]

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # n x m
        n, m = len(matrix), len(matrix[0])
        l, r = 0, (n * m) - 1

        while l <= r:
            mid = int((l + r) / 2)
            nn, mm = int(mid / m), mid % m
            val = matrix[nn][mm]
            if target > val:
                l = mid + 1
            elif target < val:
                r = mid - 1
            else:
                return True
        return False