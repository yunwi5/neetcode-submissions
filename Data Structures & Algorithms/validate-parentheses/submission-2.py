class Solution:
    def isValid(self, s: str) -> bool:
        openingToClosingDict = {
            '(' : ')',
            '{': '}',
            '[': ']',
        }

        stack = []
        for char in s:
            if char in openingToClosingDict:
                stack.append(char)
            else:
                if stack == []:
                    return False
                popped = stack.pop()
                if openingToClosingDict[popped] != char:
                    return False
        
        return stack == []
        