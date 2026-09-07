class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for r in range(len(board)):
            for c in range(len(board[0])):
                e = board[r][c]
                if e == ".":
                    continue
                i = (r//3)*3+(c//3)
                if e in row[r] or e in col[c] or e in box[i]:
                    return False
                row[r].add(e)
                col[c].add(e)
                box[i].add(e)
        return True

        # O(1) time because constant sized board
        # O(1) space because constant sized board, therefore constant arrays and sets

        # Notes:
            # Can't do [[]] * 9 because all 9 lists will be same reference
            # Use hash set (set()), slightly faster than list
                