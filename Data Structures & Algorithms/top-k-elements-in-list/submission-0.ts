class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        /**
         * map key: number, value: frequency
         * time: O(n), space: O(n)
         * 
         * map2: key: frequency, value: list of numbers
         * time: O(n), space: O(n)
         * 
         * array: unique set of frequencies 1 to n
         * Index: 0,1, ... n-1
         * Value: array of numbers at each frequency
         * 
         */
        const freqMap = new Map<number, number>();
        for (const num of nums) {
            if (!freqMap.has(num)) {
                freqMap.set(num, 0);
            }
            freqMap.set(num, freqMap.get(num) + 1);
        }

        const freqGroupingArray = Array.from({ length: nums.length }, () => []);

        // freq <= n always
        for (const [num, freq] of freqMap.entries()) {
            freqGroupingArray[freq-1].push(num);
        }

        const kFrequent: number[] = [];        
        for (let i=nums.length-1; i>=0; i--) {
            const elements = freqGroupingArray[i];
            if (elements.length === 0) {
                continue;
            }
            for (const element of elements) {
                kFrequent.push(element);
            }

            if (kFrequent.length >= k) {
                break;
            }
        }

        return kFrequent;
    }
}
