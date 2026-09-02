class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time: O(m)
        # Space: O(1)
        freqDict = collections.Counter(tasks)

        total = 0
        while freqDict:
            maxHeap = []
            for task, freq in freqDict.items():
                heapq.heappush(maxHeap, (-freq, task))

            # Time: O(26) = O(1)
            heapSize = len(maxHeap)
            for i in range(min(heapSize, n + 1)):
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
