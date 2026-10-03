class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Time: O(m*m*n)
        # Space: O(m*n)
        adjList = defaultdict(list)
        visitList = [beginWord]
        for i, word in enumerate(wordList):
            for existing in visitList:
                diffCount = 0
                for c1, c2 in zip(existing, word):
                    if c1 != c2:
                        diffCount += 1
                
                if diffCount == 1:
                    adjList[existing].append(word)
                    adjList[word].append(existing)
                
            visitList.append(word)
        
        visit = set()
        q = collections.deque([beginWord])
        sequence = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                visit.add(word)
                if word == endWord:
                    return sequence
                
                for neigh in adjList[word]:
                    if neigh not in visit:
                        q.append(neigh)

            sequence += 1


        return 0