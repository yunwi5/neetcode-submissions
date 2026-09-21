class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        # o
        #
        # Use DFS?
        # Time: O(V+E)
        # Space: O(V+E)
        # V = # vertices, E = # edges
    

        connectedComponents = 0
        # Time: O(V)
        # Space: O(V)
        unvisited = {i for i in range(n)}
        adjList = {}

        # Time: O(E)
        # Space: O(E)
        for edge in edges:
            if edge[0] not in adjList:
                adjList[edge[0]] = set()
            if edge[1] not in adjList:
                adjList[edge[1]] = set()

            adjList[edge[0]].add(edge[1])
            adjList[edge[1]].add(edge[0])
        

        # Time: O(V+E)
        # Space: O(V+E)
        def dfs(node: int, component):
            component.add(node)
            if node in unvisited:
                unvisited.remove(node)
            if node not in adjList:
                return 

            neighs = adjList[node]
            for neigh in neighs:
                if neigh in component:
                    continue
                dfs(neigh, component)

        while unvisited:
            node = unvisited.pop()
            connectedComponents += 1
            component = set()
            dfs(node, component)

        return connectedComponents

        

        

        