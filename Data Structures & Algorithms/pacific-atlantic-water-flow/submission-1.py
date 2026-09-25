class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Multi source BFS
        # for first rows and cols, run multi source BFS
        # If cell <= neigh, add neigh to the pacific result
        # Else cannot flow so ignore
        # Add to visit set
        #
        # for last rows and cols, rum multi source BFS
        # If cell <= neigh, add neigh to atlantic result
        # Else cannot flow skip
        # Add to visit set
        #
        # Time: O(n*m)
        # Space: O(n*m)

        rows = len(heights)
        cols = len(heights[0])

        pacificFlowQueue = deque()
        atlanticFlowQueue = deque()

        for row in range(len(heights)):
            for col in range(len(heights[row])):
                if row == 0 or col == 0:
                    pacificFlowQueue.append((row, col))
                if row == rows - 1 or col == cols - 1:
                    atlanticFlowQueue.append((row, col))

        def exploreNeighbours(flowQueue, flowSet):
            visit = set()
            
            def exploreNeighbour(row: int, col: int, prev: int):
                if row < 0 or row >= rows or col < 0 or col >= cols:
                    return
                if (row, col) in visit:
                    return
                if heights[row][col] < prev:
                    return
                
                visit.add((row, col))
                flowQueue.append((row, col))

            while flowQueue:
                for i in range(len(flowQueue)):
                    row, col = flowQueue.popleft()
                    flowSet.add((row, col))
                    exploreNeighbour(row+1, col, heights[row][col])
                    exploreNeighbour(row, col+1, heights[row][col])
                    exploreNeighbour(row-1, col, heights[row][col])
                    exploreNeighbour(row, col-1, heights[row][col])


        pacificFlowSet = set()
        exploreNeighbours(pacificFlowQueue, pacificFlowSet)

        atlanticFlowSet = set()
        exploreNeighbours(atlanticFlowQueue, atlanticFlowSet)

        return [list(pair) for pair in pacificFlowSet.intersection(atlanticFlowSet)]


        