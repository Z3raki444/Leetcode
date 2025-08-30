'''https://leetcode.com/problems/valid-sudoku/description/'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # 3x3 sub-boxes

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue  # skip empty cells

                # Find the box index (0 to 8)
                box_index = (r // 3) * 3 + (c // 3)

                # If num already exists in row, column, or box → invalid
                if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                    return False

                # Otherwise, record the number in the sets
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

        return True 