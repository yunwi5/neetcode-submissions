class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time: O(m)
        # Space: O(1)
        # 
        # freq dict = count of task X
        # heap = Min heap of size n + 1
        # heappush task X with weight the number of frequencies.
        # 
        # t = total time taken (from 0)
        # In every cycle, heappop task X with highest count in heap.
        # After cycle, subtract 1 for those tasks in freq dict.
        # When dict size is 0, return total time t

        freqDict = {}
        for task in tasks:
            if task not in freqDict:
                freqDict[task] = 0
            freqDict[task] += 1
        
        total = 0
        while freqDict:
            maxHeap = []
            for task, freq in freqDict.items():
                heapq.heappush(maxHeap, (-freq, task))

            heapSize = len(maxHeap)
            for i in range(n + 1):
                if not maxHeap:
                    break
                # Highest count task in the heap at iteration i
                _, task = heapq.heappop(maxHeap)
                freqDict[task] -= 1
                if freqDict[task] < 1:
                    del freqDict[task]

            if not freqDict:
                total += heapSize
                break
            total += (n + 1)

        return total
