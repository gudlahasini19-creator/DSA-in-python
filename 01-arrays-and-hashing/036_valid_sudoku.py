import collections
class Solution(object):
    def isValidSudoku(self, board):
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)  # key: (row // 3, col // 3)
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                    
                box_idx = (r // 3, c // 3)
                
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[box_idx]):
                    return False
                    
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        return True
