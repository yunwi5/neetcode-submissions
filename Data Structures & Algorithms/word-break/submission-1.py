class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        invalidIndexCache = defaultdict(bool)

        def dfs(index: int) -> True:
            if index >= len(s):
                return True
            if invalidIndexCache[index]:
                return False

            for word in wordDict:
                if index+len(word) > len(s):
                    continue
                if s[index:index+len(word)] == word:
                    furtherMatch = dfs(index+len(word))
                    if furtherMatch:
                        return True

            invalidIndexCache[index] = True

            return False


        return dfs(0)