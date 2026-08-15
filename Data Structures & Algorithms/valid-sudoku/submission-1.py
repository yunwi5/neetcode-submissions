import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        gridSeenDict = {}
        rowSeenDict = {}
        colSeenDict = {}

        for i, row in enumerate(board):
            if i not in rowSeenDict:
                rowSeenDict[i] = set()
            for j, num in enumerate(row):
                if j not in colSeenDict:
                    colSeenDict[j] = set()
                
                if num == '.':
                    continue

                gridRow = math.floor(i/3)
                gridCol = math.floor(j/3)
                gridKey = f"{gridRow}:{gridCol}"

                if gridKey not in gridSeenDict:
                    gridSeenDict[gridKey] = set()
                
                if num in rowSeenDict[i]:
                    return False
                if num in colSeenDict[j]:
                    return False
                if num in gridSeenDict[gridKey]:
                    return False
                
                rowSeenDict[i].add(num)
                colSeenDict[j].add(num)
                gridSeenDict[gridKey].add(num)

        return True

        