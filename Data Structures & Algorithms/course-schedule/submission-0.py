class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegreeDict = {}
        adjList = {}

        for pair in prerequisites:
            course, pre = pair[0], pair[1]
            
            # pre -> course
            if pre not in adjList:
                adjList[pre] = set()
            adjList[pre].add(course)

            # indegree dict update
            if course not in indegreeDict:
                indegreeDict[course] = 0
            indegreeDict[course] += 1


        q = deque()
        for i in range(numCourses):
            if i not in indegreeDict:
                q.append(i)
        

        result = []

        while q:
            for i in range(len(q)):
                node = q.popleft()
                result.append(node)

                if node not in adjList:
                    continue

                adjacents = adjList[node]
                for adjacent in adjacents:
                    indegreeDict[adjacent] -= 1
                
                    if indegreeDict[adjacent] == 0:
                        q.append(adjacent)
        

        return len(result) == numCourses



            

        