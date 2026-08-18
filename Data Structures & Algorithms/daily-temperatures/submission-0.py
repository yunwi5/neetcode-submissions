class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(n)

        output = [0] * len(temperatures)
        stack = []
        for index in range(len(temperatures)-1,-1,-1):
            temp = temperatures[index]
            if stack == []:
                stack.append((index, temp))
                output[index] = 0
                continue

            lastIndex, lastTemp = stack[-1]
            while stack and temp >= stack[-1][1]:
                stack.pop()
                if stack:
                    lastIndex, lastTemp = stack[-1]
            
            if temp < lastTemp:
                output[index] = lastIndex - index
            
            stack.append((index, temp))

        
        return output

                



        