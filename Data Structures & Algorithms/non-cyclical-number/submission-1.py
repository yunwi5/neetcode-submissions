class Solution:
    def isHappy(self, n: int) -> bool:

        def calculateSumSquares(num):
            digits = str(num)
            output = 0
            for digit in digits:
                output += int(digit) ** 2
            
            return output
        
        seen = set()

        while True:
            n = calculateSumSquares(n)
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
        
        return False
            
        