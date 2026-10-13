class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        def backtrack(index: int) -> int:
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            if index == len(s) - 1:
                return 1
            if index in cache:
                return cache[index]
            
            count = 0
            # Two digits form one letter            
            if int(s[index]+s[index+1]) <= 26:
                count += backtrack(index + 2)

            # One digit to one letter
            count += backtrack(index + 1)

            cache[index] = count

            return count

        
        return backtrack(0)
        