class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        edgeBfsQ = deque()

        for rowIndex, row in enumerate(board):
            for colIndex, cell in enumerate(row):
                isEdge = rowIndex == 0 or rowIndex == ROWS - 1 or colIndex == 0 or colIndex == COLS - 1
                if cell == 'O' and isEdge:
                    edgeBfsQ.append((rowIndex, colIndex))
        

        def addToQueueIfRegion(row: int, col: int):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return
            
            if board[row][col] == 'X':
                return
            
            if (row, col) in boundaryRegionSet:
                return
            
            edgeBfsQ.append((row, col))


        boundaryRegionSet = set()

        while edgeBfsQ:
            for i in range(len(edgeBfsQ)):
                row, col = edgeBfsQ.popleft()
                boundaryRegionSet.add((row, col))
                addToQueueIfRegion(row+1,col)
                addToQueueIfRegion(row,col+1)
                addToQueueIfRegion(row-1,col)
                addToQueueIfRegion(row,col-1)
        

        for rowIndex in range(ROWS):
            for colIndex in range(COLS):
                if board[rowIndex][colIndex] == 'O' and (rowIndex, colIndex) not in boundaryRegionSet:
                    board[rowIndex][colIndex] = 'X'


        