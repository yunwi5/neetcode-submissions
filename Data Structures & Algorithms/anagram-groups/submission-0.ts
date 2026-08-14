class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        /**
         * wordMap:
         *  key: hashed str (no ordering), value: list of str 
         * 
         * Define hash fn:
         *  - alphabetIndices = arr[26].fill(0);
         *  - for each char, get charcode and increment the slot at that index
         * 
         * For each str in strs:
         * get hashed key, push the str to its value array.
         * 
         * return array
         * 
         * 
         * Time complexity: m * n
         * Space complexity: m
         * 
         * m = number of strings
         * n = longest length of string
         */

        const getAlphabetIndex = (char: string) => char.toLowerCase().charCodeAt(0) - 97;

        const outputMap: Map<string, string[]> = new Map();
        for (const str of strs) {
            const alphabetFrequencies = Array(26).fill(0);
            for (let c of str) {
                const alphabetIndex = getAlphabetIndex(c);
                alphabetFrequencies[alphabetIndex]++;
            }

            const hashedKey = alphabetFrequencies.join(",");
            if (outputMap.has(hashedKey)) {
                outputMap.get(hashedKey).push(str);
            } else {
                outputMap.set(hashedKey, [str]);
            }
        }

        return Array.from(outputMap.values());
    }
}
