class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            # row check
            dic = {}
            for col in range(9):
                ele = board[row][col]
                if ele == '.':
                    continue
                dic[ele] = dic.get(ele, 0) + 1
            for freq in dic.values():
                if freq > 1:
                    return False
            # column check
            dic.clear()
            for col in range(9):
                ele = board[col][row]
                if ele == '.':
                    continue
                dic[ele] = dic.get(ele, 0) + 1
            for freq in dic.values():
                if freq > 1:
                    return False
            # square check
            for col in range(9):
                if not (row % 3 == 0 and col % 3 == 0):
                    continue
                dic.clear()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        ele = board[i][j]
                        if ele == '.':
                            continue
                        dic[ele] = dic.get(ele, 0) + 1
                for freq in dic.values():
                    if freq > 1:
                        return False

        return True