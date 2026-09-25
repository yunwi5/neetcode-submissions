class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union-Find
        # Time: O(V + E)
        # Space: O(V)

        n = 0
        for n1, n2 in edges:
            n = max(n, n1, n2)

        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(node):
            res = node

            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            
            return res
        
        def unionDetectCycle(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return True

            if rank[p1] < rank[p2]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]

            return False

        for n1, n2 in edges:
            if unionDetectCycle(n1, n2):
                return [n1, n2]


