class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Connected, no cycles, edges = nodes - 1
        # Time: O(V + E)
        # Space: O(V + E)
        #
        # Create adjacency list
        # Traverse with DFS
        # If all nodes visited len(visited) == len(nodes)
        # and no node visited twice, it is a tree

        if len(edges) == 0:
            return n <= 1

        adjacencyList = {}
        for edge in edges:
            if edge[0] not in adjacencyList:
                adjacencyList[edge[0]] = set()
            if edge[1] not in adjacencyList:
                adjacencyList[edge[1]] = set()
            
            adjacencyList[edge[0]].add(edge[1])
            adjacencyList[edge[1]].add(edge[0])
        

        visitedNodes = set()
        visitedEdges = set()

        def dfs(node: int):
            # visit again
            if node in visitedNodes:
                return False
            # No edges
            if node not in adjacencyList:
                return True
                
            visitedNodes.add(node)

            neighs = adjacencyList[node]
            for neigh in neighs:
                # Do not visit same edges again
                if (node, neigh) in visitedEdges or (neigh, node) in visitedEdges:
                    continue

                visitedEdges.add((node, neigh))
                isTree = dfs(neigh)
                if not isTree:
                    return False

            return True

        return dfs(0) and len(visitedNodes) == n



        