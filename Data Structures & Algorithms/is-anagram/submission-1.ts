class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        const sCharCountMap = new Map<string, number>();
        const tCharCountMap = new Map<string, number>();

        for (let char of s) {
            if (sCharCountMap.has(char)) {
                sCharCountMap.set(char, sCharCountMap.get(char) + 1)
            } else {
                sCharCountMap.set(char, 1);
            }
        }

        for (let char of t) {
            if (tCharCountMap.has(char)) {
                tCharCountMap.set(char, tCharCountMap.get(char) + 1)
            } else {
                tCharCountMap.set(char, 1);
            }
        }

        if (sCharCountMap.size != tCharCountMap.size) {
            return false;
        }

        for (const [char, count] of sCharCountMap.entries()) {
            if (!tCharCountMap.has(char) || tCharCountMap.get(char) != count) {
                return false;
            }
        }

        return true;
    }
}
