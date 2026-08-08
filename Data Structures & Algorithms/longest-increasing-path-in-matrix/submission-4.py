class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        mm = len(matrix)
        nn = len(matrix[0])

        memo = [[0] * nn for _ in range(mm)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(m: int, n: int) -> int:
            if memo[m][n] != 0:
                return memo[m][n]

            memo[m][n] = 1

            for dm, dn in directions:
                nxtm = m + dm
                nxtn = n + dn

                if (
                        0 <= nxtm < mm
                        and 0 <= nxtn < nn
                        and matrix[nxtm][nxtn] > matrix[m][n]
                ):
                    memo[m][n] = max(
                        memo[m][n],
                        1 + dfs(nxtm, nxtn)
                    )

            return memo[m][n]

        return max(
            dfs(m, n)
            for m in range(mm)
            for n in range(nn)
        )
