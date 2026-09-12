class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 1. Keep open & close count in recursion
        # 2. validate paranthesis
        # 3. Make sure same number of ( and ) AND no more ) than ( at any poiny

        # Time: O(4^n / sqrt(n)) Why? 
        # Space: O(n)

        result = []

        def backtrack(series: List[str], opened: int, closed: int):
            if len(series) == n * 2:
                result.append(''.join(series))
                return
            
            # Scenario 1: Add (
            if opened < n:
                series.append('(')
                backtrack(series, opened + 1, closed)
                series.pop()

            # Scenario 2: Add )
            if opened > closed:
                series.append(')')
                backtrack(series, opened, closed + 1)
                series.pop()
    
        backtrack([], 0, 0)

        return result
        