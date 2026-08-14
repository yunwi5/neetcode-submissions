from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        starting map: key: start, value: (start, end)
        ending map: key: end, value: (start, end)    

        (1, 2)
        3
        (4, 6)

        (1, 6)
        """

        if nums == []:
            return 0

        startingMap = defaultdict(list) 
        endingMap = defaultdict(list) 

        for num in nums:
            if endingMap[num] != []:
                continue
            preNode = endingMap[num - 1]
            postNode = startingMap[num + 1]

            newNode = (num, num)
            if preNode != []:
                newNode = (preNode[0], newNode[1])
            if postNode != []:
                newNode = (newNode[0], postNode[1])

            # print("newNode:", newNode)
            startingMap[newNode[0]] = newNode
            endingMap[newNode[1]] = newNode
        
        # print("startingMap:", startingMap)

        longest = 1
        for node in startingMap.values():
            if len(node) == 0:
                continue
            longest = max(longest, node[1] - node[0] + 1)

        return longest


            









        