class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time: O(n)
        # Space: O(1)

        # Hash map of key: char, value: frequency
        # Track the char with highest frequency right now
        # Track max length so far and never reduce that window.
        

        charMap = defaultdict(int)
        windowSize = 0
        maxCharFreq, maxFreqChar = 0, None
        for index in range(len(s)):
            char = s[index]
            charMap[char] += 1
            if charMap[char] > maxCharFreq:
                maxCharFreq = max(maxCharFreq, charMap[char])
                maxFreqChar = char

            otherCharCount = 0
            for mapChar, frequency in charMap.items():
                if mapChar != maxFreqChar:
                    otherCharCount += frequency

            if otherCharCount > k:
                # Shift window, move on. 
                charToRemove = s[index - windowSize]
                charMap[charToRemove] -= 1
                continue
            
            windowSize += 1

        
        return windowSize



            