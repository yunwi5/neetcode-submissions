class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Time: O(m * 4^n))
        # Space: O(n)
        # m = number of cells, n = length of word
        ROWS = len(board)
        COLS = len(board[0])

        def search(row: int, col: int, index: int, visit: set):
            if board[row][col] != word[index]: return False
            if index == len(word) - 1: return True
            
            visit.add((row, col))
            deltas = [
                (1, 0),
                (0, 1),
                (-1, 0),
                (0, -1),
            ]

            for (dRow, dCol) in deltas:
                newRow, newCol = row + dRow, col + dCol
                if newRow < 0 or newRow >= ROWS:
                    continue
                if newCol < 0 or newCol >= COLS:
                    continue
                if (newRow, newCol) in visit:
                    continue
                
                worked = search(newRow, newCol, index + 1, visit.copy())
                if worked:
                    return True
            
            return False


        for rowIndex, row in enumerate(board):
            for colIndex, cell in enumerate(row):
                found = search(rowIndex, colIndex, 0, set()) 
                if found:
                    return True
        
        return False