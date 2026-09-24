class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}
        indegreeDict = defaultdict(int)

        for course, preCourse in prerequisites:
            if preCourse not in adjList:
                adjList[preCourse] = set()
            adjList[preCourse].add(course)

            indegreeDict[course] += 1
        

        bfsQueue = deque()
        for course in range(numCourses):
            if indegreeDict[course] == 0:
                bfsQueue.append(course)

        
        order = []

        while bfsQueue:
            for i in range(len(bfsQueue)):
                course = bfsQueue.popleft()
                order.append(course)

                if course not in adjList:
                    continue

                neighs = adjList[course]
                for neigh in neighs:
                    indegreeDict[neigh] -= 1
                    if indegreeDict[neigh] == 0:
                        bfsQueue.append(neigh)
        
        return [] if len(order) < numCourses else order