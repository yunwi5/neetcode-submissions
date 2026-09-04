class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for i, digit in enumerate(digits):
            number += digit * 10**(len(digits) - i -1)
        
        number += 1
        
        result = []
        for c in str(number):
            result.append(int(c))
        
        return result
        