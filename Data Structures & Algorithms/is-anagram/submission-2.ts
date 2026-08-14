class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        const sCharCountMap = new Map<string, number>();

        for (let char of s) {
            if (sCharCountMap.has(char)) {
                sCharCountMap.set(char, sCharCountMap.get(char) + 1)
            } else {
                sCharCountMap.set(char, 1);
            }
        }

        for (let char of t) {
            if (sCharCountMap.has(char)) {
                sCharCountMap.set(char, sCharCountMap.get(char) - 1)
            } else {
                return false;
            }
        }


        for (const [char, count] of sCharCountMap.entries()) {
            if (count != 0) {
                return false;
            }
        }

        return true;
    }
}
