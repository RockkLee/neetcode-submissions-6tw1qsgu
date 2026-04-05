class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m_len = len(matrix)
        n_len = len(matrix[0]) if matrix else 0
        l = 0
        r = m_len * n_len - 1
        while l <= r:
            mid = (l + r) // 2
            # mid
            n_mid = int(mid % n_len)
            m_mid = mid // n_len

            if matrix[m_mid][n_mid] < target:
                l = mid + 1
            elif matrix[m_mid][n_mid] > target:
                r = mid - 1
            elif matrix[m_mid][n_mid] == target:
                return True

        return False
