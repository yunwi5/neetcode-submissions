class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        costDict = {}
        adjList = {}

        for node in range(1, n+1):
            costDict[node] = math.inf
        costDict[k] = 0

        for startNode, endNode, cost in times:
            if startNode not in adjList:
                adjList[startNode] = []
            adjList[startNode].append((cost, endNode))

        visit = set()
        minHeap = [(0, k)]

        while minHeap:
            nodeCost, node = heapq.heappop(minHeap)
            if node in visit:
                continue

            visit.add(node)
            if node in adjList:
                neighs = adjList[node]
                for neighCost, neigh in neighs:
                    if nodeCost + neighCost < costDict[neigh]:
                        costDict[neigh] = nodeCost + neighCost
                        heapq.heappush(minHeap, (costDict[neigh], neigh))

        maxCost = max(costDict.values())
        
        return -1 if maxCost == math.inf else maxCost
